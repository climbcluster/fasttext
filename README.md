# fasttextを用いた感情抽出
fasttextというテキスト分類を得意とするfacebookAI研究所が開発した自然言語ツールが日本語に対応しているので、
この機械学習ツールを使用し感情分類を行った。4感情では高い分類精度が示される例も確認した。  
なお、必要となる教師データの準備は以下のように作成した。  
その流れをざっくり説明する。  
また、フォルダ内のプログラムはデータ作成に使用したプログラムである。  
fasttextや環境構築は既出のため省略  

## 環境
・WSLやUbuntuでは確認済、私のMacではfasttextがうまくいかなかった。  
・Python3,MeCab(普通の)

## Twitterの絵文字を正解ラベル、テキストをデータとする
日本語の自然言語処理における教師データの完全なものは存在しないと思われる。(2020/3)  
そのため、教師データを以下のように作成した。  
1．Twitterの検索窓から作成したい感情に関連する絵文字を選択し、検索を行う(twitterAPIから)  
2．次に得られた検索データの絵文字を含んだテキストを切り取る  
3．取得したテキストを絵文字がラベル、テキスト本文がデータとなるように変形  
4．MeCabを用いて分かち書きにしfasttextで学習が行えるよう前処理を行う  
以上の流れで必要な数のテキスト数と種類が集めることを可能とした。  

整形したデータからfasttextで感情分類を行い性能を評価した。  
およそ4感情と6感情で30%~40%の結果であった。  
分類の割合も表示されるので考察が行いやすい。  

## 結果
結果と設定はscore.txtに記載されているような形になった。  
epoch数など増やすなど(過学習も考慮して)まだ改善の余地がありそうである。



