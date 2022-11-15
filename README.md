
# Table of Contents

1.  [これは何？](#org2794ed5)
2.  [使い方](#org263fedd)
3.  [注意](#orgb72458c)


<a id="org2794ed5"></a>

# これは何？

食べログの検索結果をcsvで出力するツールです。


<a id="org263fedd"></a>

# 使い方

食べログの任意の検索ページの１ページ目のURLを取得し、次のように実行します。

    $ python3 scraping.py --url="https://tabelog.com/tokyo/rstLst/?vs=1&sa=%E6%9D%B1%E4%BA%AC%EF%BC%88%E3%81%99%E3%81%B9%E3%81%A6%EF%BC%89&sk=&lid=top_navi1&vac_net=&svd=20221115&svt=1900&svps=2&hfc=1&sw="

結果はtabelog.csvに出力されます。


<a id="orgb72458c"></a>

# 注意

食べログの検索結果は６０ページまでしか表示されないので、適切に検索範囲を絞ってください。

