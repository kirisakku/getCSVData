import pyperclip

text = pyperclip.paste();

resultCSVList = []

# 行ごとのデータに区切る
textlist = text.split("\n")

for i in range(len(textlist)):
    dataText = textlist[i].replace(",", "").replace(", "," ").replace("，", " ")
    # スペースで区切りリストを作る
    datalist = dataText.split("	")
    # 不要なデータの削除
    del datalist[2]
    del datalist[3:5]
    # カンマでくっつける
    csv = ",".join(datalist)
    # 結果を格納
    resultCSVList.append(csv)

# 結果を連結
result = '\n'.join(resultCSVList)

# 結果を出力
print(result)
