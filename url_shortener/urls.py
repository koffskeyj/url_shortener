"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from url_app.views import IndexView, CreateUserView, CreateBookmarkView, BookmarkView, UpdateBookmarkView, DeleteBookmarkView, AllBookmarksView, ShortenedRedirect
from django.contrib.auth.views import login, logout
from url_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login, name="index_view"),
    url(r'^logout/$', logout, {'next_page': '/'}, name="logout_view"),
    url(r'^create_user/$', CreateUserView.as_view(), name="create_user_view"),
    url(r'^create_bookmark/$', CreateBookmarkView.as_view(), name="create_bookmark_view"),
    url(r'^update_bookmark/(?P<pk>\d+)$', UpdateBookmarkView.as_view(), name="update_bookmark_view"),
    url(r'^delete_bookmark/(?P<pk>\d+)$', DeleteBookmarkView.as_view(), name="delete_bookmark_view"),
    url(r'^accounts/profile/$', views.profile_view, name="profile_view"),
    url(r'^accounts/b$', BookmarkView.as_view(), name="bookmark_view"),
    url(r'^bookmarks_by_users/$', AllBookmarksView.as_view(), name="all_bookmarks_view"),
    url(r'^(?P<hash_id>\w+)/$', ShortenedRedirect.as_view(), name="shortened_redirect")
]
