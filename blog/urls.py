from django.urls import path
from .views import post_list_published, post_create, post_detail, post_update, post_delete, like,post_list_all, post_list_draft

app_name = "blog"
urlpatterns = [

    path("",post_list_all, name="list_all"),
    path("published",post_list_published, name="list_published"),
    path("draft",post_list_draft, name="list_draft"),
    path("create/",post_create, name="create"),
    path("<str:slug>/",post_detail, name="detail"),
    path("<str:slug>/update/",post_update, name="update"),
    path("<str:slug>/delete/",post_delete, name="delete"),
    path("<str:slug>/like/",like, name="like"),
]