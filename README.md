# Simple Django fixtures

*Django fixtures* - is a very powerful tool, but it has inconvenient interface. *Simple fixtures* - is a simple wrapper over *Django fixtures*, which allows you to export and import data in a bulk mode. It handles common issues with such tables like `django_content_type`, using `--natural-foreign`(see *Django fixtures documentation*).

## Requirements

* Python 3.0 or higher
* Django 1.8 or higher

## Setup

    # settings.py

    INSTALLED_APPS = [
        ...
        'simple_fixtures',
        ...
    ]

    FIXTURES_INDEX = 'main.fixtures_index'  # index file

`FIXTURES_INDEX` serves 2 purposes: allocate `fixtures_index` file and specify app label, where to put `fixtures` folder.

## Index file

It must have iterable entity, every item must be in the format `<app_lable>.<model_lower>`:

    # main/fixtures_index.py

    fixtures_index = (
        'mainapp.catalog',
        'mainapp.image',
        'mainapp.page',
        'mainapp.product',
        'mainapp.productimage',
        'news.news',
    )

To prevent any typos, use `./manage.py models_list`.

## Interface

There are 3 management commands:

* `./manage.py make_fixtures` - exports data, by using `fixtures_index` file
* `./manage.py load_fixtures` - imports data, by using `fixtures_index` file
* `./manage.py models_list` - shows available models to be exported
