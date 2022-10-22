def test_brands(client):
    """
    GIVEN a Flask app
    WHEN the route '/brands/' is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/brands/')
    assert response.status_code == 200
    print(response.data)
    assert response.data