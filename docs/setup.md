# 環境構築ガイド

## 1. Thonnyのインストール
[このサイトからThonnyをダウンロードして](https://thonny.org/)インストールしてください。

## 1. NodeMCUのドライバをインストールする
[このサイトからドライバをダウンロードして](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)インストールしてください。

## 1. NodeMCUをPCに接続する
NodeMCUをPCに接続してください。

## 1. インタプリタを指定する
Thonnyを起動し、ツールバーのOptiion→Interpreterを選択。
一覧から"MicroPython (ESP8266)を選んでください。
また、下の"Port or WebREPL"で、"CP210x UART Bridge~"を選択してください。

以上で環境構築は終了です。
必要に応じて言語、テーマ、フォントを設定してください。


## ご自分で購入されたマイコンを使用する場合
本講座でお配りするマイコンには、MicroPythonを実行するためのプログラムが事前にインストールされています。
ご自分で購入されたマイコンを使用する場合は、以下の手順でMicroPythonをインストールしてください。
なお、事前に前述のドライバのインストールが必要です。

### 1. MicroPythonのダウンロード
[このサイトからMicroPythonをダウンロードして](https://micropython.org/download/esp8266/)ください。

### 1. Pythonのインストール
管理者権限で開いたPowerShellで以下のコマンドを実行してください。
```PowerShell
winget install python.python
```

### 1. esptool.pyのインストール
PowerShellなどのコマンドラインで以下のコマンドを実行してください。
```PowerShell
pip install esptool
```

### 1. NodeMCUをPCに接続する
NodeMCUをPCに接続し、デバイスマネージャーでポート番号を確認してください。

### 1. MicroPythonの書き込み
PowerShellなどのコマンドラインで以下のコマンドを実行してください。
```PowerShell
esptool.py --port <ポート番号> erase_flash
esptool.py --port <ポート番号> --baud 460800 write_flash --flash_size=detect 0 <MicroPythonの.binファイル>
```