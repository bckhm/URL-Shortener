from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("shorten/<str:inurl>", views.check_url, name="check_url"),
    path("<str:shortened_url>", views.redirect_to_og, name="redirect_to_og")
]