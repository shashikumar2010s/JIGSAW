from textblob import TextBlob
import copy
# from googletrans import Translator
import pandas as pd
import numpy as np
import time
import pickle

comments_val=pd.read_csv('validation.csv')


def translate(comment):
#     if hasattr(comment, 'decode'):
#         comment = comment.decode('utf-8')
    text = TextBlob(comment)
    try:
#         text = text.translate(from_lang='en', to=language)
        # if text.detect_language() != 'en':
        time.sleep(0.2)
  #         print("before translation")
        text = text.translate(to='en')
        time.sleep(0.2)
        # else:
        #   return str(text)
    except Exception as e:
        print(e, text)
        pass

    return str(text)


# sample = comments_test['content'].iloc[61500:61550]
# sampled_list = []
# for coms in sample:
#     if ((len(sampled_list) % 50) == 0):
#         print(f'  Translated {len(sampled_list)} comments ')
#     try:
# #         print(coms)
#         txt = translate(coms)
    
#         sampled_list.append(txt)
#     except Exception as e:
#         print(str(e), len(sampled_list))
#         continue

# with open('parrot.pkl', 'wb') as f:
#    pickle.dump(sampled_list, f)


validation_translated_list = []
for coms in comments_val['comment_text']:
    if ((len(validation_translated_list) % 500) == 0):
        print(f'  Translated {len(validation_translated_list)} comments ')
    try:
        txt = translate(coms)
        validation_translated_list.append(txt)
    except Exception as e:
        print(str(e), len(validation_translated_list))
        continue

with open('translated_comment_validation.pkl', 'wb') as f:
   pickle.dump(validation_translated_list, f)