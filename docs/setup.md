# 環境構築ガイド

## 1. Thonnyのインストール
[このサイトからThonnyをダウンロードして](https://thonny.org/)インストールしてください。

## 2. NodeMCUのドライバをインストールする
[このサイトからドライバをダウンロードして](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)インストールしてください。
![image](https://github.com/Keio-AIConsortium/python-iot/assets/58695125/70139f70-5aa8-4985-9992-002f658cf5f1)


## 3. NodeMCUをPCに接続する
NodeMCUをPCに接続してください。

## 4. インタプリタを指定する
![image](https://github.com/Keio-AIConsortium/python-iot/assets/58695125/64b07f66-523a-4655-91d7-63fd51121dd2)

Thonnyを起動し、ツールバーのOptiion→Interpreterを選択。
一覧から"MicroPython (ESP8266)を選んでください。
また、下の"Port or WebREPL"で、"CP210x UART Bridge~"を選択してください。

## 5. エディタの設定
以下の2項目にチェック
![image](https://github.com/Keio-AIConsortium/python-iot/assets/58695125/d7bf9835-ae42-4fea-b494-22a2c048077a)

以上で環境構築は終了です。
必要に応じて言語、テーマ、フォントを設定してください。


## ご自分で購入されたマイコンを使用する場合
本講座でお配りするマイコンには、MicroPythonを実行するためのプログラムが事前にインストールされています。
ご自分で購入されたマイコンを使用する場合は、以下の手順でMicroPythonをインストールしてください。
なお、事前に前述のドライバのインストールが必要です。

### 1. MicroPythonのダウンロード
[このサイトからMicroPythonをダウンロードして](https://micropython.org/download/esp8266/)ください。

### 2. Pythonのインストール
#### Windows
管理者権限で開いたPowerShellで以下のコマンドを実行してください。
```pwsh
winget install python.python
```
#### Mac
[公式サイト](https://www.python.org/downloads/macos/)からインストーラをダウンロードし、実行してください。

#### Linux
ターミナルで以下のコマンドを実行してください。
```bash
sudo apt install python
```

### 3. esptool.pyのインストール
PowerShellなどのコマンドラインで以下のコマンドを実行してください。
```PowerShell
pip install esptool
```

### 4. NodeMCUをPCに接続する
NodeMCUをPCに接続し、デバイスマネージャーでポート番号を確認してください。

### 5. MicroPythonの書き込み
PowerShellなどのコマンドラインで以下のコマンドを実行してください。 
```PowerShell
esptool.py --port <ポート番号> erase_flash
esptool.py --port <ポート番号> --baud 460800 write_flash --flash_size=detect 0 <MicroPythonの.binファイル>
```
