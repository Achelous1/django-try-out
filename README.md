# Django를 연습해보자
> 2021년 7월부터 시작

## Django는 MTV
* Django의 아키텍쳐는 MTV(Model-Template-View)이다
* MVC와 비슷하지만 MTV에서는 View(view.py)가 Controller의 역할을 Template(templates/\*\*/*.html등)이 View의 역할을 한다
* 해당 MTV외에도 urls라는 레이어가 있는데, 이 부분이 URL요청을 처리하여 알맞은 view로 전달하는 부분이다 (urls.py)
* Django의 아키텍쳐에 관해서는 [Mozilla](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction#%EC%9A%94%EC%B2%AD%EC%9D%84_%EC%95%8C%EB%A7%9E%EC%9D%80_%EB%B7%B0%EB%A1%9C_%EC%A0%84%EB%8B%AC_urls.py) 에서 참조해서 자세하게 읽어보자
