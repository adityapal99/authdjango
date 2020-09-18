from django.urls import path, include

from . import views

from restauth import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.homePage),
    path("signup/", views.SignUpPage.as_view()),
    path("login/", views.LoginPage.as_view()),
    path("dashboard/", views.DashboardPage.as_view()),
    path("logout/", views.Logout)
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

