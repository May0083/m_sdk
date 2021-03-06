from mtgsdk import Card
import json
import os
import pickle

def main():
  
    cards = Card.where(set="AVR").all()
    card_j = read_json()


    for x in card_j:
        name = card_j[x]["name"]
        card_j[x]["multiverseid"] = get_multiverseid(name,cards)
        card_j[x]["jp_multiverseid"] = get_multiverseid_jp(name,cards)

    save_data(card_j)

def get_multiverseid(name,cards):
    try:#たまに無いこともある
        id_list = []
        for card in cards:
            if card.name == name:
                if card.multiverse_id != None: id_list.append(card.multiverse_id) 
        id_list.sort()
        return id_list[0]
    except:
        return 0

def get_multiverseid_jp(name,cards):
    try:#無いことがよくある
        id_list = []
        for card in cards:
            if card.name == name:
                jpid = get_jpid(card)
                if jpid != 0: id_list.append(jpid)
        id_list.sort()
        return id_list[0]
    except:
        return 0

def get_jpid(card):
    # 日本語見つけたらmultiverseid返すよ関数
    jpid = 0
    try: #他のエキスパンションだとcard.foreign_namesが存在しない場合があり、エラーが生じる。
        for foreign_name in card.foreign_names:
            if foreign_name["language"] == "Japanese":#この後に他の言語をチェックするとidが0に上書きされてしまう問題
                jpid = foreign_name["multiverseid"]
    except:
        pass
    
    return jpid
    
def read_json():
    one_path = os.path.dirname(__file__)+"/little.json"
    card_json = open(one_path, 'r',encoding="utf-8")
    card_j= json.load(card_json)
    card_json.close()
    return card_j

def save_data(card_j):
    output_path = os.path.dirname(__file__) + "/output.json"
    f = open(output_path,'w',encoding='utf-8')
    json.dump(card_j,f,indent=4,ensure_ascii=False)
    f.close()



if __name__=='__main__':
    main()