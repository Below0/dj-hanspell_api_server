import base64
from .models import Word


def save_dict_word(word_dict):
    print(word_dict)
    context = word_dict['original']
    for key in word_dict['words'].keys():
        if word_dict['words'][key] == 0:
            continue
        encoded_key = key.encode('utf-8')
        tmp = (base64.b85encode(encoded_key)).decode()
        try:
            word = Word.objects.get(word_id=tmp)
            word.count += 1
            word.save()
        except Word.DoesNotExist:
            word = Word(word_id=tmp, correct=word_dict['words'][key])
            word.save()
#
 # def split_dict_word(context, keys):
 #


