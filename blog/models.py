from django.conf import settings
from django.db import models
from django.utils import timezone


# Model을 정의하게 되면 해당 모델을
# `python manage.py makemigrations {appname}` 을 통하여 migration 할 수 있다(데이터베이스로 등록을 하기 위해)
# `python manage.py migrate {appname}`을 하게 되면 데이터베이스에 해당 모델의 테이블을 migration함

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
