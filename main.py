# -*- coding: utf-8 -*-
import time
import diff
import ssh
import os
import sys
import multiprocessing.dummy as mp 
import shutil

#タイム測定のため
start = time.time()

#outputフォルダ初期化
shutil.rmtree('output')
os.mkdir('output')

#対象機器のjsonファイル読み込み
device_path = "input/device"

device_file = os.listdir(device_path)
device_files = [f for f in device_file if os.path.isfile(os.path.join(device_path, f))]

str_json = ",".join(device_file)
print("[情報] ログ取得対象機器："+str_json)


#並列処理で実行
'''
何並列で実行するか
'''
p=mp.Pool(5) #現状5並列

return_list = (p.map(ssh.ssh_log,device_file))

'''
実行間隔を何秒にするか
'''

time.sleep(1) #実行間隔 現状1秒

p.close()
p.join()

config_path = "input/config"

#configフォルダの中身確認
files = os.listdir(config_path)
files = [f for f in files if not f.startswith(".")]
if not files:
    print("[情報] configフォルダが空なので終了します")

    #finish
    print("    ___________   ___________ __  __   __")
    print("   / ____/  _/ | / /  _/ ___// / / /  / /")
    print("  / /_   / //  |/ // / \__ \/ /_/ /  / / ")
    print(" / __/ _/ // /|  // / ___/ / __  /  /_/  ")
    print("/_/   /___/_/ |_/___//____/_/ /_/  (_)   ")

    elapsed_time = time.time() - start
    print ("[情報] 処理時間:{0}".format(elapsed_time)+ "[sec]")

    #成功数、エラー数表示
    return_sum = sum(return_list)
    return_len = len(return_list)
    return_err = return_len - return_sum
    print ("[情報] 対象機器:"+ str(return_len) +" 成功:"+ str(return_sum) +" エラー:"+ str(return_err))
    sys.exit()

else:
    print("[情報] configフォルダあり")

#finish
print("    ___________   ___________ __  __   __")
print("   / ____/  _/ | / /  _/ ___// / / /  / /")
print("  / /_   / //  |/ // / \__ \/ /_/ /  / / ")
print(" / __/ _/ // /|  // / ___/ / __  /  /_/  ")
print("/_/   /___/_/ |_/___//____/_/ /_/  (_)   ")

elapsed_time = time.time() - start
print ("[情報] 処理時間:{0}".format(elapsed_time)+ "[sec]")

#成功数、エラー数表示
return_sum = sum(return_list)
return_len = len(return_list)
return_err = return_len - return_sum

print ("[情報] 対象機器:"+ str(return_len) +" 成功:"+ str(return_sum) +" エラー:"+ str(return_err))
