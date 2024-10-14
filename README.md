# 第２章　はじめてのROS2（Humble版）
## 概要
ROS2とPythonで作って学ぶAIロボット入門（出村・萩原・升谷・タン著，講談社）第２章のサンプルプログラムと補足情報などを掲載しています．

## ディレクトリ構成
- **[airobot_interfaces](airobot_interfaces)**: 「AI Robot Book」のためのインタフェース定義 （プログラムリスト2.12, 2.15,2.16）(升谷 保博) 
- **[bringme_action](bringme_action)**: airobot_interfacesを使ったアクション通信のサンプルパッケージ （プログラムリスト2.20, 2.21, 2.22）
- **[bringme_service](bringme_service)**: airobot_interfacesを使ったサービス通信のサンプルパッケージ （プログラムリスト2.14, 2.15, 2.16） 
- **[happy](happy)**: はじめてのROS2パッケージ （プログラムリスト2.4, 2.5, 2.6, 2.7, 2.8）
- **[happy_action](happy_action)**: action用のサンプルパッケージ 
- **[happy_action_interfaces](happy_action_interfaces)**: happy_action用のインタフェース定義 
- **[happy_interfaces](happy_interfaces)**: happy用のインタフェース定義 
- **[happy_pub_sub](happy_pub_sub)**: topic用のサンプルパッケージ（プログラムリスト2.13） 
- **[happy_service](happy_service)**: service用のサンプルパッケージ 
- **[happy_topic](happy_topic)**: topic用のサンプルパッケージ（プログラムリスト2.9, 2.10, 2.11, 2.12）
- **[hello](hello)**: ros2 pkg createコマンドで自動生成されたパッケージ（プログラムリスト2.1, 2.2, 2.3）
- **[turtlesim_launch](turtlesim_launch)**: タートルシム用のローンチファイル 

## サンプルプログラム一覧
- プログラムリスト2.1 [package.xml](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/hello/package.xml)
- プログラムリスト2.2 [setup.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/hello/setup.py)
- プログラムリスト2.3 [hello_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/hello/hello/hello_node.py)
- プログラムリスト2.4 [happy_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy/happy/happy_node.py)
- プログラムリスト2.5 [happy_node2.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy/happy/happy_node2.py)
- プログラムリスト2.6 [setup.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy/setup.py)
- プログラムリスト2.7 [happy_node3.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy/happy/happy_node3.py)
- プログラムリスト2.8 [setup.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy/setup.py)
- プログラムリスト2.9 [happy_publisher_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy_topic/happy_topic/happy_publisher_node.py)
- プログラムリスト2.10 [happy_subscriber_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy_topic/happy_topic/happy_subscriber_node.py)
- プログラムリスト2.11 [package.xml](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy_topic/package.xml)
- プログラムリスト2.12 [setup.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/happy_topic/setup.py)
- プログラムリスト2.13 [happy_pub_sub_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/tree/master/happy_pub_sub/happy_pub_sub)
- プログラムリスト2.14 [StringCommand.srv](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/airobot_interfaces/srv/StringCommand.srv)
- プログラムリスト2.15 [bringme_service_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/bringme_service/bringme_service/bringme_service_node.py)
- プログラムリスト2.16 [bringme_client_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/bringme_service/bringme_service/bringme_client_node.py)
- プログラムリスト2.17 [CMakeLists.txt](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/airobot_interfaces/CMakeLists.txt)
- プログラムリスト2.18 [package.xml](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/airobot_interfaces/package.xml)
- プログラムリスト2.19 [setup.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/bringme_service/setup.py)
- プログラムリスト2.20 [StringCommand.srv](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/airobot_interfaces/srv/StringCommand.action)
- プログラムリスト2.21 [bringme_action_server_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/bringme_action/bringme_action/bringme_action_server_node.py)
- プログラムリスト2.22 [bringme_action_client_node.py](https://github.com/AI-Robot-Book-Humble/chapter2/blob/master/bringme_action/bringme_action/bringme_action_client_node.py)

## 実演動画一覧 (後で変更する） 
- [チャレンジ2.4 (p.50)] (https://youtu.be/Vmu8w7EW-7U)  
- [チャレンジ2.5 (p.53)] (https://youtu.be/hsBdCBVgmQY)  
- [チャレンジ2.6 (p.53)] (https://youtu.be/p6whfw_g6TU)  
- [チャレンジ2.7 (p.56)] (https://youtu.be/sV9rLgRLK1Q)  
- [チャレンジ2.8 (p.59)] (https://youtu.be/Y4eyENWhwH0)  


## インストール
Chapter2の全パッケージを以下のコマンドでインストールします．
- ROSのワークスペースを`~/airobot_ws`とする．
  ```
  cd ~/airobot_ws/src
  ```

- Chapter2のリポジトリを入手
  ```
  git clone https://github.com/AI-Robot-Book-Humble/chapter2
  ```
  
- パッケージのビルド   
  ```
  cd ~/airobot_ws  
  colcon build
  ```



## バグ情報
- 今のところありません。
