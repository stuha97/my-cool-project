import pytest
import requests

r = requests.get('https://dog.ceo/api/breeds/list/all')
r2 = requests.get('https://dog.ceo/api/breed/hound/list')


def test_get_all_breeds():
    response = r.json()
    print(response)
    assert response['status'] == 'success'


@pytest.mark.parametrize('code_status', [200])
def test_get_all_breeds_status_code(code_status):
    assert r.status_code == code_status


@pytest.mark.parametrize('breed', ['boxer'])
def test_get_boxer_breed(breed):
    response = r.json()
    assert breed in response['message']


@pytest.mark.parametrize('hound', ['afghan', 'basset', 'blood', 'english'])
def test_get_hound(hound):
    response = r2.json()
    assert hound in response['message']


def test_get_all_hound():
    response = r2.json()
    assert response['status'] == 'success'
