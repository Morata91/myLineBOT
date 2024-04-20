import json
import os
from linebot import LineBotApi
from linebot.models import TextSendMessage

LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def lambda_handler(event, context):
    try:
        if event['events'][0]['type'] == 'message':
            if event['events'][0]['message']['type'] == 'text':
                replyToken = event['events'][0]['replyToken']
                if event['events'][0]['message']['type'] == 'text':
                    print('a')
                    if event['events'][0]['message']['text'] == 'ほりべ' or event['events'][0]['message']['text'] == '堀部':
                        print('h')
                        replyText = 'きょうへい'
                    elif event['events'][0]['message']['text'] == 'たかでら':
                        replyText = 'じゅんた♡'
                    else:
                        replyText = '誰？'
                    LINE_BOT_API.reply_message(replyToken, TextSendMessage(text=replyText))
        if event['events'][0]['type'] == 'follow':
            replyToken = event['events'][0]['replyToken']
            replyText = 'こんにちは！きょうへいだよ！'
            LINE_BOT_API.reply_message(replyToken, TextSendMessage(text=replyText))
            
    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': json.dumps('Exception occurred.')}
    return {'statusCode': 200, 'body': json.dumps('Reply ended normally.')}