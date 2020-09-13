## Author: Aleem Juma

from flask import request
from app import app, bot

@app.route('/bot', methods=['POST'])
def bot_response():
    response = bot.handle(request.form.to_dict())
    return str(response)
