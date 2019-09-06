# -*- coding: UTF-8 -*-
import os


def extractAudio(video="", formato="mp3", nome_do_audio="audio"):

	if video == "":
		print("[!] video can't is empty")


	comando = "ffmpeg -i {} -vn {}.{}".format(video, nome_do_audio,formato)
	os.system(comando)