## Ejecución

Se deberá tener un árbol de directorio de la siguiente forma 

- data/videos/
- data/audios/
- data/audios/speakers/

El primero contendrá el video a ser trabajado, en la segunda carpeta se escribirá el audio extraido y e en la última, las voces de cada hablante con la estructura `{IdSpeaker}-{Time Start}-{Time End}.wav`

Posteriormente la instalación de dependencias `pip install` 

Dentro del código se encuentra la ruta del video sobre el cual se realizará la diarialización 

`video = mp.VideoFileClip(r"data/videos/video.mp4")`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/braymarco/Speaker-Diarization/blob/main/notebooks/Diariazation.ipynb)
