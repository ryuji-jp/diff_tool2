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
│  main.py
│  ssh.py
│
├─input
│  │  command_cisco.txt
│  │  command_vyos.txt
│  │
│  ├─config
│  │      device1.txt
│  │      device3.txt
│  │
│  └─device
│          device1.json
│          device2.json
│          device3.json
│          device4.json
│
└─output
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

