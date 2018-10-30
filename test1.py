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
        #これをしたいがためにリストに作り直した
        #cards = Card.all()
        #filter_result = filter(lambda x:x["name"] == name,cards)
        #↑こんな感じに出来ればよかったのに・・・

        try:
            res = list(filter_result)[-1]
            card_j[x]["multiverseid"] = res["multiverseid"]
            card_j[x]["jp_multiverseid"] = res["jp_multiverseid"]
        except:
            pass

    save_data(card_j)

def read_bin():
    sdk_data_path = os.path.dirname(__file__)+"/ktk.bin"

    with open(sdk_data_path, 'rb') as base_file:
        cards  = pickle.load(base_file)

    ex = []
    for card in cards:
        jpid = get_jpid(card)
        jptext = get_jptext(card)
        ex.append({"name":card.name,"multiverseid":card.multiverse_id,"jp_multiverseid":jpid})

    print(ex)
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

def get_jpid(card):
# 日本語見つけたらmultiverseid返すよ関数
    jpid = 0
    try: #他のエキスパンションだとcard.foreign_namesが存在しない場合があり、エラーが生じる。
        for foreign_name in card.foreign_names:
            if foreign_name["language"] == "Japanese":#これがないとこの後に他の言語をチェックするとidが0に上書きされてしまう問題
                jpid = foreign_name["multiverseid"]
    except:
        pass
    
    return jpid


if __name__=='__main__':
    main()