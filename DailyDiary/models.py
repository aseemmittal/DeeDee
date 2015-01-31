from django.db import models
from django.contrib.auth.models import User
import datetime

#class UserGroup(models.Model):

class Star(models.Model):
    star_caster = models.ForeignKey(User)
    stars = models.IntegerField()

class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User)
    publushed_date = models.DateTimeField(default=datetime.datetime.now())
    is_published = models.IntegerField()
    saved_on = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_text = models.CharField(max_length=1000)
    comment_post = models.ForeignKey(Post)
    comment_date = models.DateTimeField()
    comment_caster = models.ForeignKey(User)
    comment_stars = models.ForeignKey(Star)
    comment_privacy = models.IntegerField()
