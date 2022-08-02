def test_pytest_addoption(base_url, session):
    response = session.get(base_url)
    assert response.ok
