import moviepy.editor as mp
import torch
from pyannote.audio.features import RawAudio
from IPython.display import Audio
from pydub import AudioSegment
import csv

"""**Extracción del audio**"""

video = mp.VideoFileClip(r"data/videos/video.mp4")
video.audio.write_audiofile(r"data/audios/audio.wav")

FILE = {'audio': 'data/audios/audio.wav'}

"""**Opcion scd_ami (espectrograma)**"""

pipeline = torch.hub.load('pyannote/pyannote-audio', 'dia')
diarization = pipeline(FILE)

#diarization

!mkdir data/audios/speakers

with open('data.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Id", "Start", "End","path"])
  song = AudioSegment.from_wav("data/audios/audio.wav")
  combined = AudioSegment.empty()
  id = ''
  startG = ''
  endG = ''
  for turn, _, speaker in diarization.itertracks(yield_label=True):
    start = int(turn.start*1000)
    end = int(turn.end*1000)
    if id!=speaker :
      if len(id)>0:
        path = "data/audios/speakers/"+speaker+"-"+str(startG)+"-"+str(endG)+".wav"
        writer.writerow([speaker, startG, endG, path])
        combined.export(path, format="wav")
        combined = AudioSegment.empty()
      id=speaker
      startG = start
    endG=end
    aud = song[start:end]
    combined += aud
