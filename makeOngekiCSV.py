import pyperclip

text = pyperclip.paste();

resultCSVList = []

# 行ごとのデータに区切る
textlist = text.split("\n")

for i in range(len(textlist)):
    dataText = textlist[i].replace(",", "").replace(", "," ").replace("，", " ")
    # スペースで区切りリストを作る
    datalist = dataText.split("	")
    # 先頭に難易度種類追加
    if "MAS" in datalist[0]:
        datalist.insert(0, 'MASTER')
    elif "EXP" in datalist[0]:
        datalist.insert(0, 'EXPERT')
    # 不要なデータの削除
    del datalist[1]
    del datalist[7:9]
    del datalist[3:6]
    # カンマでくっつける
    csv = ",".join(datalist)
    # 結果を格納
    resultCSVList.append(csv)

# 結果を連結
result = '\n'.join(resultCSVList)

# 結果を出力
print(result)
