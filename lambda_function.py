import os
import json
from linebot.v3.webhooks import(
    Event,
    MessageEvent,
    PostbackEvent
    )
from linebot.v3.messaging import(
    Configuration,
    MessagingApi,
    ApiClient,
    ReplyMessageRequest,
    TextMessage,
    FlexContainer,
    FlexMessage,
    PushMessageRequest,
    StickerMessage
    
)

# lambdaの環境変数からLINE Botのチャネルアクセストークンを取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
# 俺のuserID
DEVELOPER_ID_1 = os.environ["DEVELOPER_ID_1"]
# 開発者2のuserID
DEVELOPER_ID_2 = os.environ["DEVELOPER_ID_2"]

configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
with ApiClient(configuration) as api_client:
    messaging_api = MessagingApi(api_client)

def lambda_handler(e, context):
    try:
        
        print(e)
        
        #各イベントのインスタンスが返される 
        event = Event.from_dict(e['events'][0])
        print(event)
        print(type(event))

        # メッセージイベントの場合
        if isinstance(event, MessageEvent):
            message_handler(event=event)
                
        # ポストバックイベントの場合
        elif isinstance(event, PostbackEvent):
            postback_handler(postback_event=event)
        # 送信取り消しイベントの場合
        elif event.type == 'unsend':
            pass
        # フォローイベントの場合
        elif event.type == 'follow':
            messages=[
                        TextMessage(
                            text="フォローされました\nuserID : "
                            + event.source.user_id
                        )
                    ]
            messaging_api.push_message(push_message_request=PushMessageRequest(to=DEVELOPER_ID_1, messages=messages))
            #管理者のフォロー通知以外のフォロー通知を管理者2に通知
            if event.source.user_id != DEVELOPER_ID_1:
                messaging_api.push_message(push_message_request=PushMessageRequest(to=DEVELOPER_ID_2, messages=messages))
            
            # フォローメッセージの送信
            messaging_api.reply_message(
            reply_message_request=ReplyMessageRequest(
                replyToken=event.reply_token,
                messages=[
                    TextMessage(text="フォローありがとう！\nきょうへいだよ🍏"),
                    StickerMessage(packageId='789',stickerId='10855')
                    ]
            )
            )
            
        # フォロー解除イベントの場合
        elif event.type == 'unfollow':
            pass
        # 参加イベントの場合
        elif event.type == 'join':
            pass
        # 退出イベントの場合
        elif event.type == 'leave':
            pass
        # メンバー参加イベントの場合
        elif event.type == 'memberJoined':
            pass
        # メンバー退出イベントの場合
        elif event.type == 'memberLeft':
            pass
        # 動画視聴完了イベントの場合
        elif event.type == 'videoPlayComplete':
            pass
        # ビーコンイベントの場合
        elif event.type == 'beacon':
            pass
        # アカウント連携イベントの場合
        elif event.type == 'accountLink':
            pass
    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': json.dumps('Exception occurred.')}

    return {'statusCode': 200, 'body': json.dumps('Reply ended normally.')}



#メッセージイベントのハンドラ
def message_handler(event: MessageEvent):
    # メッセージイベントのタイプがテキストの場合
    if event.message.type == 'text':
        print("aaaa")
        if event.message.text == "かわいい":
            messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='そうかな？')]
                )
            )
        elif event.message.text == "かっこいい":
            messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='ありがとう😍')]
                )
            )
        elif event.message.text == "ブス":
            messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='ひどい😭')]
                )
            )
        elif event.message.text == "堀部" or event.message.text == "ほりべ":
            messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='きょうへい')]
                )
            )
        elif event.message.text == "高寺" or event.message.text == "たかてら":
            messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='じゅんた')]
                )
            )
        else:
            messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='?')]
                )
            )
        
    elif event.message.type == 'image':
        messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='かわいいね🥰')]
                )
            )
    elif event.message.type == 'video':
        messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='すてき😘')]
                )
            )
    elif event.message.type == 'audio':
        pass
    elif event.message.type == 'file':
        messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='ふむふむ🤨')]
                )
            )
    elif event.message.type == 'location':
        messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[TextMessage(text='すぐ行くわ💪')]
                )
            )
    elif event.message.type == 'sticker':
        messaging_api.reply_message(
                ReplyMessageRequest(
                    replyToken=event.reply_token,
                    messages=[StickerMessage(packageId='6325', stickerId='10979913')]
                )
            )




# ポストバックイベントのハンドラ
def postback_handler(postback_event: PostbackEvent):
    print(type(postback_event))
    print(postback_event.reply_token)
    if postback_event.postback.data == "richmenu_0":
        with open('flex_message/0001.json', "r", encoding="utf-8") as file:
            fm_json = json.load(file)
        bubble_string = json.dumps(fm_json, ensure_ascii=False, indent=4)
        contents = FlexContainer.from_json(bubble_string)
        messages = [FlexMessage(alt_text="フレックスメッセージ", contents=contents)]
        messaging_api.reply_message(
            reply_message_request=ReplyMessageRequest(
                replyToken=postback_event.reply_token,
                messages=messages
            )
            )
    elif postback_event.postback.data == "richmenu_1":
        messaging_api.reply_message(
            reply_message_request=ReplyMessageRequest(
                replyToken=postback_event.reply_token,
                messages=[TextMessage(text="開発中です。しばらくお待ちください。")]
            )
            )
    elif postback_event.postback.data == "richmenu_2":
        messaging_api.reply_message(
            reply_message_request=ReplyMessageRequest(
                replyToken=postback_event.reply_token,
                messages=[TextMessage(text="開発中です。しばらくお待ちください。")]
            )
            )