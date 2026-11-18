from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("katalog/", views.catalog, name="catalog"),
    path("vizkard/<slug:slug>/", views.card_detail, name="card_detail"),
    path("kirish/", views.login_page, name="login"),
    path("royxatdan-otish/", views.register_page, name="register"),
    path("biz-haqimizda/", views.about_page, name="about"),
    path("boglanish/", views.contact_page, name="contact"),
]