import os
import json
from linebot.v3.messaging import (
    Configuration,
    MessagingApi,
    ApiClient,
    PushMessageRequest,
    BroadcastRequest,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage,
    FlexContainer,
)



LINE_CHANNEL_ACCESS_TOKEN = os.environ['KYOUHEIBOT_ACCESS_TOKEN']
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
with ApiClient(configuration) as api_client:
    messaging_api = MessagingApi(api_client)

def main():
    
    with open('../flex_message/0001.json', "r", encoding="utf-8") as file:
        fm_json = json.load(file)
    bubble_string = json.dumps(fm_json, ensure_ascii=False, indent=4)

    # フレックスメッセージを作成
    #alt_textが通知に表示される
    contents = FlexContainer.from_json(bubble_string)
    messages = [FlexMessage(alt_text="フレックスメッセージ", contents=contents)]
    

    ###全員に
    messaging_api.broadcast(broadcast_request=BroadcastRequest(messages=messages))
    print("フレックスメッセージを送信しました")

if __name__ == '__main__':
    print("送信先を確認した？(y/n)")
    user_input = input().strip().lower()
    if user_input == 'y':
        main()
    else:
        print("送信をキャンセルしました")
