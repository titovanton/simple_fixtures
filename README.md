# Simple Django fixtures

*Django fixtures* - is a very powerful tool, but it has inconvenient interface. *Simple fixtures* - is a simple wrapper over *Django fixtures*, which allows you to export and import data in a bulk mode. It handles common issues with such tables like `django_content_type`, using `--natural-foreign`(see *Django fixtures documentation*).

## Requirements

* Python 3.0 or higher
* Django 1.8 or higher

## Setup

There is only 1 setting:

    # settings.py

    FIXTURES_INDEX = 'main.fixtures_index'  # index file

The same, in this case, `main` app will have *fixtures* folder, after data has exported, or to use it for import.

## Index file

It must have iterable entity, every item must be in the format `<app_lable>.<model_low_case>`:

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

* `./manage.py make_fixtures` - export data
* `./manage.py load_fixtures` - import data
* `./manage.py models_list` - available models to be exported
