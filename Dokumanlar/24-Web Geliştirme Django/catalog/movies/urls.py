from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
]