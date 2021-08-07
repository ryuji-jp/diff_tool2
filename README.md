# diff_tool2使い方

## diff_tool2でできること
・netmikoを使ってログ採取  
・採取した端末の一覧をcsvに列挙  
・事前ログがあれば、採取したログと比較  

## 準備
・netmikoをインストール

## フォルダ階層
'''bash
│  diff.py
│  log_replace.py
│  main.py
│  ssh.py
│
├─input
│  │  command.txt
│  │
│  ├─config
│  │      config1.log
│  │      config2.log
│  │
│  ├─device
│  │      device1.json
│  │      device2.json
│  │      device3.json
│  │
│  └─log
│          device1.json
│          device2.json
│
└─output
        output_device1_225141.txt
        output_device2_225141.txt
        output_device3_225141.txt
        取得結果.csv
'''
