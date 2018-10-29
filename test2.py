from mtgsdk import Card
import pickle
import os


def main():
    path = os.path.dirname(__file__)+"\\sdk_data.bin"

    with open(path, 'rb') as base_file:
        cards  = pickle.load(base_file)

    #cardsの中のnameが"Thalia, Guardian of Thraben"のカードを抽出したい。　合計3枚ある。
    # 最終目的は3枚目のid 270445のみの取得

    #全くスマートじゃない方法
    multiverseid = 0
    for c in cards:
        if c.name == "Thalia, Guardian of Thraben":
            multiverseid = c.multiverse_id
    print(multiverseid) #とりあえず3枚目のID取れる。


    #できると思ったけどできなかった方法
    filter_result = filter(lambda x:x["name"]=="Thalia, Guardian of Thraben",cards)
    print(list(filter_result))

if __name__=='__main__':
    main()