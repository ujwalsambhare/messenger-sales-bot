
import json

from flask import Flask,request
from bot import Bot


PAGE_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
GREETINGS = ['Hi','hi' , 'Hii' ,  'hii', 'Hello','hello' , 'How are you']
ITEMS = ['Keyboard','Keyboard ','Mouse?','Mouse ?','I want mouse','I want keyboard','I want ram']
KEYBOARD_company = ['Zebronic','Logitech','Dell','Hp','Ibm']
Zebronic = 250
Logitech =450
Dell = 500
Hp= 600
Ibm =2500
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def webhook():
    if request.method =='GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == 'secret':
            return str(challenge)
        return '400'
    else:

        print(request.data)
        data = json.loads(request.data)
        messaging_events = data['entry'][0]['messaging']
        bot = Bot(PAGE_ACCESS_TOKEN)
        for message in messaging_events:
            user_id = message['sender']['id']
            text_input = message['message'].get('text')
 #input parts
            response_text = 'i am not understanding.  can you repeat it'

            if text_input in GREETINGS:
                response_text ='Hello ' "\n" 'These is ngptechie \n Computer sales and spare part services' "\n" 'how may i help you'

            elif text_input in ITEMS:
                response_text= 'Which company'

            elif text_input == 'Zebronic' in KEYBOARD_company:
                response_text=Zebronic
            elif text_input == 'Logitech' in KEYBOARD_company:
                response_text=Logitech
            elif text_input == 'Dell' in KEYBOARD_company:
                response_text=Dell
            elif text_input == 'Hp' in KEYBOARD_company:
                response_text=Hp
            elif text_input == 'Ibm' in KEYBOARD_company:
                response_text=Ibm
            print('message from user ID {} - {}'.format(user_id,text_input))
            bot.send_text_message(user_id,response_text)
        return '200'
if __name__== '__main__':
    app.run(debug=True)
