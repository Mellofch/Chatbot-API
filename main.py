from flask import Flask, jsonify, request
from test import chatbot_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! this is chatbot api</p>"

@app.route('/chat', methods=['POST'])
def returnChatbotResponse():
    if request.method == 'POST':
        # Assuming JSON data is sent, adjust accordingly if using form data
        data = request.get_json()
        userQuery = data.get('userQuery')

        if not userQuery:
            return jsonify({"error": "No user query provided"}), 400
        
        try:
            chat_response = chatbot_response(userQuery.lower())
            result = {
                "user_query": userQuery,
                "chatbot_response": chat_response
            }
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # Changed localhost to 0.0.0.0 for broader accessibility

