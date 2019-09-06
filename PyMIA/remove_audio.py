# -*- coding: UTF-8 -*-
import os


def removeAudio(video="", formato="", nome_do_video="audioRemoved"):

	if video == "":
		print("[!] video can't is empty")

	if formato == "":
		formato = video.split('.')[1]

	comando = "ffmpeg -i {} -an {}.{}".format(video, nome_do_video, formato)
	os.system(comando)