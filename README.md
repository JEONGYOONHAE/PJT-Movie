# Final_pjt_관통 프로젝트

### i. 팀원 정보 및 업무 분담 내역

**1. 팀원 정보**

* 이동민
* 정윤해



**2. 업무 분담 내역**

* 이동민
  * vue의 기본기능 구현 + movie 외 css

* 정윤해
  * django api + movie 관련 css





### ii. 목표 서비스 구현 및 실제 구현 정도

**1. 서비스 구현 목표**

* 영화 목록 + 세부 영화 정보
* 영화 추천 알고리즘
* 영화 평점 매기기
* 영화 검색
* 게시판
* 댓글
* 프로필
* 로그인
* 로그아웃
* 회원가입
* 페이지네이션
* 평점 별로 만들기

\+ 꾸미기 .. 



**2. 실제 구현 정도**

* 영화 목록 + 세부 영화 정보
* 영화 추천 알고리즘
* 영화 평점 매기기
* 영화 검색
* 게시판
* 댓글
* 프로필
* 로그인
* 로그아웃
* 회원가입



### iii. 데이터베이스 모델링 (ERD)

**1. ERD**

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Movie(models.Model):
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre, related_name='movie_ids')
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=200)
    overview = models.CharField(max_length=400)
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    video = models.BooleanField(default=False)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review_id')
```






### iv. 필수 기능에 대한 설명

**1. 필수 기능**

* 로그인
  * 로그인 필수!
* 회원가입
* 로그아웃
* 영화 데이터
* 게시글 받아오기 
* 프로필
* 영화 좋아요



**2. 실제 구현 정도**

* 로그인

  * 로그인 필수!

* 회원가입

* 로그인 회원가입 동일 화면에서 애니매이션 적용

* 로그아웃

* 영화 데이터

* 게시글 받아오기

* 게시글 좋아요

* 영화 평점 매기기

* 댓글 기능

* 댓글 한 화면에서 update 기능

* 영화 title 검색 기능

* 영화 평점 순 정렬

* 영화 좋아요

* 프로필 

  



### v. 기타 (느낀 점)

**1. 느낀점**

* 이동민
  * 동기와 비동기를 잘 생각해서 코드를 구성해야 함
  * vuex를 사용하면 데이터의 흐름을 vuex에 몰아 넣는게 좋아보임
  * comment를 쓰는것 처럼 평점을 구성하는데 생각보다 어려움
  * 오타 조심
  * css 구성하기가 어려움..
  * vue style에서도 변수를 불러오는것 이외에도 let으로 위치를 정의해서 사용 가능
  * bootstrap vue 를 사용하면 만들기는 편하지만 커스텀하기 어려움
  * Array, Object 구별
  * Array function의 사용 익숙해짐
  * lodash가 생각보다 속도가 느린듯
  * 부모 컴포넌트와 자식 컴포넌트를 잡거나 화면을 구성하는데 어려움을 겪음
  * 디자인이 어려움
* 정윤해
  * 
