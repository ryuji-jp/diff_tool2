# coding: UTF-8
import datetime
import json
import os

def replace(file_name):

	#file.json読み込み
	json_open = open('input/log/'+file_name, 'r')
	before_file = json.load(json_open)

	#フォルダのpath取得
	f = open(before_file["before_file"])

	#プロンプト情報取得
	pmt = before_file["prompt"]

	#コマンド情報取得
	cmd = before_file["command"]
	
	line = f.readline()
	#line_replace = line.replace("\n", "")

	#抽出する内容を保存するテキスト作成 ファイル名に現在の時間を記載
	log_file, ext = os.path.splitext( os.path.basename('input/log/'+file_name) )
	now = datetime.datetime.now()
	file_write = open("output/config_"+log_file+"_{0:%H%M%S}.log".format(now), mode='w')

	print(file_name+" logリプレース実行中!!!")

	while line:
		
		if cmd in line: #show runから読み込み始める
			#file_write.writelines(line) #テキスト書き込み ⇒ show run 部分

			while line:
				line = f.readline()
				
				if pmt not in line: #プロンプトが帰ってきたら終了
					
					line_replace = line.replace("\n", "")
					#print(line_replace)

					file_write.writelines(line) #テキスト書き込み ⇒ show run の内容部分

				else:
					break
		line = f.readline()
		
	f.close()
	file_write.close()