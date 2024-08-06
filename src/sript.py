import json , os
word_tree={ }
with open("./output/word_tree.json","w+" if not os.path.exists("./output/word_tree.json") else "r") as rf:
    json_data=rf.read()
    word_tree=json.loads(json_data if json_data else "{}")

def put_letter_in_dict(word,dict):
    if word and word[0] not in dict:
        dict[word[0]]={"is_word":True} if len(word)==1 else {"is_word":False}
    elif word and word[0] in dict and len(word)==1:
        dict[word[0]]["is_word"]=True
    if len(word)>1:
        dict[word[0]]=put_letter_in_dict(word[1:], dict[word[0]])
    return dict


def insert_word(word:str):
    global word_tree
    word=word.strip().lower()
    word_tree = put_letter_in_dict(word,word_tree)         

with open("./input/wordlist.txt","r") as inprd:
    wordlist=inprd.read().split("\n")
    for word in wordlist:
        print("inserting::", word)
        insert_word(word=word)




with open("./output/word_tree.json",'w') as wf:
    wf.write(json.dumps(word_tree, indent=2))
print("word_tree",word_tree)



