#python3.7
from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
ydl_opts = {}
X=input("enter the url :")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
ydl.download([X])
