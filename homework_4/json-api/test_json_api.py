import pytest
import requests


def test_get_json_status_code():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.ok


@pytest.mark.parametrize('url_json', ['https://jsonplaceholder.typicode.com/posts'])
@pytest.mark.parametrize('user_id', [1, 2, 3, 4, 5])
def test_post_method_status_code(url_json, user_id):
    response = requests.post(url_json, json={
        'title': 'foo',
        'body': 'bar',
        'userId': user_id})
    assert response.ok


@pytest.mark.parametrize('url_json', ['https://jsonplaceholder.typicode.com/posts/1'])
@pytest.mark.parametrize('user_id', [1])
def test_patch_method_status_code(url_json, user_id):
    response = requests.patch(url_json, json={
        'title': 'boo',
        'userId': user_id})
    assert response.ok


@pytest.mark.parametrize('url_json', ['https://jsonplaceholder.typicode.com/posts/1'])
def test_put_method_status_code(url_json):
    response = requests.patch(url_json, json={
        'id': 1,
        'title': 'foo',
        'body': 'bar',
        'userId': 10})
    assert response.ok


@pytest.mark.parametrize('url_json', ['https://jsonplaceholder.typicode.com/posts/1'])
def test_delete_method_status_code(url_json):
    response = requests.delete(url_json, json={
        'id': 1,
        'title': 'foo',
        'body': 'bar',
        'userId': 10
    })
    assert response.ok
