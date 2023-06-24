# APIリファレンス
## About
講習会用のAPIのリファレンスです．

## API
### 天気予報 API（livedoor 天気互換）
|              |                                                     |
| ------------ | --------------------------------------------------- |
| 概要         | 3日間の天気，気温，降水確率，波の情報を提供します． |
| URL          | https://weather.tsukumijima.net/api/forecast        |
| ドキュメント | https://weather.tsukumijima.net/                    |
| 情報提供元   | ライブドア天気                                          |

### 洗濯指数API
|            |                                                                                                                                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 概要       | 今日と明日の洗濯指数を5段階で返します．                                                                                                                                                                  |
| API URL    | https://script.google.com/macros/s/AKfycbzh2BOv0C3MmuEO6TJbxlkAPehnlDi8S90Jue9ug-fFqXp4jwTlRFwpETRHgYawnOsK_Q/exec                                                                                       |
| 呼び出し方 | GET                                                                                                                                                                                                      |
| パラメータ | URL末尾に `?r=3/17/4610/14100/` のようなパラメタを付与し地域を指定する．数字は tenki.jp の末尾のものに同じ．例: https://tenki.jp/forecast/3/17/4610/14100/ であれば最後の"3/17/4610/14100/" を抜き取る． |
| 例         | `r = urequests.get('https://script.google.com/macros/s/AKfycbzh2BOv0C3MmuEO6TJbxlkAPehnlDi8S90Jue9ug-fFqXp4jwTlRFwpETRHgYawnOsK_Q/exec?r=3/17/4610/14100/')`                                             |
| 返り値     | 今日，明日の順で値が格納されたlist                                                                                                                                                                       |
| 情報提供元 | tenki.jp                                                                                                                                                                                                 |

### 暑さ指数API
|            |                                                                                                                                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 概要       | 今日と明日の暑さ指数を5段階で返します．                                                                                                                                                                  |
| API URL    | https://script.google.com/macros/s/AKfycbxK3kTLhWTnuGtP2qZqG9BU8RaRVN0tgL7DSimR8ns2pOaO0e5OUq3iwrA7sUTHcLlx/exec                                                                                         |
| 呼び出し方 | GET                                                                                                                                                                                                      |
| パラメータ | URL末尾に `?r=3/17/4610/14100/` のようなパラメタを付与し地域を指定する．数字は tenki.jp の末尾のものに同じ．例: https://tenki.jp/forecast/3/17/4610/14100/ であれば最後の"3/17/4610/14100/" を抜き取る． |
| 例         | `r = urequests.get('https://script.google.com/macros/s/AKfycbxK3kTLhWTnuGtP2qZqG9BU8RaRVN0tgL7DSimR8ns2pOaO0e5OUq3iwrA7sUTHcLlx/exec?r=3/17/4610/14100/')`                                               |
| 返り値     | 今日，明日の順で値が格納されたlist                                                                                                                                                                       |
| 情報提供元 | tenki.jp                                                                                                                                                                                                 |

### 遅延情報API
|            |                                                                                                                                                                            |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 概要       | 現在の関東地方の鉄道路線の運行情報を提供します．                                                                                                                           |
| API URL    | https://script.google.com/macros/s/AKfycbz1bKlQpnrxjo9dIZC0lIylyXgaZnZlVu4A9hU4X717M0K3tiAsfCRE4lFzpq43IMJX/exec                                                           |
| 呼び出し方 | GET                                                                                                                                                                        |
| パラメータ | URL末尾に `?name=路線名`の形で路線名を渡す．路線名は [Yahoo! 路線情報](https://transit.yahoo.co.jp/diainfo/area/4)のページに準拠する．路線名の[]や()も含めて一致させる必要がある．2バイト文字はURLエンコードする必要がある． |
| 例         | `r = urequests.get('https://script.google.com/macros/s/AKfycbz1bKlQpnrxjo9dIZC0lIylyXgaZnZlVu4A9hU4X717M0K3tiAsfCRE4lFzpq43IMJX/exec?name='+parse("東急東横線"))`                    |
| 返り値     | 現在の運行情報のテキスト                                                                                                                                                   |
| 情報提供元 | Yahoo! 路線情報 |

### LINE Notify API
|              |                                                                          |
| ------------ | ------------------------------------------------------------------------ |
| 概要         | LINE Notifyに通知を送信します．                                          |
| API URL      | https://notify-api.line.me/api/notify                                    |
| ドキュメント | [https://notify-bot.line.me/doc/ja/](https://notify-bot.line.me/doc/ja/) |
| 情報提供元   | LINE |
