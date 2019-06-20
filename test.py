import codecs
import json
import jieba
from os import listdir
from os.path import isfile, isdir, join


if __name__ == '__main__':

    mypath = '格林童話故事'
    files = listdir(mypath)
    jieba.set_dictionary('data/dict.txt.big')
    scene_list = []
    for f in files:
        print(f)
        fullpath = join(mypath, f)
        text = codecs.open(fullpath, 'r', 'utf-8').read()
        text = text.replace('「', '“').replace('」', '”')
        print(text)
        w = codecs.open(fullpath, 'w', 'utf-8')
        w.write(text)