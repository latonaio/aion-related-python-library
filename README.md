## aion-related-python-library  
aion-related-python-libraryはAIONのマイクロサービスで利用するpythonライブラリーです。  

## 動作環境
aion-related-python-libraryは、AIONのプラットフォーム上での動作を前提としています。  
使用する際は、事前に以下の動作環境を用意してください。  
 
・OS: Linux Ubuntu   
・CPU: ARM/AMD/Intel    
・Kubernetes  
・AIONのリソース  

## 概要  
aion-related-python-library内のaionディレクトリ以下にライブラリーが含まれています。
```
kanban：
    kanbanサーバーへの問い合わせ
    kanbanサーバーへの書き込み
    redisクライアントの生成
logger：
    k8sにログを吐き出せる
    k8s対応を行ったデバッグログのラッパー
microservice：
    内部で実装しているdecoratorを実装している。
    decoratorを呼び出したマイクロサービスをkanbanクライアント化する
mongo：
    mongoクライアントの生成
    mongoへの問い合わせ
    mongoへのデータ書き込み
mysql：
    mysqlクライアントの生成
    mysqlへの問い合わせ
    mysqlへのデータ書き込み
proto：
    自動生成されたgrpcのコードが入っている
    kanbanライブラリでのgrpcに使用
```

## 利用方法
このリポジトリをクローンし、カレントディレクトリにしてください。その後、以下の手順でコンテナにマウントし、ライブラリーをインストールしてください。
```
$ docker exec -it [コンテナ名] bash  #コンテナに入る
$ apt-get install python3-dev libmysqlclient-dev  #mysql_config: not foundエラーの対策
$ cd ~/path/to/aion-related-python-library 
$ pip install .
```
Dockerfileや、docker-compose.ymlに記載して使用する方法は、testディレクトリ配下のファイルを参照してください。


