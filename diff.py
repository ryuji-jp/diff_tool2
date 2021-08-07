# -*- coding: utf-8 -*-

import difflib as diff
import datetime
import os
import glob
from difflib import HtmlDiff
from plyer import notification


def diff_log(device_name):
	df = HtmlDiff()

	device_file, ext = os.path.splitext( os.path.basename('input/device/'+device_name) )
	#output 最新path抽出
	saishin_output = glob.glob("output/output_"+device_file+"*")
	saishin_output_file = max(saishin_output, key=os.path.getctime)

	#config 最新path抽出
	saishin_config = glob.glob("output/config_"+device_file+"*")
	saishin_config_file = max(saishin_config, key=os.path.getctime)

	#outpit_* ファイル
	with open(saishin_output_file,'r') as f:
		str_output = f.readlines()

	#config_* ファイル
	with open(saishin_config_file,'r') as g:
		str_config = g.readlines()

	#差分比較HTML
	now = datetime.datetime.now()
	file_write = open("output/diff_"+device_file+"_{0:%H%M%S}.html".format(now), mode='w')

	file_write.writelines(df.make_file(str_output, str_config))

	file_write.close()

	#差分抽出
	file_write_diff = open("output/diff_txt_"+device_file+"_{0:%H%M%S}.txt".format(now), mode='w')
	for i in diff.context_diff(str_output, str_config, fromfile=saishin_output_file, tofile=saishin_config_file):
		#print(i, end='')
		file_write_diff.writelines(i)
	file_write_diff.close()

	#diff.txt 最新path抽出
	saishin_diff = glob.glob('output/diff_txt_*')
	saishin_diff_file = max(saishin_diff, key=os.path.getctime)

	#diff_txt_ * ファイル
	with open(saishin_diff_file,'r') as h:
		str_diff = h.readlines()
	h.close()
	
	#diffの抽出	
	for str in str_diff:
		
		if str.startswith('- '):
			str_diff_replace = str.replace("\n", "")
			print(str_diff_replace)

		if str.startswith('+ '):
			str_diff_replace = str.replace("\n", "")
			print(str_diff_replace)

		elif str.endswith('---'):
			break
	





