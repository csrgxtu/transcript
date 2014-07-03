transcript
==========

create plain text transcript from subtitles file

Goal:
transport the subtitles file to plain text file

i.e.

  1
  00:00:19,920 --> 00:00:24,198
  
  <i>For 74 years, the might
  
  of Soviet socialism was so great</i>

  ==>

  For 74 years, the might of Soviet socialism was so great

Requirements:

  pysrt, nltk packege
  
  install on ubuntu
  
  sudo pip install pysrt
  
  sudo apt-get install python-nltk
  

Run:

./transcript.py movie.srt movie.txt


welcome to <a href="http://csrgxtu.blog.com/">csrgxtu</a>
