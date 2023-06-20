from flask import Flask
from dotenv import load_dotenv
import os


# load environment variables
load_dotenv()

app = Flask(__name__)
 
 
@app.route('/<random_string>')
def return_reversed_string(random_string):
    # take a string, reverse and return it 
    return "".join(reversed(random_string))

@app.route('/get-mode')
def get_mode():
    # return the env mode .eg. dev, prod, .etc
    return os.environ.get("MODE")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)