# coding=utf8
import codecs
import re

def cuttest(text):
    cut_word_loc = []
    cut_word = []

    with open('./data/scene_dic.txt', 'r') as f:
        for line in f:
            if line.strip('\n').strip('\t').strip('\r').strip(' ') in text:
                cut = line.strip('\n')
                cut_word.append(cut)

    # save index of the cut word
    for i in range(len(cut_word)):
        pos = text.index(cut_word[i])
        cut_word_loc.append(pos)

    # sorting by article
    if len(cut_word) == 0:
        pass
    else:
        cut_word_loc, cut_word = zip(*sorted(zip(cut_word_loc, cut_word)))
        # print(cut_word_loc)
        # print(cut_word)

    new_cut_word_loc = list(cut_word_loc)
    new_cut_word = list(cut_word)

    indx_cut = 1
    while indx_cut < len(new_cut_word_loc):
        if new_cut_word_loc[indx_cut] - new_cut_word_loc[indx_cut-1] <15:
            new_cut_word_loc.remove((new_cut_word_loc[indx_cut]))
            new_cut_word.remove(new_cut_word[indx_cut])
        indx_cut += 1
    # print(new_cut_word_loc)
    print(new_cut_word)

    return new_cut_word

def split_scene(cut_word, text):
    scene = []
    scene_num = len(cut_word)
    text = text.replace('\n', '').replace('\t', '').replace('\r', '').replace(' ','')
    print(text)

    if scene_num == 0:
        scene.append(text)
        scene_num = len(scene)
    else:
        # sce: 0,1,2,3...
        flag_start = -1
        for sce in range(scene_num-1):
            start = text.find(cut_word[sce])
            end = text.find(cut_word[sce+1])
            temp_text = text.replace('!', '。').replace('！', '。').replace('?', '。').replace('？', '。').replace('”', '。')
            flag_end = temp_text.rfind('。', start, end) # 倒著找回來最早碰到。者就為切點
            scene.append(text[flag_start+1:flag_end+1].replace('\n', '').replace('\t', '').replace(' ', ''))
            flag_start = flag_end

            if sce+2 == scene_num:
                scene.append(text[flag_start+1:].replace('\n', ''))

        # double check if scene is empty
        scene = list(filter(None, scene))
        scene_num = len(scene)

        # 確認切詞是否誤切在引號內
        i = 0
        while i < scene_num:
            temp_text = scene[i].replace('“', '「').replace('”', '」')
            up_quotes = temp_text.rfind('「')
            down_quotes = temp_text.rfind('」')
            if up_quotes > down_quotes:
                scene[i:i+2] = [''.join(scene[i:i+2])]
                scene_num -= 1
            else:
                i += 1


    return scene, scene_num

def check_whether_merge(scene, scene_num):

    if scene_num == 1:
        new_scene = scene
    elif scene_num == 2:
        new_scene = scene
    else:
        i = 0
        while i < scene_num:
            # print(len(scene[i].encode('utf-8')))
            # chinese word contains 3 characters
            if len(scene[i].encode('utf-8')) < 120:
                scene[i:i+2] = [''.join(scene[i:i+2])]
                scene_num -= 1
            i += 1
        new_scene = scene
        for j in range(len(new_scene)):
            new_scene[j] = new_scene[j].replace('\n', '')
    return new_scene, len(new_scene)

if __name__ == "__main__":
    # text = codecs.open('格林童話故事/約麗丹和約雷德爾.txt', 'r', 'utf-8').read()
    text = codecs.open('white.txt', 'r', 'utf-8').read()
    cut_word = cuttest(text)
    temp_scene, temp_scene_num = split_scene(cut_word, text)
    scene, scene_num = check_whether_merge(temp_scene, temp_scene_num)
    print()
    for i in range(scene_num):
        print(i, scene[i])