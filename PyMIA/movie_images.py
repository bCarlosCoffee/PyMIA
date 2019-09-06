# -*- coding: UTF-8 -*-

import os

# transformar imagens em filme

def movieImages(pasta, frame_rate=1, nome_do_video="video", formato_do_video="mp4", formato_images="", libx264=True):
	if formato_images == "":
		formato_images = os.listdir(pasta)[0].split('.')[1]

	if libx264 == True:
		libx264 = "-c:v libx264"

	if libx264 == False:
		libx264 = ""

	comando = "ffmpeg -r {} -pattern_type glob -i {}/'*.{}' {} {}.{}".format(frame_rate, pasta, formato_images, libx264, nome_do_video, formato_do_video)

	os.system(comando)