import os
from linebot.v3.messaging import (
    MessagingApi,
    RichMenuRequest,
    Configuration,
    ApiClient,
    RichMenuArea,
    RichMenuBounds,
    URIAction,
    Action,
    PostbackAction,
)
import json
import requests

CHANNEL_ACCESS_TOKEN = os.environ['KYOUHEIBOT_ACCESS_TOKEN']
IMAGE_PATH = "../rich_menu/0001/rich_menu_image.png"
JSON_PATH = "../rich_menu/0001/rich_menu.json"



def main():
    # try:
    # MessagingApiインスタンスの作成
    configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
    with ApiClient(configuration) as api_client:
        messaging_api = MessagingApi(api_client)

    with open(JSON_PATH, "r", encoding="utf-8") as file:
        richmenu_content = json.load(file)

    # リッチメニューを作成
    rich_menu_request = RichMenuRequest(
        size=richmenu_content["size"],
        selected=True,  # デフォルトで表示するか
        name="お試し",  # 説明。ユーザーからは見えない
        chat_bar_text="メニュー",  # チャットバーに表示されるやつ
        areas=[
            RichMenuArea(  # リッチメニューのどの部分がタップ可能であるかを定義するための情報を含むオブジェクトの配列
                bounds=RichMenuBounds(x=0, y=0, width=1666, height=1686),
                action=PostbackAction(label="Kyouheiを評価", data="richmenu_0", displayText="Kyouheiを評価する")
            ),
            RichMenuArea(  # リッチメニューのどの部分がタップ可能であるかを定義するための情報を含むオブジェクトの配列
                bounds=RichMenuBounds(x=1667, y=0, width=834, height=843),
                action=PostbackAction(label="メニュー1", data="richmenu_1", displayText="メニュー1")
            ),
            RichMenuArea(  # リッチメニューのどの部分がタップ可能であるかを定義するための情報を含むオブジェクトの配列
                bounds=RichMenuBounds(x=1667, y=844, width=834, height=843),
                action=PostbackAction(label="メニュー2", data="richmenu_2", displayText="メニュー2")
            )
        ],
    )
    rich_menu_id = messaging_api.create_rich_menu(
        rich_menu_request=rich_menu_request
    ).rich_menu_id

    # リッチメニューに画像をアップロード
    url = f"https://api-data.line.me/v2/bot/richmenu/{rich_menu_id}/content"
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "image/png",
    }
    with open(IMAGE_PATH, "rb") as image_file:
        response = requests.post(url, headers=headers, data=image_file)
    if response.status_code == 200:
        print("リッチメニュー画像が正常にアップロードされました")
    else:
        print(f"エラーが発生しました: {response.status_code}")
        print(response.text)

    # デフォルトのリッチメニューを設定する
    messaging_api.set_default_rich_menu(rich_menu_id)
    print("リッチメニューが正常に作成されました")

    # except Exception as e:
    #     print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    print("送信先を確認した？(y/n)")
    user_input = input().strip().lower()
    if user_input == "y":
        main()
    else:
        print("送信をキャンセルしました")
