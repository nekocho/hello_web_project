# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

# Names route
GET /names


```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# GET /names
#  Expected response (200 OK):
"""
Julia, Alice, Karim
"""

# GET /names?add=Leo
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Leo
"""

# GET /names?add=Eddie
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""

# GET /names?add=Eddie,Leo
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie, Leo
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /names
  Expected response (200 OK):
  "Julia, Alice, Karim"
"""
def test_get_names(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim'

"""
GET /names?add=Leo
  Expected response (200 OK):
  "Julia, Alice, Karim, Leo"
"""
def test_get_names_add_leo(web_client):
    response = web_client.get('/names?add=Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Leo'

"""
GET /names?add=Eddie
  Expected response (200 OK):
  "Julia, Alice, Karim, Eddie"
"""
def test_get_names_add_eddie(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

"""
GET /names?add=Eddie,Leo
  Expected response (200 OK):
  "Alice, Eddie, Julia, Karim"
"""
def test_get_names_add_leo_and_eddie(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie, Leo'


```
