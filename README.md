# crawling-twitter-image
crawl twitter image and post photos on django webpage

## Install
1. pycharm에서 프로젝트 생성


2. termial에 django 설치
~~~
$ pip install django
~~~


3. 장고 프로젝트 생성
~~~
$ django-admin startproject 만들이름 .
~~~


4. 데이터베이스 초기화 및 관리자 계정 생성
~~~
$ python manage.py migrate
$ python manage.py createsuperuser
~~~


5. 서버 실행
~~~
$ python manage.py runserver
~~~

***
* crawl_twitter_data.py 파일에서 원하는 트위터 계정과 해시태그를 넣어 이미지를 크롤링하고, 
트위터 정보(이미지url, 계정id 등)를 DB에 저장한다.

* django MTV 패턴을 이용하여 크롤링한 이미지가 웹페이지에 나오도록 한다.
