from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView

from url_app.models import Bookmark


class IndexView(View):

    def get(self, request):
        return HttpResponse("Welcome to the Index!")


class CreateUserView(CreateView):

    model = User
    form_class = UserCreationForm
    success_url = "/"


class CreateBookmarkView(CreateView):

    model = Bookmark
    fields = ["bookmark"]
    success_url = "/"


class BookmarkView(ListView):
    model = Bookmark
