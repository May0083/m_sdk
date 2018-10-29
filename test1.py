from mtgsdk import Card
import json
import os
import pickle

def main():
    #やりたいこと
    #all_cardの情報の一部をpatchに登録する。

    sdk_data_path = os.path.dirname(__file__)+"\\sdk_data.bin"

    with open(sdk_data_path, 'rb') as base_file:
        cards  = pickle.load(base_file)


    one_path = os.path.dirname(__file__)+"\\one.bin"
    card_json = open(one_path, 'r',encoding="utf-8")
    card_j= json.load(card_json)
    card_json.close()


    #最初に改善したい部分　test2.pyで試行錯誤中
    for x in card_j:
        id = 0
        for c in cards:
            if card_j[x]["name"] == c.name:
                id = c.multiverse_id

        card_j[x]["multiverseid"] = id

        

    #パッチ適応データを保存-----------------------------------------------------------------------------------
    output_path = os.path.dirname(__file__) + "\\output.json"
    fw = open(output_path,'w',encoding='utf-8')
    json.dump(card_j,fw,indent=4,ensure_ascii=False)
    fw.close()


if __name__=='__main__':
    main()