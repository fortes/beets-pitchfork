from beets.plugins import BeetsPlugin
from beets import ui
from beets.dbcore import types

from optparse import OptionParser
from pitchfork_api import search

class PitchforkPlugin(BeetsPlugin):
    @property
    def album_types(self):
        return  {
            'pitchfork_description': types.STRING,
            'pitchfork_score': types.FLOAT,
            'pitchfork_url': types.STRING
        }

    def commands(self):
        return [PitchforkCommand(self.config, self._log)]

class PitchforkCommand(ui.Subcommand):
    def __init__(self, config, log):
        self._log = log

        parser = OptionParser(usage='%prog [options] [QUERY...]')
        parser.add_option(
            '-f', '--force',
            action='store_true', dest='force', default=False,
            help=u'force updating review if already present'
        )

        super(PitchforkCommand, self).__init__(
            parser=parser,
            name='pitchfork',
            help=u'get reviews from Pitchfork'
        )

    def func(self, lib, options, args):
        self.batch_fetch_reviews(lib, lib.albums(ui.decargs(args)), options.force)

    def batch_fetch_reviews(self, lib, albums, force):
        """Fetch review for each album"""
        for album in albums:
            rating = album.get('pitchfork_score')
            if rating != None and rating != '' and not force:
                message = ui.colorize('text_highlight_minor', u'has rating %s' % rating)
                self._log.info(u'{0}: {1}', album, message)
                continue

            try:
                self._log.debug(u'Querying {0.albumartist} - {0.album}', album)
                review = search(album['albumartist'], album['album'])
                score = float(review.score())
            except IndexError as e:
                self._log.debug(u'No review found: {0}', e)
                message = ui.colorize('text_error', u'no review found')
                self._log.info(u'{0}: {1}', album, message)
                continue

            message = ui.colorize('text_success', u'found review %s' % review.score())
            album['pitchfork_description'] = review.abstract()
            album['pitchfork_score'] = score
            album['pitchfork_url'] = 'https://pitchfork.com%s' % review.url
            album.store()
            self._log.info(u'{0}: {1}', album, message)
