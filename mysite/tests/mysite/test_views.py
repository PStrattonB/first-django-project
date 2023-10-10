# test_views.py


# def test_index():
#     assert False  # This is a must fail

def test_index_ok(client):
    # Make a GET request to / and store the response object
    # using the Django tes client
    response = client.get('/')
    # Assert that the status_code is 200(OK)
    assert response.status_code == 200
