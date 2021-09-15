# 제 4회 KB국민은행 소프트웨어 경진대회
## Butterfly-Effect(나비효과) 팀


## 1. 팀 구성

본 경진대회에 참여하는 나비효과 팀의 팀원과 팀원의 역할은 다음과 같다. (가나다 순으로 나열)

-  김제현 (디자이너)
- [박현준](https://github.com/c2lv) (개발자)
- [이태검](https://github.com/LeeTaeGeom) (개발자)
- [이형석](https://github.com/lhs961021) (개발자, 팀장)

### 1.1. 참여 과제

주제: 환경을 바꾸는 소프트웨어

### 1.2 과제 주제

**<나비효과>**

**나** 를 통해

**비** 로소 지켜지는 환경

부제 : 나의 날개짓이 커다란 변화를 이끈다

## 2. 프로그래밍 언어

본 프로젝트는
[**Python**](https://www.python.org)을 메인 프로그래밍 언어로 사용하고, 
웹 프레임워크로 [**Django**](https://www.djangoproject.com)를 이용한다.

### 2.1. 외부 라이브러리의 사용

본 애플리케이션을 구현하는 과정에서 활용 가능한 외부 라이브러리는 제한없이 사용하는 것을 원칙으로 한다.

### 2.2. Requirements.txt

본 애플리케이션의 소스코드 내에서 활용한 모든 외부 라이브러리는 requirements.txt에 해당 라이브러리 리스트를 저장하여 팀원들에게 공유하여야 한다.
```
$ pip freeze > requirements.txt
```
requirements.txt에 저장된 외부 라이브러리를 다운로드 받는 명령어는 다음과 같다.
```
$ pip install -r requirements.txt
```

### 2.3. Python 가상환경
- [pipenv](https://github.com/pypa/pipenv) :  Python.org에서 공식적으로 권장하는 패키지 설치 툴 및 가상환경 구현용 프로그램

## 3. 서버 실행
```
$ python manage.py runserver 
```
## 4. 환경변수 파일

.gitignore

- Git 관련 환경변수 파일

requirements.txt

- 파이썬 라이브러리 종속성 파일
