東京メトロオープンデータサイト開発者サイト　操作ツール
==========
東京メトロオープンデータサイト開発者サイトのフォーラムが提供していない検索機能をサポートします。  

https://developer.tokyometroapp.jp/  

Windows7, Debianのpython2.7で動作を確認しています。  


依存ファイル  
-------------
下記のファイルに依存しているので、easy_installなり,pipでインストールしてください。  

peewee  
urllib2  
lxml  
cookielib  
ConfigParser  


Debianでlxmlをインストールするには、下記のファイルが必要になります。

    apt-get install libxml2-dev libxslt1-dev

参考:  
http://stackoverflow.com/questions/6504810/how-to-install-lxml-on-ubuntu  



操作方法
-----------------
1.application.ini.originをコピーしてappication.iniを作成する。  
下記を修正すること。  

    [user]
    email = 開発者フォーラムのEMAIL
    pass = パスワード


2.開発者サイトの情報をデータベースに格納します。

    python sync.py


3.指定のワードを含むトピックを検索をします。

    python search_term.py 列車

