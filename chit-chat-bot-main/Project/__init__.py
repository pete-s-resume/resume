# import imp
# from tkinter import image_names
from flask import Flask, request, abort
from linebot import LineBotApi
from linebot.models import ImageSendMessage,emojis,Emojis
# from linebot.exceptions import LineBotApiError
from Project.Clothes import *
import requests
import json
from Project.Config import  *
from Project.PriceAsking import *
from Project.whatsizeedit import *
from Project.Sorting import *
from Project.instock2 import *
from Project.discount import *
app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        print(payload)

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)
        User_Id = payload['events'][0]['source']['userId']
        print(User_Id)

        line_bot_api = LineBotApi(Channel_access_token)
        if message == "001":
            image_message = ImageSendMessage(
                original_content_url=white_shirt_o,
                preview_image_url=white_shirt_p
            )
            line_bot_api.push_message(User_Id,image_message)
        elif message == "002":
            image_message = ImageSendMessage(
                original_content_url=long_sleeved_white_o,
                preview_image_url=long_sleeved_white_p
            )
            line_bot_api.push_message(User_Id,image_message)
        elif message == "003":
            image_message = ImageSendMessage(
                original_content_url=white_hoodie_o,
                preview_image_url=white_hoodie_p
            )
            line_bot_api.push_message(User_Id,image_message)
        elif message == "004":
            image_message = ImageSendMessage(
                original_content_url=black_shirt_o,
                preview_image_url=black_shirt_p
            )  
            line_bot_api.push_message(User_Id,image_message)
        sen = ""
        sen = sorting(message)
        ans = ""
        if sen == "nothing" :
            ans = "สวัสดีครับคุณลูกค้า สอบถามอะไรดีครับ\n\nหากคุณลูกค้าต้องการซื้อสินค้า รบกวนพิมพ์คำว่า \"เอา\" ตามด้วยรหัสสินค้า ไซส์ และจำนวน\nตย. เอา 001 xl 1"  #สวัสดีครับคุณลูกค้า สอบถามอะไรดีครับ

        elif sen == "asksize" :
            ans = whatsize(message)
            image_message = ImageSendMessage(
                original_content_url=size_table_o,
                preview_image_url=size_table_p
            )
            line_bot_api.push_message(User_Id,image_message)

        elif sen == "askprize" :
            ans = AskPrice(message)
            Emojis(0,1,"5ac1bfd5040ab15980c9b435","009")

        elif sen == "order" :
            ans = finish(message)

        elif sen == "dis":
            ans = discount(message)

        elif sen == "have":
            image_message = ImageSendMessage(
                original_content_url=white_shirt_o,
                preview_image_url=white_shirt_p
            )
            line_bot_api.push_message(User_Id,image_message)
            image_message = ImageSendMessage(
                original_content_url=long_sleeved_white_o,
                preview_image_url=long_sleeved_white_p
            )
            line_bot_api.push_message(User_Id,image_message)
            image_message = ImageSendMessage(
                original_content_url=white_hoodie_o,
                preview_image_url=white_hoodie_p
            )
            line_bot_api.push_message(User_Id,image_message)
            image_message = ImageSendMessage(
                original_content_url=black_shirt_o,
                preview_image_url=black_shirt_p
            )
            line_bot_api.push_message(User_Id,image_message)
            ans ="เสื้อตัวบนสุดรหัสสินค้า 001 002 003 004 เรียงลงมาตามลำดับ\n\nหากคุณลูกค้าต้องการซื้อสินค้าตัวไหน รบกวนพิมพ์คำว่า \"เอา\" ตามด้วยรหัสสินค้า ไซส์ และจำนวน\nตย. เอา 001 xl 1"
            ReplyMessage(Reply_token,ans,Channel_access_token)

            # df = pd.DataFrame({'total':[0]})
            # writer = pd.ExcelWriter('total.xlsx', engine='xlsxwriter')
            # df.to_excel(writer, sheet_name='Sheet1', index=False)
            # writer.save()

        print(ans)
        ReplyMessage(Reply_token,ans,Channel_access_token)
        # try:
        #     line_bot_api.push_message('Ucaec5acf21ce73dc769e9881cd192907',image_message)
        # except LineBotApiError as e:
        #     print('e.status_code:', e.status_code)
        #     print('e.error.message:',e.error.message)
        #     print('e.error.details:',e.error.details)
        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(200)

@app.route('/')
def hello():
    return 'Hello, It is Chit-Chat-Shop',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) 
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200

def ReplyImage(Reply_token,TextImage,Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) 
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"image",
            "originalContentUrl":"https://images.unsplash.com/photo-1620799139507-2a76f79a2f4d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=772&q=80",
            "previewImageUrl":"https://i.imgur.com/VqvCVT6.jpeg"
        }] 
    }
    r = requests.post(LINE_API, headers=headers, data=data) 
    return '',200
