# bringme_action:  
## 概要
２章のサンプルプログラム  
airobot_interfacesを使ったアクション通信のサンプルパッケージ


## インストール
Chapter2のパッケージは全部まとめてインストール・ビルドをします．
- [第2章 インストール](https://github.com/AI-Robot-Book/chapter2)を参照してください．


## 実行  
- 端末を２つに分割する．
- 1番目の端末で次のコマンドを実行する．  
```
ros2 run bringme_action bringme_action_server_node  
```
- 2番目の端末で次のコマンドを実行する．
```
ros2 run bringme_action bringme_action_client_node
何をとってきますか：
```
と聞かれるので，取ってきて欲しい英単語を入力する．  
'apple', 'banana', 'candy'を入力すると **"はい，〇〇です．”** とゴールの結果が返る，  
それ以外は **"〇〇を見つけることができませんでした．”** とゴールの結果が返る．


## ヘルプ
- 今のところありません．
　
 
## 著者
出村 公成


## 履歴
- 2024-10-14: 初期版


## ライセンス
Copyright (c) 2024, Kosei Demura All rights reserved. This project is licensed under the Apache-2.0 license found in the LICENSE file in the root directory of this project.


## 参考文献
- 今のところありません．

