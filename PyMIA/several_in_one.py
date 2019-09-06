# -*- coding: UTF-8 -*-
import os


def severalInOne(pasta="", nome_do_video="video" , formato=""):
	if pasta == "":
		print("[!] folder cannot be empty")

	if os.path.exists(pasta) == False:
		print("[!] folder/directory does not exist")

	if formato == "":
		formato = os.listdir(pasta)[0].split('.')[1]

	with open(pasta + '/lista.txt', 'w') as videos:
		for video in os.listdir(pasta):
			videos.write("file " + video + '\n')


	comando =  "ffmpeg -f concat -safe 0 -i {}/lista.txt -c copy {}.{}".format(pasta, nome_do_video,formato)
	os.system(comando)
	os.remove(pasta + '/lista.txt')