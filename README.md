# Pitchfork Plugin for Beets

![build status](https://travis-ci.org/fortes/beets-pitchfork.svg?branch=master)

Plugin for [Beets](http://beets.io/) that adds ratings from [Pitchfork](https://pitchfork.com/).

## Installation

```
pip install git+git://github.com/fortes/beets-pitchfork.git@master
```

## Configuration

Make sure to add `pitchfork` to your `plugins` setting in `config.yaml`. In the unlikely event you don't have any other plugins, just add a new line like:

```
plugins: pitchfork
```

### Use

Fetch album ratings via:

```
beet pitchfork [options] [QUERY...]
```

* `-f`/`--force`: Force updating even if review already exists

Use `pitchfork_score` in your queries. You can find this year's highly rated albums in your library like so:

```
beet ls -a pitchfork_score:8..10 year:2018
```

The following fields are available via this plugin:

* `pitchfork_bnm`: Whether the album was designated [Best New Music](https://pitchfork.com/reviews/best/albums/)
* `pitchfork_description`: Review summary
* `pitchfork_score`: Numeric score
* `pitchfork_url`: Link to the actual review

## Changelog

* `0.0.3`: Add `pitchfork_bnm`, move back to `pitchfork` library
* `0.0.2`: Use `pitchfork_api` dependency
* `0.0.1`: First release

## Possible future work

* Auto-fetch review on import
* Allow manual specification for artist / album query in order to alleviate failures
* Consider some method of re-trying search if no result found
* Use [pre-scraped database](https://github.com/nolanbconaway/pitchfork-data) to avoid spamming Pitchfork servers

## License

MIT
