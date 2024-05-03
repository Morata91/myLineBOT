import json
import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    PushMessageRequest,
)

from linebot.v3.messaging import FlexMessage, FlexContainer


LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
# 俺のuserID
DEVELOPER_ID_1 = os.environ["DEVELOPER_ID_1"]
# 開発者2のuserID
DEVELOPER_ID_2 = os.environ["DEVELOPER_ID_2"]
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)


def lambda_handler(event, context):
    with ApiClient(configuration) as api_client:
        print(event)
        line_bot_api = MessagingApi(api_client)
        reply_token = event["events"][0]["replyToken"]
        # フォローされたら
        if event["events"][0]["type"] == "follow":
            # 管理者に通知を送る
            line_bot_api.push_message(
                PushMessageRequest(
                    to=DEVELOPER_ID_1,
                    messages=[
                        TextMessage(
                            text="フォローされました\nuseID : "
                            + event["events"][0]["source"]["userId"]
                        )
                    ],
                )
            )
            line_bot_api.push_message(
                PushMessageRequest(
                    to=DEVELOPER_ID_2,
                    messages=[
                        TextMessage(
                            text="フォローされました\nuserID : "
                            + event["events"][0]["source"]["userId"]
                        )
                    ],
                )
            )

            # フォローメッセージの送信
            line_bot_api.push_message(
                PushMessageRequest(
                    to=event["events"][0]["source"]["userId"],
                    messages=[
                        TextMessage(
                            text='フォローありがとう！\nきょうへいだよ🍏'
                        )
                    ],
                )
            )
            # フレックスメッセージの送信
            with open("flex_message.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            bubble_string = json.dumps(data, ensure_ascii=False, indent=4)
            message = FlexMessage(
                alt_text="hello",
                contents=FlexContainer.from_json(bubble_string),
            )
            line_bot_api.push_message(
                PushMessageRequest(
                    to=event["events"][0]["source"]["userId"],
                    messages=[message],
                )
            )

        # メッセージが送られてきたら
        elif event["events"][0]["type"] == "message":
            # テキストメッセージのWebhookに対する処理
            if event["events"][0]["message"]["type"] == "text":
                got_text = event["events"][0]["message"]["text"]

                # フレックスメッセージの送信
                if got_text == "フレックス":
                    with open("flex_message.json", "r", encoding="utf-8") as file:
                        data = json.load(file)
                    bubble_string = json.dumps(data, ensure_ascii=False, indent=4)
                    message = FlexMessage(
                        alt_text="hello",
                        contents=FlexContainer.from_json(bubble_string),
                    )
                    line_bot_api.reply_message(
                        ReplyMessageRequest(reply_token=reply_token, messages=[message])
                    )
                elif got_text == "かわいい":
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=reply_token,
                            messages=[TextMessage(text="そうかな〜？")],
                        )
                    )
                elif got_text == "かっこいい":
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=reply_token,
                            messages=[TextMessage(text="照れちゃうよ〜〜〜")],
                        )
                    )
                elif got_text == "ブス":
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=reply_token,
                            messages=[TextMessage(text="ひどい、、、")],
                        )
                    )

                elif got_text == "堀部" or got_text == "ほりべ":
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=reply_token,
                            messages=[TextMessage(text="きょうへい")],
                        )
                    )
                elif got_text == "高寺" or got_text == "たかてら":
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=reply_token,
                            messages=[TextMessage(text="じゅんた")],
                        )
                    )

                else:
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=reply_token, messages=[TextMessage(text="?")]
                        )
                    )

    # try:
    #     if event['events'][0]['type'] == 'message':
    #         if event['events'][0]['message']['type'] == 'text':
    #             replyToken = event['events'][0]['replyToken']
    #             if event['events'][0]['message']['type'] == 'text':
    #                 print('a')
    #                 if event['events'][0]['message']['text'] == 'ほりべ' or event['events'][0]['message']['text'] == '堀部':
    #                     print('h')
    #                     replyText = 'きょうへい'
    #                 elif event['events'][0]['message']['text'] == 'たかでら':
    #                     replyText = 'じゅんた♡'
    #                 else:
    #                     replyText = '誰？'
    #                 LINE_BOT_API.reply_message(replyToken, TextSendMessage(text=replyText))
    #     if event['events'][0]['type'] == 'follow':
    #         replyToken = event['events'][0]['replyToken']
    #         replyText = 'こんにちは！きょうへいだよ！'
    #         LINE_BOT_API.reply_message(replyToken, TextSendMessage(text=replyText))

    # except Exception as e:
    #     print(e)
    #     return {'statusCode': 500, 'body': json.dumps('Exception occurred.')}
    # return {'statusCode': 200, 'body': json.dumps('Reply ended normally.')}
