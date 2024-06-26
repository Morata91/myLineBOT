import os
from linebot.v3.messaging import (
    Configuration,
    MessagingApi,
    ApiClient,
    PushMessageRequest,
    BroadcastRequest,
    ReplyMessageRequest,
    TextMessage,
)

LINE_CHANNEL_ACCESS_TOKEN = os.environ['KYOUHEIBOT_ACCESS_TOKEN']
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
with ApiClient(configuration) as api_client:
    messaging_api = MessagingApi(api_client)

def push_message():
    # ユーザー、グループを指定
    user_id = 'USER_ID'  # ここに実際のユーザーIDを入れてください
    messages=[TextMessage(text="ああああ")]
    messaging_api.push_message(push_message_request=PushMessageRequest(to=user_id, messages=messages))
    print("プッシュメッセージを送信しました")

def broadcast():
    # 友達になっている人全てにメッセージを送信
    messages=[TextMessage(text="ああああ")]
    messaging_api.broadcast(broadcast_request=BroadcastRequest(messages=messages))
    print("ブロードキャストメッセージを送信しました")
    
def reply():
    messaging_api.reply_message(
            reply_message_request=ReplyMessageRequest(
                replyToken=event.reply_token,
                messages=[TextMessage(text="開発中です。しばらくお待ちください。")]
            )
            )

if __name__ == '__main__':
    broadcast()
