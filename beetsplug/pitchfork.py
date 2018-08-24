from beets.plugins import BeetsPlugin
from beets import ui
from beets.dbcore import types

from optparse import OptionParser
from pitchfork import search


class PitchforkPlugin(BeetsPlugin):
    def __init__(self):
        super(PitchforkPlugin, self).__init__()
        self.config.add({
            'auto': False,
        })

        if self.config['auto']:
            self.register_listener('album_imported', self.on_import)

    @property
    def album_types(self):
        return {
            'pitchfork_bnm': types.BOOLEAN,
            'pitchfork_description': types.STRING,
            'pitchfork_score': types.FLOAT,
            'pitchfork_url': types.STRING
        }

    def commands(self):
        return [PitchforkCommand(self.config, self._log)]

    def on_import(self, lib, album):
        fetch_review(album, self._log, False)


class PitchforkCommand(ui.Subcommand):
    def __init__(self, config, log):
        self._log = log

        parser = OptionParser(usage='%prog [options] [QUERY...]')
        parser.add_option(
            '-f',
            '--force',
            action='store_true',
            dest='force',
            default=False,
            help=u'force updating review if already present')

        super(PitchforkCommand, self).__init__(
            parser=parser,
            name='pitchfork',
            help=u'get reviews from Pitchfork')

    def func(self, lib, options, args):
        self.batch_fetch_reviews(lib, lib.albums(ui.decargs(args)),
                                 options.force)

    def batch_fetch_reviews(self, lib, albums, force):
        """Fetch review for each album"""
        for album in albums:
            fetch_review(album, self._log, force)


def fetch_review(album, log, force):
    rating = album.get('pitchfork_score')
    if rating != None and rating != '' and not force:
        message = ui.colorize('text_highlight_minor',
                              u'has rating %s' % rating)
        log.info(u'{0}: {1}', album, message)
        return

    try:
        log.debug(u'Querying {0.albumartist} - {0.album}', album)
        review = search(album['albumartist'], album['album'])
        score = float(review.score())
    except IndexError as e:
        log.debug(u'No review found: {0}', e)
        message = ui.colorize('text_error', u'no review found')
        log.info(u'{0}: {1}', album, message)
        return
    except Exception as e:
        log.debug(u'Error trying to get review: {0}', e)
        message = ui.colorize('text_error', u'could not fetch review')
        log.info(u'{0}: {1}', album, message)
        return

    message = ui.colorize('text_success', u'found review %s' % review.score())
    album['pitchfork_bnm'] = review.best_new_music()
    album['pitchfork_description'] = review.abstract()
    album['pitchfork_score'] = score
    album['pitchfork_url'] = 'https://pitchfork.com%s' % review.url
    album.store()
    log.info(u'{0}: {1}', album, message)
