# Pitchfork Plugin for Beets

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

## Credits

`pitchfork.py` is from [tejassharma96/pitchfork](https://github.com/tejassharma96/pitchfork), included in this repository temporarily until the upstream package is updated.

## License

MIT
