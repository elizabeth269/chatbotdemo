from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    response = chatbot(incoming_msg)
    msg.body(response)
    responded = True

    if not responded:
        msg.body('I apologize, I do not understand. Can you please rephrase your question?')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)