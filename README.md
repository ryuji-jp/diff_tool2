# diff_tool2使い方

## diff_tool2でできること
* netmikoを使ってログ採取  
* 採取した端末の一覧をcsvに列挙  
* 事前ログがあれば、採取したログと比較  

## 準備
* netmikoをインストール
* input フォルダは以下のログイン情報を修正する

## フォルダ階層
* 以下はサンプルの階層となっております。
```
C:.
│  diff.py
│  main.py ★実行するpythonファイル
│  ssh.py
│
├─input ★利用者が事前に編集するフォルダ
│  │  command_cisco.txt
│  │  command_vyos.txt
│  │
│  ├─config ★比較対象ファイル
│  │      device1.txt
│  │      device3.txt
│  │
│  └─device ★機器情報記載ファイル
│          device1.json
│          device2.json
│          device3.json
│          device4.json
│
└─output ★本プログラム実行により、生成されるファイル
        diff_device1_141826.html
        diff_device3_141826.html
        diff_txt_device1_141826.txt
        diff_txt_device3_141826.txt
        output_device1_141811.txt
        output_device2_141811.txt
        output_device3_141811.txt
        output_device4_141811.txt
        取得結果.csv
```
## inputフォルダについて
### configフォルダ
* 事前コンフィグを格納して下さい。
* 事前コンフィグが無い場合は、特に何も格納しなくて大丈夫です。
* 事前コンフィグのファイル名は、deviceフォルダ内ファイルの名と対応するように命名して下さい。
```
 ├─config
 │      device1.txt
 │      device2.txt
 │
 └─device
         device1.json
         device2.json
```
### deviceフォルダ
* 機器のログイン情報を記載します。
* 機器1台に対して、1つのjsonファイルを作成して下さい。
* 以下を参考に作成して下さい。
```device1.json
{
	"a": {
		"device_type": "autodetect", ★変更しなくてよい
		"port": 22,                  ★ポート番号
		"ip": "192.168.2.111",       ★IPアドレス
		"username": "fnets",         ★ログインユーザ名
		"password": "fnets",         ★ログインパスワード
		"secret": "fnets"            ★enabaleパスワード
	},
	"b": {
		"command": "command_cisco.txt" ★ログイン後投入するコマンドファイル
	}
}
```
### command.txt
* device.jsonの```"command": "command_cisco.txt"```で投入するコマンドを指定します。
* 初めにcisco でいう```terminal length 0``` を記載して下さい。

## 実行方法
```
python main.py
```
## その他
* 何回かに1回エラーになる時があります。もう一回実行してみて下さい。
