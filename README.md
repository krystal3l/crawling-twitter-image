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
