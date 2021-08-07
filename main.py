# -*- coding: utf-8 -*-

import time
import diff
import ssh
import log_replace
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

#並列処理で実行
p=mp.Pool(4)
p.map(ssh.ssh_log,device_file)
p.close()
p.join()

"""
for dev in device_files:
    #tpe.submit(ssh.ssh_log(dev))
    ssh.ssh_log(dev)
"""

#logリプレース
log_path = "input/log"
config_path = "config/log"

#logフォルダの中身確認
files = os.listdir(log_path)
files = [f for f in files if not f.startswith(".")]
if not files:
    print("logフォルダが空なので終了します")
    sys.exit()
else:
    print("logフォルダあり")


log_file = os.listdir(log_path)
log_files = [f for f in log_file if os.path.isfile(os.path.join(log_path, f))]
print(log_files)

'''
for log in log_files:
    log_replace.replace(log)

#diff
for log in log_files:
    diff.diff_log(log)
'''

#finish
f = Figlet(font="slant")
msg = f.renderText("FINISH !")
print(msg)

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)+ "[sec]")

