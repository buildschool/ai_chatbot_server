# import dependencies
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import dotenv_values
import openai

# Define config
config = dotenv_values(".env")

# define openai key
openai.api_key = config['API_KEY']

# define flask app
app = Flask(__name__)

# use cors
CORS(app)

# define / route
@app.route('/', methods=["POST"])
def index():
    body = request.get_json()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=body['prompt'],
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return jsonify({"response":response})
