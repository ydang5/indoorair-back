from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/version', views.GetVersion.as_view(),name='get_version'),
    path('api.login',views.LoginAPI.as_view(),name='login_api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
