# PyMia

- Movies
- Images
- Audios

## Version: **0.1.0**

> Voce precisa ter o **[FFmpeg](https://www.ffmpeg.org/download.html)** instalado em seu computador.
&nbsp;

### Como usar:
   - ffmpeg instalado. ( __o programa foi testado com a versao: ffmpeg version 3.4.6-0ubuntu0.18.04.1 Copyright (c) 2000-2019 the FFmpeg developers__ )
   
   1. Exemplo de uso no **linux**
   ```bash
   git clone https://github.com/bCarlosCoffee/PyMIA.git
   ```
   - arquivo.py
   ```python
   
   from PyMIA.convert import convert
   
   # Função para converter videos para outros formatos
   convert('teste.mp4', 'mkv', 'formatado')
 
   ```

***

&nbsp;
&nbsp;
### Funções:
   ```python
      	from PyMIA.convert import convert
   ```
   > Converte videos para outros formatos.
   &nbsp;
   
   ```python
   	from PyMIA.extract_audio import extractAudio
   ```
   > Extrai audio de videos.
   &nbsp;
   
   ```python
   	from PyMIA.extract_image import extractImage
   ```
   > Extrai cenas de um video.
   &nbsp;
   
   ```python 
   	from PyMIA.movie_images import movieImages
   ```
   > Cria um filme de imagens.
   &nbsp;
   
   ```python	
   	from PyMIA.remove_audio import removeAudio
   ```
   > Remove audio de um video.
   &nbsp;
   
   ```python
   	from PyMIA.several_in_one import severalInOne
   ```
   > Junta varios videos em um só.
   &nbsp;
   
   
   ```python
   	from PyMIA.split_in_two import splitInTwo
   ```
   > Separa um video em 2 separados.
   &nbsp;
  


&nbsp;

## **PyMIA.convert**
```python
from PyMIA.converter import convert
```
- **Paramentros**
	- Video(str)  
	- Formato(str)
	- Nome do video finalizado(str)

***
### convert(video="") 

> Parametro **'video'** precisa receber ponto com formato!

```python
Errado
convert(video="meuVideo")
```

```python
Certo
convert(video="meuVideo.mp4")
```
***
### convert(formato="")

 >Paramentro **'formato'** não pode receber pontos!
 
 ```python
 Errado
 convert(formato=".mp4")
 ```
```python
Certo
convert(formato="mp4")
```
Se o parametro **'formato'** não receber argumento
Por padrão ele irá ser o mesmo **formato do original**

***

### convert(nome_do_video="")


> Parametro **'nome_do_video'** não pode receber pontos!

```python
Errado
convert(nome_do_video="finalizado.mkv")
```

```python
Certo
convert(nome_do_video="finalizado")
```

Se o parametro **'nome_do_video'** não receber argumento
Por padrão ele irá **renomear o video finalizado**
com o **mesmo nome do video original**

***


&nbsp;
## **PyMIA.extractAudio**

```python
from PyMIA.extract_audio import extractAudio
```
- **Paramentros**
	- Video(str)  
	- Formato(str)
	- Nome do audio finalizado(str)

***


### extractAudio(video="") 

> Parametro **'video'** precisa receber ponto com formato!

```python
Errado
extractAudio(video="meuVideo")
```

```python
Certo
extractAudio(video="meuVideo.mp4")
```

***

### extractAudio(formato="")

 >Paramentro **'formato'** não pode receber pontos!
 
 ```python
 Errado
 extractAudio(formato=".mp4")
 ```
```python
Certo
extractAudio(formato="mp4")
```
Se o parametro **'formato'** não receber argumento
Por padrão ele irá ser  **.mp3**

***

### extractAudio(nome_do_audio="")


> Parametro **'nome_do_audio'** não pode receber pontos!

```python
Errado
extractAudio(nome_do_audio="finalizado.mp3")
```

```python
Certo
extractAudio(nome_do_audio="finalizado")
```

Se o parametro **'nome_do_audio'** não receber argumento
Por padrão ele irá **renomear o audio finalizado para audio**

***


&nbsp;
## **PyMIA.extractImage**

```python
from PyMIA.extract_image import extractImage
```
- **Paramentros**
	- Video(str)  
	- quantidade de images por segundo (int)
	- formato(str)
	- nome da Imagem(str)

***


### extractImage(video="") 

> Parametro **'video'** precisa receber ponto com formato!

```python
Errado
extractImage(video="meuVideo")
```

```python
Certo
extractImage(video="meuVideo.mp4")
```

***

### extractImage(quant_de_images="")

 >Paramentro **'quant_de_images'** não pode receber pontos!
 
 ```python
 Errado
 extractImage(quant_de_images=".2")
 ```

```python
Certo
extractImage(quant_de_images="60")
```
Padrão: **1**

***

### extractImage(formato="")

> Parametro **'formato'** não pode receber pontos!

```python
Errado
extractImage(formato=".png")
```

```python
Certo
extractImage(formato="png")
```

Padrão Formato: **jpg**


***


### extractImage(nome_da_imagem="")


> Parametro **'nome_da_imagem'** não pode receber pontos!

```python
Errado
extractImage(nome_da_imagem="finalizado.png")
```

```python
Certo
extractImage(nome_da_imagem="finalizado")
```

Padrão nome dá Imagem: **Imagem**

***


&nbsp;
## **PyMIA.movie_images**

```python
from PyMIA.movie_images import movieImages
```
- **Paramentros**
	- pasta(str)  
	- frame_rate (int) imagens por segundo
	- nome_do_video(str)
	- formato_do_video(str)
	- formato_images(str)
	- libx264(bool)

***


### movieImages(pasta="") 

> Parametro **'pasta'** não pode receber ponto com formato!

```python
Errado
movieImages(video="img.png")
```

```python
Certo
movieImages(video="pasta_img")
```

***

### movieImages(frame_rate="")

 >Paramentro **'frame_rate'** não pode receber pontos!
 
 ```python
 Errado
 movieImages(frame_rate=".2")
 ```

```python
Certo
movieImages(frame_rate="1")
```
Padrão: **1**

***

### movieImages(nome_do_video="")

> Parametro **'nome_do_video'** não pode receber pontos!

```python
Errado
movieImages(nome_do_video="meuvideo.mkv")
```

```python
Certo
movieImages(nome_do_video="meuvideo")
```

Padrão Nome do video: **video**

### movieImages(formato_do_video="")


> Parametro **'formato_do_video'** não pode receber pontos!

```python
Errado
movieImages(formato_do_video=".mkv")
```

```python
Certo
movieImages(formato_do_video="mkv")
```

Padrão formato do video: **mp4**

***

### movieImages(formato_images="")


> Parametro **'formato_images'** não pode receber pontos!

```python
Errado
movieImages(formato_images=".png")
```

```python
Certo
movieImages(formato_images="png")
```

Padrão formato das imagens: é o mesmo formato da primeira 
imagem que estiver dentro dá pasta 

***


### movieImages(libx264="")


> Parametro **'libx264'** só pode ser True ou False!

```python
Errado
movieImages(libx264="False")
```

```python
Certo
movieImages(libx264=False)
```

Padrão libx264: **True**

***


&nbsp;
## **PyMIA.removeAudio**

```python
from PyMIA.remove_audio import removeAudio
```
- **Paramentros**
	- Video(str)  
	- formato(str)
	- nome do video(str)

***


### removeAudio(video="") 

> Parametro **'video'** precisa receber ponto com formato!

```python
Errado
removeAudio(video="meuVideo")
```

```python
Certo
removeAudio(video="meuVideo.mp4")
```

***

### removeAudio(formato="") 

> Parametro **'formato'** não pode receber pontos

```python
Errado
removeAudio(formato=".mp4")
```

```python
Certo
removeAudio(formato="mp4")
```

Padrão nome do video finalizado: **audioRemoved**
Padrão formato: é o mesmo formato do video original

***


&nbsp;
## **PyMIA.severalInOne**

```python
from PyMIA.several_in_one import severalInOne
```
- **Paramentros**
	- pasta(str)  
	- nome do video(str)
	- formato(str)
	
obs: Essa função apaga a pasta com os vídeos depois de juntar os vídeos.

***


### severalInOne(pasta="") 

> Parametro **'pasta'** não pode receber só um video!

```python
Errado
severalInOne(pasta="meuVideo.mp4")
```

```python
Certo
severalInOne(pasta="videos")
```

***

### severalInOne(nome_do_video="") 

> Parametro **'nome_do_video'** não pode receber pontos

```python
Errado
severalInOne(nome_do_video=".mp4")
```

```python
Certo
severalInOne(nome_do_video="mp4")
```

Padrão nome do video finalizado: **video**
Padrão formato: é o mesmo formato do video original

***


&nbsp;
## **PyMIA.splitInTwo**

```python
from PyMIA.split_in_two import splitInTwo
```
- **Paramentros**
	- video(str)
	- tempo1(str)
	- nome do video 1(str)
	- tempo2(str)
	- nome do video 2(str)

***


### splitInTwo(video="") 

> Parametro **'video'** precisa do formato

```python
Errado
splitInTwo(video="meuVideo")
```

```python
Certo
splitInTwo(video="meuVideo.mp4")
```

***

### splitInTwo(tempo1="") 

> Parametro **'tempo1'** não pode receber pontos

```python
Errado
splitInTwo(tempo1="23")
```

```python
Certo
splitInTwo(tempo1="00:04:00") #Precisa ser nesse formato!!
```

Padrão do tempo1: **"00:01:00"**

***

### splitInTwo(nome_part_1="") 

> Parametro **'nome_part_1'** não pode receber pontos

```python
Errado
splitInTwo(nome_part_1="part1.mp4")
```

```python
Certo
splitInTwo(nome_part_1="part1") #Precisa ser nesse formato!!
```

Padrão do tempo1: **"part1"**

***

### splitInTwo(tempo2="") 

> Parametro **'tempo2'** não pode receber pontos

```python
Errado
splitInTwo(tempo2="23")
```

```python
Certo
splitInTwo(tempo2="00:04:00") #Precisa ser nesse formato!!
```

Padrão do tempo2: **é igual tempo1**

***

### splitInTwo(nome_part_2="") 

> Parametro **'nome_part_2'** não pode receber pontos

```python
Errado
splitInTwo(nome_part_2="part2.mp4")
```

```python
Certo
splitInTwo(nome_part_2="part2") #Precisa ser nesse formato!!
```

Padrão nome_part_2: **"part2"**

***
