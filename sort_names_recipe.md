# Sort names Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Sort names route
POST /sort-names
    names: string

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python


# POST /sort-names
#  Parameters:
#    names: Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):

"""
Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
#  Parameters: 
#    names: Yvonne,Ben,Angie,Liam
#  Expected response (200 OK):

"""
Angie,Ben,Liam,Yvonne
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

"""
# POST /sort-names
#  Parameters:
#    names: Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):
  Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'name': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
# POST /sort-names
#  Parameters:
#    names: Yvonne,Ben,Angie,Liam
#  Expected response (200 OK):
  Angie,Ben,Liam,Yvonne
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'name': 'Yvonne,Ben,Angie,Liam'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Angie,Ben,Liam,Yvonne'
```

