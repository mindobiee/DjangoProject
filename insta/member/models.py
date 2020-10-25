from django.db import models

# Create your models here.

# 회원 DB와 게시글, 댓글 DB


class Member(models.Model):
    # id, password, 닉네임, 이메일, 전화번호, 설명
    # id, pw, nickname, email, phone_number, desc
    name = models.CharField(max_length=20)
    pw = models.CharField(max_length=20)

    # nickname = models.CharField(max_length=20)
    # email = models.CharField()
    # phone_number = models.CharField(max_length=13)
    # desc = models.TextField()

    class Meta:
        db_table= "members"

#
# class Post(models.Model):
#     # 닉네임, 텍스트, 이미지
#     nickname = models.CharField(max_length=20)
#     text = models.CharField(max_length=200)
#     image = models.fields #???
#     # 좋아요 수, 댓글 수
#     likes = models.IntegerField(default=0)
#     comments = models.IntegerField(default=0)
#     # 날짜
#     created = models.DateTimeField(auto_now_add=True)
#
#
# class Comments(models.Model):
#     nickname = models.CharField(max_length=20)
#     text = models.CharField(max_length=50)
#     likes = models.IntegerField(dafault=0)