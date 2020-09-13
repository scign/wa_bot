# Whatsapp bot using flask and twilio

Instructions:

As per [This article](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio)

* Start the flask server, either on your hosted platform or locally using ngrok

> If using ngrok, copy the `https://` URL from the ngrok output

> If using a hosted service, copy your service base URL

Once the flask server is running:
* Go to the Twilio Console
* -> Programmable Messaging
* -> Settings
* -> WhatsApp Sandbox Settings
* Paste your URL on the "When a message comes in" field
* Append `/bot` (if you haven't changed the endpoint in the code)
* Make sure the request method is set to `HTTP Post`
* Click Save
