# coding=utf8
from Synonyms.synonyms import synonyms
from hanziconv import HanziConv
import random

def rewrite(text):
    seg = synonyms.seg(text) # select the POS in synonyms (using jieba)
    seg_word = seg[0]
    # seg_pos = seg[1]
    seg_index = seg[2]
    # print(seg_word)
    # print(seg_pos)
    replace_words = list()

    for i in range(len(seg_word)):
        word = synonyms.nearby(seg_word[i])[0]
        score = synonyms.nearby(seg_word[i])[1]
        # print(word)
        # print(score)
        if len(word) != 0 and min(score) > 0.5:
            replace_word = random.choice(word)
            replace_words.append(replace_word)
            new_text = text.replace(seg_word[i], replace_word, seg_index[i])
            text = new_text
        else:
            replace_word = ''
            replace_words.append(replace_word)

    new_text = text

    return new_text, seg_word, replace_words

if __name__ == "__main__":
    # text = codecs.open('格林童話故事/約麗丹和約雷德爾.txt', 'r', 'utf-8').read()
    text = '從前，有一隻胖胖的豬媽媽，她生了三隻小豬。最大的小豬：豬大哥很貪睡，很懶惰。一天到晚都在打瞌睡。第二個小豬：豬二哥很愛吃，他也很懶惰。幸好最小的小豬：豬小弟是個勤勞的好孩子。常常努力的工作。'
    print(text)
    text_rewrite, change_original_index = rewrite(text)
    print(text_rewrite)
    print(change_original_index)