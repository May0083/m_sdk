from mtgsdk import Card
import json
import os
import pickle

def main():
    #やりたいこと
    #all_cardの情報の一部をpatchに登録する。


    #skd_dataとoneの読み込み------------------------------------
    sdk_data_path = os.path.dirname(__file__)+"\\ktk.bin"

    with open(sdk_data_path, 'rb') as base_file:
        cards  = pickle.load(base_file)

    #必要な情報を配列に入れ直す
    #汚い…

    ex = []
    for c in cards:
        try:
            for f in c.foreign_names:
                if f["language"] == "Japanese":
                    jpid = f["multiverseid"]
        except:
            jpid = 0
        ex.append({"name":c.name,"multiverse_id":c.multiverse_id,"jp_multiverse_id":jpid})

    #one.json読み込み----------------------------------

    one_path = os.path.dirname(__file__)+"\\one.json"
    card_json = open(one_path, 'r',encoding="utf-8")
    card_j= json.load(card_json)
    card_json.close()


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

    #データを保存-----------------------------------------------------------------------------------
    output_path = os.path.dirname(__file__) + "\\output.json"
    fw = open(output_path,'w',encoding='utf-8')
    json.dump(card_j,fw,indent=4,ensure_ascii=False)
    fw.close()


if __name__=='__main__':
    main()