東京メトロオープンデータサイト開発者サイト　操作ツール
==========
東京メトロオープンデータサイト開発者サイトのフォーラムが提供していない検索機能をサポートします。  

https://developer.tokyometroapp.jp/  

依存ファイル  
-------------
下記のファイルに依存しているので、easy_installなり,pipでインストールしてください。
peewee  
urllib2  
lxml  
cookielib  
ConfigParser  


操作方法
-----------------
1.application.ini.originをコピーしてappication.iniを作成する。  
下記を修正すること。  

    [user]
    email = 開発者フォーラムのEMAIL
    pass = パスワード


2.開発者サイトの情報をデータベースに格納します。

    python sync.py


3.検索をします。

    python search_term.py 列車

