from django.urls import path

from . import views

app_name = "applications"
urlpatterns = [
    path("", views.index, name="home"),
    path("signup", views.signup, name="signup"),
    path("create_account", views.create_account, name="create_account"),
    path(
        "create_profile", views.get_profile_information, name="get_profile_information"
    ),
    path("_create_profile", views.create_profile, name="create_profile"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("applications", views.ApplicationsView.as_view(), name="applications"),
    path('applications/new', views.NewApplicationView.as_view(), name='new_application'),
    path('applications/create', views.create_new_application, name='create_new_application')
]