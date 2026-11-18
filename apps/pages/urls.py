from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("katalog/", views.catalog, name="catalog"),
    path("vizkard/<slug:slug>/", views.card_detail, name="card_detail"),
    path("kirish/", views.login_page, name="login"),
]