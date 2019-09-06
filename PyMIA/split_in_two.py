# -*- coding: UTF-8 -*-
import os


def splitInTwo(video="", tempo1="00:01:00", nome_part_1="part1", tempo2="", nome_part_2="part2"):

	if video == "":
		print("[!] video can't is empty")

	if tempo2 == "":
		tempo2 = tempo1

	formato = video.split('.')[1]
	if os.path.exists(nome_part_1 + "." + formato) or os.path.exists(nome_part_2 + "." + formato):
		print("[!] name part one or name part two already exist")

	comando = "ffmpeg -i {} -t {} -c copy {}.{} -ss {} -codec copy {}.{}".format(video, tempo1, nome_part_1, formato, tempo2, nome_part_2, formato)

	os.system(comando)