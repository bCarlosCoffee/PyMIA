# -*- coding: UTF-8 -*-
import os


def convert(video="", formato="", nome_do_video=""):

	if video == "":
		print("[!] video can't is empty")

	if formato == "":
		formato = video.split('.')[1]

	if nome_do_video == "":
		nome_do_video = video.split('.')[0]

	comando = "ffmpeg -i {} -q:v 0 -q:a 0 {}Mod.{}".format(video, nome_do_video, formato)
	os.system(comando)