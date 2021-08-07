from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler
import datetime
import os
import json
import csv

def ssh_log(device):


  json_open = open('input/device/'+device, 'r')
  remote_device = json.load(json_open)

  json_open.close()

  now = datetime.datetime.now()

  #フォルダ作成
  new_path = "output"
  if not os.path.exists(new_path):#ディレクトリがなかったら
      os.mkdir(new_path)#作成したいフォルダ名を作成

  # ファイル準備
  device_file, ext = os.path.splitext( os.path.basename('input/device/'+device) )
  f = open("output/output_"+device_file+"_{0:%H%M%S}.txt".format(now), "w") # output_時間 のテキスト名

  
  #ssh接続できない時のエラーは無視します
  try:
    # 自動検出
    guesser = SSHDetect(**remote_device)
    best_match = guesser.autodetect()

    # 検出結果のデバッグ出力
    print("device_type: " + best_match)
    print(device+"実行中!!!")

    # 自動検出した device_type を再設定する
    remote_device['device_type'] = best_match
    connection = ConnectHandler(**remote_device)
    connection.enable() #enableパスワード入力

    # コマンド実行結果の出力
    #print(connection.send_command('show clock\nshow run'),file=f)

    command = open('input/command.txt','r')
    command_list = command.readlines()


    for i in range(len(command_list)):   # インデックス番号 0 から順に要素をスライスします。
      list_item = command_list[i]     # list 関数でリストの要素の数の分ループします。
      print (list_item)
      print(connection.send_command(command_list[i]),file=f)

    command.close()

    f.close()

    with open('output/取得結果.csv','a',newline="") as f:
      writer = csv.writer(f)
      writer.writerow([remote_device['username'],remote_device['ip'],"取得OK",datetime.datetime.now().strftime("%Y-%m-%d %H:%M")])

  # 切断
    connection.disconnect()

  except :
    print(device+" SSH接続できません")
    with open('output/取得結果.csv','a',newline="") as f:
      writer = csv.writer(f)
      writer.writerow([remote_device['username'],remote_device['ip'],"取得NG",datetime.datetime.now().strftime("%Y-%m-%d %H:%M")])
    pass

