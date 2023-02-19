# Tweepyライブラリをインポート
import os
import sys
import tweepy


def setting_api():
    # Twitter APIキーとアクセストークン（Bearer Token）
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    # TweepyのAPIオブジェクトを作成
    
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except:
        print("Error: twitter api is not loaded")
        sys.exit()
        
    return api

    


def get_fav(api, name, count=40):
    # いいねしたツイートのデータ（最新20件）を取得
    favorites = api.get_favorites(user_id="daiki_prv", count=count)

    twi_list = []
    # それぞれのツイートについてIDやテキストや日時などを表示
    for tweet in favorites:
        #print(tweet.user.name)
        twi_obj = {}
        twi_obj["text"] = tweet.text
        twi_obj["id"] = str(tweet.id)
        twi_obj["created_at"] = str(tweet.created_at)
        twi_obj["tweet_url"] = "https://twitter.com/" + tweet.user.screen_name + "/status/" + str(tweet.id)
        if 'media' not in tweet.entities:
            l = [twi_obj, []]

        else:
            urls = []
            # for media in tweet.entities['media']:
            #     urls.append(media['media_url_https'])
                
            for media in tweet.extended_entities['media']:
                urls.append(media['media_url_https'])
            l = [twi_obj, urls]
        twi_list.append(l)
    return twi_list
