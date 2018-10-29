from mtgsdk import Card
import json
import os
import pickle

def main():
    ex = read_bin()
    card_j = read_json()

    #名前で検索してid登録～～～----------------------------------

    for x in card_j:
        name = card_j[x]["name"]
        filter_result = filter(lambda x:x["name"] == name,ex)
        try:
            res = list(filter_result)[-1]
            card_j[x]["multiverseid"] = res["multiverse_id"]
            card_j[x]["jp_multiverseid"] = res["jp_multiverse_id"]
        except:
            pass

    save_data(card_j)

def read_bin():
    sdk_data_path = os.path.dirname(__file__)+"/ktk.bin"

    with open(sdk_data_path, 'rb') as base_file:
        cards  = pickle.load(base_file)

    ex = []
    for card in cards:
        for foreign_name in card.foreign_names:
            jpid = get_jpid(foreign_name)
            ex.append({"name":card.name,"multiverse_id":card.multiverse_id,"jp_multiverse_id":jpid})

    return ex

def read_json():
    one_path = os.path.dirname(__file__)+"/one.json"
    card_json = open(one_path, 'r',encoding="utf-8")
    card_j= json.load(card_json)
    card_json.close()
    return card_j

def save_data(card_j):
    output_path = os.path.dirname(__file__) + "/output.json"
    f = open(output_path,'w',encoding='utf-8')
    json.dump(card_j,f,indent=4,ensure_ascii=False)
    f.close()

def get_jpid(foreign_name):
# 日本語見つけたらmultiverseid返すよ関数
    if foreign_name["language"] == "Japanese":
        return foreign_name["multiverseid"]
    else:
        return 0

if __name__=='__main__':
    main()