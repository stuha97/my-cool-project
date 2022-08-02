import random

import pytest
import requests


@pytest.mark.parametrize('url_brewe_default', ['https://api.openbrewerydb.org/breweries'])
def test_brewery_status_code(url_brewe_default):
    r = requests.get(url_brewe_default)
    assert r.status_code == 200


@pytest.mark.parametrize('postal_code', ['95492-6652'])
def test_exists_postal_code(postal_code):
    r = requests.get('https://api.openbrewerydb.org/breweries')
    response = r.text
    assert postal_code in response


def test_brew_search():
    param = 'dog'
    r = requests.get(f'https://api.openbrewerydb.org/breweries/search?query={param}')
    response = r.text
    assert param in response


def test_bre_per_page():
    page = random.randint(1, 40)
    r = requests.get(f'https://api.openbrewerydb.org/breweries?per_page={page}')
    assert len(r.json()) == page


def test_get_filter_by_type():
    list_type = ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor', 'closed']
    page = random.randint(1, 40)
    r = requests.get(f'https://api.openbrewerydb.org/breweries?by_type={random.choice(list_type)}&per_page={page}')
    assert r.status_code == 200
