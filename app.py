import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==


# GET /hello
# Returns 'Hello David!'
#   ; curl http://localhost:5001/hello

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name']

    return f"Hello {name}!"

# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"


# A method POST
# A path /submit
# Body parameters name and message

# # Request:
# POST /submit

# # With body parameters:
# name=Leo
# message=Hello world

# # Expected response (2OO OK):
# Thanks Leo, you sent this message: "Hello world"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    return f'Thanks {name}, you sent this message: "{message}"'

# A method GET
# A path /wave
# A query parameter name

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f'I am waving at {name}'


# A method POST
# A path /count_vowels
# A body parameter text

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    textlist = list(text.lower())
    vowels = [i for i in textlist if i in ['a', 'e', 'i', 'o', 'u']]
    count_vowels = len(vowels)
    return f'There are {count_vowels} vowels in "{text}"'


# POST /sort-names
#  Parameters:
#    names: Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):

@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['name']
    nameslist = names.split(',')
    sortnames = sorted(nameslist)
    newlist = ','.join(sortnames)
    return newlist


# CHALLENGE START

@app.route('/names', methods=['GET'])
def names():
    add = request.args.get('add', '')

    names = ['Julia', 'Alice', 'Karim']
    predefined_names = ', '.join(names)
    if add: 
        new_added = add.split(',')
        new_names = ', '.join(new_added)
        newlist = predefined_names + ', ' + new_names
        split_newlist = newlist.split(", ")
        sortnames = sorted(split_newlist)
        joined_names = ', '.join(sortnames)
        return joined_names


        # return f"{predefined_names}, {new_names}"
    # else:
    #     return sorted(list(predefined_names))







            

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

