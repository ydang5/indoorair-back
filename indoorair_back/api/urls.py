from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/version', views.GetVersion.as_view(),name='get_version'),
    path('api/login',views.LoginAPI.as_view(),name='login_api'),
    path('api/register', views.RegisterAPI.as_view()),
    path('api/logout',views.AccountLogoutAPI.as_view()),
    path('api/dashboard',views.DashboardAPI.as_view()),
    path('api/instruments', views.InstrumentListAPIView.as_view()),
    path('api/instrument/<int:id>', views.InstrumentRetrieveUpdateAPI.as_view()),
    path('report/api/1', views.download_csv_report_01_temperature_sensor_api,name ='download_csv_report_01_api'),
    path('api/sensor/<int:id>', views.SensorRetrieveAPI.as_view()),
    path('api/profile', views.get_profile_retrieve_api, name='profile_retrieve_api'),
    path('api/profile/update', views.post_profile_update_api, name='profile_update_api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
