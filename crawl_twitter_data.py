import tweepy
from tweepy import OAuthHandler
import os
# import json
# import wget

# https://softwaree.tistory.com/74
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "config.settings")
import django

django.setup()

from app.models import ImageData


def crawl_twitter_data():
    # 크롤링한 데이터 저장하는 리스트
    searched_tweets = []

    # API 키 입력
    consumer_key = 'consumer key 입력'
    consumer_secret = 'consumer secret 입력'
    access_token = 'access token 입력'
    access_token_secret = 'access token secret 입력'

    # API 접근
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # 트위터 검색. from:사용자 ID #hashtag
    timeline = tweepy.Cursor(api.search,
                             q="from:WM_ONOFF #WYATT",
                             tweet_mode='extended').items()

    searched_tweets.extend(timeline)
    extract_data(searched_tweets)


def extract_data(tweet_data):
    # tweet에서 원하는 값만 추출한 리스트
    image_result = []
    # ImageData 모델에 저장된 media_id 데이터 가져오기(중복 저장을 막기위해 사용)
    stored_data = ImageData.objects.values('media_id')

    for tweet in tweet_data:
        try:
            for count in range(0, len(tweet.extended_entities['media'])):
                if (len(tweet.extended_entities['media']) != 0):
                    q2 = stored_data.filter(media_id=tweet.extended_entities['media'][count]['id_str'])
                    if not q2:
                        media_url = tweet.extended_entities['media'][count]['media_url']
                        tweet_url = tweet.extended_entities['media'][count]['url']
                        media_id = tweet.extended_entities['media'][count]['id_str']
                        user_id = tweet.user.screen_name

                        item_obj = {
                            'media_id': media_id,
                            'user_id': user_id,
                            'tweetlink': tweet_url,
                            'tweetimage': media_url
                        }
                        image_result.append(item_obj)

                    else:
                        pass
                else:
                    pass
        except:
            print('0')

    # 오래전에 post된 트윗부터 DB에 추가하기 위해 reverse 사용.
    image_result.reverse()
    new_image_insert_into_db(image_result)

def new_image_insert_into_db(image_result_list):
    for item in image_result_list:
        print('new item added!!: ', item['tweetlink'])
        ImageData(media_id=item['media_id'],
                  user_id=item['user_id'],
                  tweetlink=item['tweetlink'],
                  tweetimage=item['tweetimage']).save()


if __name__ == '__main__':
    crawl_twitter_data()
