from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORY_LIST_CHOICE = [
    (1, '남자'),
    (2, '여자'),
    (3, '동물'),
    (4, '만화'),
    (5, '게임'),
]

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_like = models.ManyToManyField(User, related_name='user_like')
    user_count = models.ManyToManyField(User, related_name='user_count')

class Category(models.Model):
    category = models.CharField(choices=CATEGORY_LIST_CHOICE, max_length=2)
    level = models.IntegerField()
    board_relation = models.ManyToManyField(Board, related_name='category')

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


