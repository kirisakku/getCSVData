# getCSVData
Wikiにある楽曲データのグリッドを選択すると、選択範囲のCSVを出力してくれるスクリプト。ランダム選曲アプリ用のCSVファイルが得られます。

### 使い方
* オンゲキは以下のサイトのある特定難易度のグリッドのデータを纏めて選択し、コピー実行後、makeOngekiCSV.pyを実行してください
 * https://ongeki.gamerch.com/%E3%82%AA%E3%83%B3%E3%82%B2%E3%82%AD%20%E6%A5%BD%E6%9B%B2%E4%B8%80%E8%A6%A7%EF%BC%88Lv%E9%A0%86%EF%BC%89%E9%AB%98%E9%9B%A3%E6%98%93%E5%BA%A6
* チュウニは以下のサイトにある特定難易度のグリッドのデータを纏めて選択し、コピー実行後、makeChuniCSV.pyを実行してください
 * https://chunithm.gamerch.com/CHUNITHM%20CRYSTAL%20%E6%A5%BD%E6%9B%B2%E4%B8%80%E8%A6%A7%EF%BC%88Lv%E9%A0%86%EF%BC%891
 
### 注意事項
データは過不足なく範囲選択してください。特にチュウニの方では"MAS"の選択が不十分で"AS"になっているとバグります。また、ヘッダー部分（難易度、ジャンル等）は含まれないように注意してください
