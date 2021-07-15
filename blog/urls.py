from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 기본적으로 ''의 URL패턴을 post_list 함수로 참조
]