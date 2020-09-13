## Author: Aleem Juma

# Developed using tutorial:
# https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio

from twilio.twiml.messaging_response import MessagingResponse
import requests

"""
    key                 :   value
    ---------------------------------------------------------------------
    SmsSid              :   message_id ("MM" + 32-digit hex string)
    SmsMessageSid       :   message_id
    MessageSid          :   message_id
    AccountSid          :   account_id ("AC" + 32-digit hex string)
    SmsStatus           :   accepted, queued, sending, sent, failed, delivered, undelivered, receiving, received, read (https://www.twilio.com/docs/sms/api/message-resource#message-status-values)
    From                :   "whatsapp:" + phone_number (E.164 format)
    To                  :   "whatsapp:" + phone_number (E.164 format)
    Body                :   body_text_string
    NumSegments         :   number of SMS messages it took to deliver the body of the message
    NumMedia            :   number of media parts
    MediaContentType{n} :   mime type of media part {n}
    MediaUrl{n}         :   url for media part {n} usually https://api.twilio.com/{api_ver}/Accounts/{account_id}/Messages/{message_id}/Media/{media_id}
    ApiVersion          :   2010-04-01
"""

def handle(args):
    """
    Analyses the incoming message and constructs an appropriate response

    Parameters:
      args     dict of key, value pairs from the incoming POST request
               based on the Twilio ML request format. For details see
               https://www.twilio.com/docs/sms/twiml#twilios-request-to-your-application
    
    Returns:
      resp     twilio.twiml.messaging_response.MessagingResponse object
               containing the full constructed message to send as a response
    """
    incoming_msg = args.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    if 'quote' in incoming_msg:
        quote = get_quote()
        msg.body(quote)
    elif 'cat' in incoming_msg:
        cat_pic_url = get_cat_pic()
        msg.media(cat_pic_url)
    else:
        msg.body('I only know about famous quotes and cats, sorry!')
    return resp

def get_quote():
    # return a quote
    r = requests.get('https://api.quotable.io/random')
    if r.status_code == 200:
        try:
            data = r.json()
            return f'{data["content"]} ({data["author"]})'
        except:
            pass
    return 'I could not retrieve a quote at this time, sorry.'

def get_cat_pic():
    return 'https://cataas.com/cat'