from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json, os



app = FastAPI(title="SpellChecker")


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

def match_word(word:str, word_map:dict):
    letter=word[0]
    if letter not in word_map:
        return False
    elif letter in word_map and len(word)==1:
        return word_map[letter]["is_word"]
    elif len(word)>1 and letter in word_map:
        return match_word(word[1:], word_map[letter])
    
def find_word_from_dict(word_map:dict,word_pref:str=""):
    valid_word_list=[]
    key_count=len(list(word_map.keys()))
    if key_count>1:
        for key in word_map.keys():
            if key !="is_word":
                print
                valid_word_list= valid_word_list+ find_word_from_dict(word_map[key], word_pref+key)
            else:
                if word_map[key] and word_pref:
                    valid_word_list.append(word_pref)
    elif word_map["is_word"] and word_pref:
            valid_word_list.append(word_pref) 

    return valid_word_list

def get_word_sugestion(word:str, word_tree:dict,suggesion_list:list=[], word_prefix:str=""):
    letter=word[0]
    if letter not in word_tree:
        return suggesion_list
    elif letter in word_tree and len(word)==1:
        if len(list(word_tree[letter].keys()))>1:
            suggesion_list=suggesion_list+find_word_from_dict(word_tree[letter], word_prefix+letter)
        elif word_tree[letter]["is_word"]:
            suggesion_list.append(word_prefix+letter)
    elif letter in word_tree and len(word)>1:
        return get_word_sugestion(word[1:], word_tree[letter], suggesion_list,word_prefix+letter)
    return suggesion_list

@app.get('/suggest/{word_prefix}')
def word_suggestions(word_prefix:str)->dict:
    word_prefix=word_prefix.strip().lower()
    if not word_prefix:
        return {"error":"Invalid word_prefix !"}
    suggestion_list=list(set(get_word_sugestion(word_prefix, word_tree)))
    suggestion_list.sort()
    
    return {"given_pref": word_prefix,"suggestions_count":len(suggestion_list), "suggestions":suggestion_list}

@app.get('/{word}')
def check_word_presence(word:str)->dict:
    is_found=False
    word=word.strip().lower()
    is_found=match_word(word,word_tree)
    return {"searched_word":word,"is_found":is_found}


@app.post('/insert/{word}')
def insert_new_word(word:str)->dict:
    global word_tree
    
    word=word.strip().lower()
    word_tree = put_letter_in_dict(word,word_tree)         

    with open("./output/word_tree.json",'w') as wf:
        wf.write(json.dumps(word_tree, indent=2))
    return {"word":word, "is_inserted":True}
