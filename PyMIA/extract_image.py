# -*- coding: UTF-8 -*-
import os


def extractImage(video="", quant_de_images=1, formato="jpg", nome_da_imagem="Imagem"):
	#quant_de_images = Quantidade de imagens por segundo

	if video == "":
		print("[!] video can't is empty")

	comando = "ffmpeg -i {} -r {}  {}-%3d.{}".format(video, quant_de_images, nome_da_imagem, formato)
	os.system(comando)