from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from forms import AddPostForm
# Create your views here.

class MainIndex(View):
    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MainIndex, self).dispatch(*args, **kwargs)

    def __init__(self):
        pass

    def get(self, request):
        form = AddPostForm()
        return render(request,'DailyDiary/add_post.html',{'form':form})


class SignUp:
    def __init__(self):
        pass

class SignIn:
    def __init__(self):
        pass

class HomePage:
    def __init__(self):
        pass

class UserArea:
    def __init__(self):
        pass

class NewPost:
    def __init__(self):
        pass

class ReadDiary:
    def __init__(self):
        pass

class ResetPassword:
    def __init__(self):
        pass

class RatePost:
    def __init__(self):
        pass

class RateComment:
    def __init__(self):
        pass

class DeletePost:
    def __init__(self):
        pass

class DeleteComment:
    def __init__(self):
        pass


def posted(request):
    return HttpResponse(request)