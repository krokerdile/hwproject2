from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    
    subject11 = models.CharField(max_length=20, null=True)
    subject12 = models.CharField(max_length=20, null=True)
    subject13 = models.CharField(max_length=20, null=True)
    subject14 = models.CharField(max_length=20, null=True)
    subject15 = models.CharField(max_length=20, null=True)

    subject21 = models.CharField(max_length=20, null=True)
    subject22 = models.CharField(max_length=20, null=True)
    subject23 = models.CharField(max_length=20, null=True)
    subject24 = models.CharField(max_length=20, null=True)
    subject25 = models.CharField(max_length=20, null=True)

    subject31 = models.CharField(max_length=20, null=True)
    subject32 = models.CharField(max_length=20, null=True)
    subject33 = models.CharField(max_length=20, null=True)
    subject34 = models.CharField(max_length=20, null=True)
    subject35 = models.CharField(max_length=20, null=True)

    subject41 = models.CharField(max_length=20, null=True)
    subject42 = models.CharField(max_length=20, null=True)
    subject43 = models.CharField(max_length=20, null=True)
    subject44 = models.CharField(max_length=20, null=True)
    subject45 = models.CharField(max_length=20, null=True)

    subject51 = models.CharField(max_length=20, null=True)
    subject52 = models.CharField(max_length=20, null=True)
    subject53 = models.CharField(max_length=20, null=True)
    subject54 = models.CharField(max_length=20, null=True)
    subject55 = models.CharField(max_length=20, null=True)

    subject61 = models.CharField(max_length=20, null=True)
    subject62 = models.CharField(max_length=20, null=True)
    subject63 = models.CharField(max_length=20, null=True)
    subject64 = models.CharField(max_length=20, null=True)
    subject65 = models.CharField(max_length=20, null=True)

    subject71 = models.CharField(max_length=20, null=True)
    subject72 = models.CharField(max_length=20, null=True)
    subject73 = models.CharField(max_length=20, null=True)
    subject74 = models.CharField(max_length=20, null=True)
    subject75 = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name


class Blog(models.Model): # Blog 라는 이름의 객체 틀(Model) 생성
    title = models.CharField(max_length=200) # title 라는 최대 200 글자의 문자 데이터 저장
    pub_date = models.DateTimeField('date published') # pub_date 라는 날짜 시간 데이터 저장
    body = models.TextField()

    def __str__(self):
        return self.name