# -*- coding:utf-8 -*-
import json, config, emoji
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
url = "https://api.twitter.com/1.1/search/tweets.json"

faces = ["😠", "😩", "😱", "😆", "😢", "😯"] #怒り、嫌悪、恐怖、喜び、悲しみ、驚き
efiles = ["ikari.txt", "keno.txt", "kyofu.txt", "yorokobi.txt", "kanashimi.txt", "odoroki.txt"]

for face, efile in zip(faces, efiles):   #6感情一括取得
    with open(efile, 'w') as f:  #前回の6感情ファイル空処理
            f.write('')

    print("ツイート取得開始"+ efile)
    print('----------------------------------------------------')

    for time in range(8, 24):
        begin_time = '2020-1-6_' + str(time) + ':00:00_JST'   #＊＊＊日付変更＊＊＊
        end_time = '2020-1-6_' + str(time) + ':59:59_JST'
        params = {'q' : face, 'count' : 100, 'lang' : 'ja', 'exclude' : 'retweets', 'since' : begin_time, 'until' : end_time}
        req = twitter.get(url, params = params)
        count = 0

        if req.status_code == 200:
            search_timeline = json.loads(req.text)
            with open(efile, "a", encoding="utf_8") as f:   #出力ファイル 
                for tweet in search_timeline['statuses']:
                    f.write(tweet['text']+"\n")
                    count += 1
            print(begin_time, end_time, count)
        else:
            print("ERROR: %d" % req.status_code)
    print('----------------------------------------------------')
    print("ツイート取得終了" + efile)