# LINEボット「Kyouhei bot」






## API集

### メッセージを送信

```
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {'"$KYOUHEIBOT_ACCESS_TOKEN"'}' \
-d '{
    "to": "userID",
    "messages":[
        {
            "type":"text",
            "text":"テキスト"
        }
    ]
}'
```

### リッチメニュー作成

```
curl -v -X POST https://api.line.me/v2/bot/richmenu \
-H 'Authorization: Bearer {'"$KYOUHEIBOT_ACCESS_TOKEN"'}' \
-H 'Content-Type: application/json' \
-d \
'{
    "size": {
        "width": 2500,
        "height": 1686
    },
    "selected": false,
    "name": "デフォルトのリッチメニューのテスト",
    "chatBarText": "Tap to open",
    "areas": [
        {
            "bounds": {
                "x": 0,
                "y": 0,
                "width": 1666,
                "height": 1686
            },
            "action": {
                "type": "uri",
                "label": "タップ領域A",
                "uri": "https://developers.line.biz/ja/news/"
            }
        },
        {
            "bounds": {
                "x": 1667,
                "y": 0,
                "width": 834,
                "height": 843
            },
            "action": {
                "type": "uri",
                "label": "タップ領域B",
                "uri": "https://lineapiusecase.com/ja/top.html"
            }
        },
        {
            "bounds": {
                "x": 1667,
                "y": 844,
                "width": 834,
                "height": 843
            },
            "action": {
                "type": "uri",
                "label": "タップ領域C",
                "uri": "https://techblog.lycorp.co.jp/ja/"
            }
        }
    ]
}'
```
リッチメニューのIDが返ってくる。
そのIDと、使用する背景画像に置き換えて以下のコマンドで画像の設定。
```
curl -v -X POST https://api-data.line.me/v2/bot/richmenu/{richmenu-ID}/content \
-H "Authorization: Bearer {'"$KYOUHEIBOT_ACCESS_TOKEN"'}" \
-H "Content-Type: image/png" \
-T richmenu.png
```
```
curl -v -X POST https://api.line.me/v2/bot/user/all/richmenu/{richmenu-ID} \
-H "Authorization: Bearer {'"$KYOUHEIBOT_ACCESS_TOKEN"'}"
```
### リッチメニューの削除
```
curl -v -X DELETE https://api.line.me/v2/bot/richmenu/{} \
-H 'Authorization: Bearer {'"$KYOUHEIBOT_ACCESS_TOKEN"'}'
```
