#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 03/Jul/2014
# File: transcript.py
# Des: use pysrt module process the subtile from the movie
# and generate the text transcript for me, to help me
# learning english.
#
# Produced By CSRGXTU
import nltk
import pysrt
import sys


# ldSrtFile
# load srt file
#
# @param path to srt file
# @return list of pysrt obj or false on error
def ldSrtFile(path):
  # check out the param

  subs = pysrt.open(path)
  if len(subs) == 0:
    return false
  else:
    return subs


# getPlainTxt
# get plain text from the subtitles list
#
# @param subs list of pysrt
# @return texts list
def getPlainTxt(subs):
  # check out the param

  texts = []
  for item in subs:
    # remove html
    tmp = nltk.clean_html(item.text)
    # remove \n \r
    tmp = tmp.replace('\n', ' ')
    tmp = tmp.replace('\r', ' ')
    tmp = tmp.replace('\n\r', ' ')
    # strip non ascci for english
    tmp = _strip_non_ascci(tmp)
    texts.append(tmp)
    
  return texts

# _strip_non_ascci
# strip out the non ascci chars
#
# @param string to strip
# @return stripped string
def _strip_non_ascci(string):
  # check out the param

  stripped = (c for c in string if 0 <= ord(c) <= 127)
  return ''.join(stripped)


# save2File
# save subs to file
#
# @param subs list
# @param path
def save2File(subs, path):
  # check the param

  with open(path, "w") as FH:
    for item in subs:
      FH.write("%s\n" % item)


# main
# main method that glue everything up
def main():
  if len(sys.argv) != 3:
    print "Usage: transcript.py movie.srt trascript.txt\n"
    sys.exit(1)

  subs = ldSrtFile(sys.argv[1])
  texts = getPlainTxt(subs)
  save2File(texts, sys.argv[2])


if __name__ == "__main__":
  main()
