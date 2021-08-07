# diff_tool2使い方

## diff_tool2でできること
* netmikoを使ってログ採取  
* 採取した端末の一覧をcsvに列挙  
* 事前ログがあれば、採取したログと比較  

## 準備
* netmikoをインストール
* input フォルダは以下のログイン情報を修正する

## フォルダ階層
```
│  diff.py 〇基本いじらなくてよい
│  log_replace.py 〇基本いじらなくてよい
│  main.py 〇python main.py で実行します
│  ssh.py 〇基本いじらなくてよい
│
├─input ★事前に利用者が設定するフォルダ
│  │  command.txt ★リモートログイン時、実行するコマンドリスト
│  │
│  ├─config ★比較する事前コンフィグ
│  │      config1.log
│  │      config2.log
│  │
│  ├─device ★リモート接続する機器の情報を記載する(ip,pwなど)
│  │      device1.json
│  │      device2.json
│  │      device3.json
│  │
│  └─log ★ログ比較をする際に情報を記載する()
│          device1.json
│          device2.json
│
└─output ■本ツール実行時に作成されるアウトプット
        output_device1_225141.txt ■ログ
        output_device2_225141.txt ■ログ
        output_device3_225141.txt ■ログ
        取得結果.csv ■取得情報をまとめたcsv
```
## 実行方法
```
python main.py
```

