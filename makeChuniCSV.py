import pyperclip

text = pyperclip.paste();

resultCSVList = []

difficulty = ""
category = ""
prefix = ""
# 行ごとのデータに区切る
textlist = text.split("\n")
# 一番最後の行は余分な改行なので１つ手前までループを回す
for i in range(len(textlist) - 1):
    targetText = textlist[i]
    # 難易度
    if targetText == "MAS":
        difficulty = "MASTER"
    elif targetText == "EXP":
        difficulty = "EXPERT"
    # カテゴリー
    elif targetText == "ORI":
        category = "ORIGINAL"
    elif targetText == "nico":
        category = "niconico"
    elif targetText == "VAR":
        category = "VARIETY"
    elif targetText == "撃舞":
        category = "ゲキマイ"
    elif targetText == "東方":
        category = "東方Project"
    elif targetText == "P&A":
        category = "POPS&ANIME"
    elif targetText == "イロ":
        category = "イロドリミドリ"
    # それ以外の曲データ
    else:
        dataText = textlist[i].replace(",", "").replace(", "," ").replace("，", " ")
        # スペースで区切りリストを作る
        datalist = dataText.split("	");
        # 要素数が1だったら次のデータとつなげる
        if len(datalist) == 1:
            prefix += datalist[0]
            continue
        else:
            # データを生成
            datalist = [difficulty, category, prefix + datalist[0], datalist[2]]
            # prefixを初期化
            prefix = ""
            # カンマでくっつける
            csv = ",".join(datalist)
            # 結果を格納
            resultCSVList.append(csv)

# 結果を連結
result = '\n'.join(resultCSVList)

# 結果を出力
print(result)
