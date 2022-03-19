from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    # <path:inurl> to match all possible strings, including forward /
    path('shorten/<path:inurl>/', views.check_url, name="check_url"),
    path("<str:shortened_url>", views.redirect_to_og, name="redirect_to_og")
]