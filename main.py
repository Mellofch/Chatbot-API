from flask import Flask, jsonify, request
import json
from test import chatbot_response  # Ensure this import is working and that chatbot_response is defined properly

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World! This is the chatbot API.</p>"

@app.route('/', methods=['POST'])
def returnChatbotResponse():
    # Check if the incoming request has JSON data
    if request.is_json:
        # Parse the JSON data, assuming it's correctly formatted
        data = request.get_json()
        userQuery = data.get('userQuery', '')  # Provide a default empty string if 'userQuery' is not in the JSON

        if userQuery:  # Check if userQuery is not empty
            response = chatbot_response(userQuery.lower())
            result = {
                "user_query": userQuery,
                "chatbot_response": response
            }
            return jsonify(result)
        else:
            return jsonify({"error": "userQuery is empty or not provided"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)

