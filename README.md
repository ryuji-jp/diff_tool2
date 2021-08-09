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
## 実行方法
```
python main.py
```

