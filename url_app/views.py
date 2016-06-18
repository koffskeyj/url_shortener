from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from hashids import Hashids
from url_app.models import Bookmark

hashids = Hashids()

class IndexView(View):

    def get(self, request):
        return HttpResponse("Welcome to the Index!")


class CreateUserView(CreateView):

    model = User
    form_class = UserCreationForm
    success_url = "/"


class CreateBookmarkView(CreateView):

    model = Bookmark
    fields = ["URL", "title", "description"]
    success_url = "/create_bookmark"

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        return super(CreateBookmarkView, self).form_valid(form)


class UpdateBookmarkView(UpdateView):

    model = Bookmark
    fields = ["URL", "title", "description"]
    template_name = 'url_app/bookmark_update_form.html'
    success_url = "/accounts/profile/b"

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        return super(UpdateBookmarkView, self).form_valid(form)


class DeleteBookmarkView(DeleteView):

    model = Bookmark
    template_name = 'url_app/bookmark_confirm_delete.html'
    success_url = "/accounts/profile/b"


class BookmarkView(ListView):

     def get_queryset(self):
         return Bookmark.objects.filter(user=self.request.user)

     class Meta:
         ordering = ["-title"]


@login_required
def profile_view(request):
    profile_data = {
        "data": list(Bookmark.objects.filter(user=request.user))
    }
    return render(request, "profile.html", profile_data)

