from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, ListView, RedirectView
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
        hash = Hashids(salt='Arsenal')
        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        bookmark.hash_id = hash.encode(id(bookmark.URL))
        return super(CreateBookmarkView, self).form_valid(form)


class UpdateBookmarkView(UpdateView):

    model = Bookmark
    fields = ["URL", "title", "description"]
    template_name = 'url_app/bookmark_update_form.html'
    success_url = "/accounts/b"

    def form_valid(self, form):

        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        return super(UpdateBookmarkView, self).form_valid(form)


class DeleteBookmarkView(DeleteView):

    model = Bookmark
    template_name = 'url_app/bookmark_confirm_delete.html'
    success_url = "/accounts/b"


class BookmarkView(ListView):

     def get_queryset(self):
         return Bookmark.objects.filter(user=self.request.user)

     class Meta:
         ordering = ["-title"]


class AllBookmarksView(ListView):

    template_name = 'url_app/bookmark_all_list.html'

    def get_queryset(self):
        return Bookmark.objects.all()


class ShortenedRedirect(RedirectView):

    def get(self, request, *args, **kwargs):
        hash_id = self.kwargs.get('hash_id', None)
        link = Bookmark.objects.get(hash_id=hash_id)
        self.url = link.URL
        return super(ShortenedRedirect, self).get(request, args, **kwargs)


@login_required
def profile_view(request):
    profile_data = {
        "data": list(Bookmark.objects.filter(user=request.user))
    }
    return render(request, "profile.html", profile_data)

