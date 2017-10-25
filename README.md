## AI Deadlines

Countdown timers to keep track of a bunch of CV/NLP/ML/AI conference deadlines.

## Adding/updating a conference

* Fork the repository
* Update `_data/conferences.yml`
* Make sure it has the `name`, `year`, `id`, `link`, `deadline`, `date` and `place` attributes (and optionally `timezone`; default is Eastern Time)
* Send a pull request


After updating the conferences.yml, updade the deadlines running:

./create.py > index.html

## License

[MIT][1]

[1]: https://abhshkdz.mit-license.org/
[2]: http://aideadlin.es/
