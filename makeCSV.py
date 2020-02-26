import pyperclip

text = pyperclip.paste();

resultCSVList = []

# 行ごとのデータに区切る
textlist = text.split("\n")
# 一番最後の行は余分な改行なので１つ手前までループを回す
for i in range(len(textlist) - 1):
    dataText = textlist[i].replace(",", "").replace(", "," ").replace("，", " ")
    # スペースで区切りリストを作る
    datalist = dataText.split("	");
    # 不要なデータの削除
    del datalist[4:6]
    del datalist[2]
    # カンマでくっつける
    csv = ",".join(datalist)
    # 結果を格納
    resultCSVList.append(csv)

# 結果を連結
result = '\n'.join(resultCSVList)

# 結果を出力
print(result)
