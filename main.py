import codecs
import json
import scene_cal
import time_cal
import info
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
        # jieba.set_dictionary('data/dict.txt.big')
        cut_word = scene_cal.cuttest(text)
        temp_scene, temp_scene_num = scene_cal.split_scene(cut_word, text)
        scene, scene_num = scene_cal.check_whether_merge(temp_scene, temp_scene_num)
        scene_list.append(scene_num)
        # for i in range(scene_num):
        #     print(scene[i], '\n')
        all_characters = []
        scene_sum = []

        scene_idx = 1
        for i in range(scene_num):
            s = info.Scene(scene[i])
            scene_character = s.get_character()
            scene_location = s.get_location()
            scene_content = s.get_content()
            scene_time = time_cal.extract_time(scene[i])

            scene_dict = {
                "scene": scene_idx,
                "location": scene_location,
                "time": scene_time,
                "character": scene_character,
                "contents": scene_content
            }
            all_characters += scene_character
            scene_sum.append(scene_dict)

            scene_idx += 1

        all_characters = list(set(all_characters))

        story_dict = {
            "title": f.replace('.txt', ''),
            "scenes": scene_num,
            "all_characters": all_characters,
            "scene": scene_sum
        }

        json_str = json.dumps(story_dict, indent=4, ensure_ascii=False)
        with open('output_v3/' + f.replace('.txt', '') + '_output.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json_str)

    print('The scene number of each articles:', scene_list)
