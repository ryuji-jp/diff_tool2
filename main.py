# -*- coding: utf-8 -*-
import time
import diff
import ssh
import os
import sys
from pyfiglet import Figlet
import multiprocessing.dummy as mp 

#タイム測定のため
start = time.time()

#ssh
device_path = "input/device"

device_file = os.listdir(device_path)
device_files = [f for f in device_file if os.path.isfile(os.path.join(device_path, f))]

str = ",".join(device_file)
print("[情報] ログ取得対象機器："+str)

#並列処理で実行
p=mp.Pool(len(device_file))
p.map(ssh.ssh_log,device_file)
p.close()
p.join()


#logリプレース
log_path = "input/config"
config_path = "input/config"

#configフォルダの中身確認
files = os.listdir(config_path)
files = [f for f in files if not f.startswith(".")]
if not files:
    print("[情報] configフォルダが空なので終了します")

    #finish
    f = Figlet(font="slant")
    msg = f.renderText("FINISH !") 
    print(msg)
    elapsed_time = time.time() - start
    print ("[情報] 処理時間:{0}".format(elapsed_time)+ "[sec]")
    sys.exit()

else:
    print("[情報] configフォルダあり")


log_file = os.listdir(log_path)
log_files = [f for f in log_file if os.path.isfile(os.path.join(log_path, f))]
#print(log_files)

'''
try:
    for log in log_files:
        log_replace.replace(log)
except:
    print("logファイルの記載が間違いです。input/log配下のjsonファイルの見直しをしてください")
'''

#diff
for log in log_files:
    diff.diff_log(log)

#finish
f = Figlet(font="slant")
msg = f.renderText("FINISH !")
print(msg)

elapsed_time = time.time() - start
print ("[情報] 処理時間:{0}".format(elapsed_time)+ "[sec]")

