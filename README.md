
# Table of Contents

1.  [これは何？](#orgc1be04f)
2.  [使い方](#org5cd46c7)
3.  [注意](#orgee8065b)


<a id="orgc1be04f"></a>

# これは何？

食べログの検索結果をcsvで出力するツールです。


<a id="org5cd46c7"></a>

# 使い方

urlに食べログの任意の検索ページの１ページ目のURLを取得し、次のように実行します。

    $ python3 scraping.py --url="https://tabelog.com/tokyo/rstLst/?vs=1&sa=%E6%9D%B1%E4%BA%AC%EF%BC%88%E3%81%99%E3%81%B9%E3%81%A6%EF%BC%89&sk=&lid=top_navi1&vac_net=&svd=20221115&svt=1900&svps=2&hfc=1&sw="

結果はtabelog.csvに出力されます。


<a id="orgee8065b"></a>

# 注意

食べログの検索結果は６０ページまでしか表示されないので、適切に検索範囲を絞ってください。

