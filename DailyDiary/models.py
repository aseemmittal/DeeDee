from django.db import models
from django.contrib.auth.models import User

#class UserGroup(models.Model):

class Stars(models.Model):
    star_caster = models.ForeignKey(User)
    stars       = models.IntegerField()

class Posts(models.Model):
    post_text    = models.CharField(1000)
    post_caster  = models.ForeignKey(User)
    post_date    = models.DateTimeField()
    post_stars   = models.ForeignKey(Stars)
    post_privacy = models.IntegerField()

class Comments(models.Model):
    comment_text    = models.CharField(max_length=1000)
    comment_post    = models.ForeignKey(Posts)
    comment_date    = models.DateTimeField()
    comment_caster  = models.ForeignKey(User)
    comment_stars   = models.ForeignKey(Stars)
    comment_privacy = models.IntegerField()
