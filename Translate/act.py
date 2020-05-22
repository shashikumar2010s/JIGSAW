import pickle

with open('translated_comment_validation.pkl', 'rb') as f:
   mynewlist = pickle.load(f)

print(len(mynewlist))
print(mynewlist[6381])