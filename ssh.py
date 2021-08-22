from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler
from netmiko import Netmiko
import datetime
import os
import json
import csv
import diff
import subprocess

def ssh_log(device):

  #josnファイル呼び出し
  json_open = open('input/device/'+device, 'r')
  remote_device_pre = json.load(json_open)
  remote_device = remote_device_pre["a"]
  remote_device_command = remote_device_pre["b"]

  json_open.close()

  now = datetime.datetime.now()

  #pingフラグ
  ping_flag = 0
  #sshフラグ
  ssh_flag=0

  #フォルダ作成
  new_path = "output"
  if not os.path.exists(new_path):#ディレクトリがなかったら
      os.mkdir(new_path)#作成したいフォルダ名を作成

  # ファイル準備
  device_file, ext = os.path.splitext( os.path.basename('input/device/'+device) )
  f = open("output/"+device_file+"_output_{0:%H%M%S}.txt".format(now), "w") # output_時間 のテキスト名
 

  #ping 確認
  res = subprocess.run(["ping",remote_device["ip"],"-n","2", "-w", "300"],stdout=subprocess.PIPE)
  #print(res.stdout.decode("cp932"))
  if res.returncode == 0 :
      print("[情報] "+device+ " ping成功")
      ping_flag = 1
  else:
      print("[エラー] "+device+ " ping失敗")

  #ssh接続できない時のエラーは無視します
  try:

    # 自動検出
    guesser = SSHDetect(**remote_device)
    best_match = guesser.autodetect()

    # 検出結果のデバッグ出力
    print("[情報] device_type: " + best_match)
    print("[情報] "+device+"実行中!!!")

    # 自動検出した device_type を再設定する
    remote_device['device_type'] = best_match
    connection = Netmiko(**remote_device)
    connection.enable() #enableパスワード入力

    # コマンド実行結果の出力
    #print(connection.send_command('show clock\nshow run'),file=f)

    #投入コマンド検知
    if "cisco" in best_match:
      remote_device_command["command"] = "command_cisco.txt" 
    
    elif "fujitsu" in best_match:
      remote_device_command["command"] = "command_fujitsu.txt" 

    #コマンドリスト
    command = open('input/command/'+remote_device_command["command"],'r')
    command_list = command.readlines()

    for i in range(len(command_list)):   # インデックス番号 0 から順に要素をスライスします。
      list_item = command_list[i]     # list 関数でリストの要素の数の分ループします。
      #コマンド出力結果を取得
      print(connection.send_command(command_list[i]),file=f)

    command.close()

    f.close()
    # 切断
    connection.disconnect()

    

    if ping_flag == 1: #ping OK
      #csv書き込み
      with open('output/取得結果.csv','a',newline="") as c:
        writer = csv.writer(c)
        writer.writerow([device,remote_device['ip'],"取得OK","Ping OK",datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),f.name])

    else: #ping NG
      with open('output/取得結果.csv','a',newline="") as c:
        writer = csv.writer(c)
        writer.writerow([device,remote_device['ip'],"取得OK","Ping NG",datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),f.name])
    
    ssh_flag = 1

  except :
    print("[エラー] "+device+" SSH接続できません。次の理由で接続できていません。netmikoが対象機器に対応していない。対象機器に不備がある。input/device配下ののjsonファイルに不備がある。")

    #csv書き込み
    if ping_flag == 1: #ping OK
      #csv書き込み
      with open('output/取得結果.csv','a',newline="") as c:
        writer = csv.writer(c)
        writer.writerow([device,remote_device['ip'],"取得NG","Ping OK",datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),f.name])

    else: #ping NG
      with open('output/取得結果.csv','a',newline="") as c:
        writer = csv.writer(c)
        writer.writerow([device,remote_device['ip'],"取得NG","Ping NG",datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),f.name])

    pass

  #diff path
  log_path = "input/config"
  log_file = os.listdir(log_path)
  #log_files = [f for f in log_file if os.path.isfile(os.path.join(log_path, f))]
  #print(log_file)

  for name in log_file:
    device2 = os.path.basename(device).split('.', 1)[0]
    device3 = device2 + "_"
    if device3 in name:
      #print(device2)
      diff.diff_log(device3)

  if ssh_flag == 1:
    return 1
  else:
    return 0
