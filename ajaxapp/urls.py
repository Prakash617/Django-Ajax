from django.urls import path
from .views import *


app_name = "ajaxapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("allarticles/", AllArticlesView.as_view(), name="allArticle"),
    path("createarticle/", CreateArticlesView.as_view(), name="createArticle"),
]
