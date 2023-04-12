# 環境構築ガイド

## OS共通
[Visual Studio Code](https://code.visualstudio.com/)をインストールする
https://code.visualstudio.com/

## Windows
Windowsストアで以下の3つのアプリを検索し，インストールする

### batファイルを起動
予め用意したインストールスクリプトを実行し、
- VSCode
- Python
- Nodejs
- Git
- micropy-cli
- pymakr
をインストール・設定する

### CP2102のドライバーを当てる
https://jp.silabs.com/interface/usb-bridges/classic/device.cp2102?tab=softwareandtools

### pymakrの設定を変更する
pymakrのGlobal settingsの"auto_connect"をfalseに変更する


## 参考資料
- https://zenn.dev/iot101/articles/b2e9c28f0bec39
- https://zenn.dev/nnabeyang/articles/3c8d6783f75190

## メモ
micropy-cliが依存しているnetifacesがpython3.9.13でインストール不可。C++ビルドツールが必要と言われる。whlファイルを落としてきて入れればできた
