from django.urls import path
from app import views  # rather than   from app.views import hello, show_details


urlpatterns = {
    path('', views.hello),
    path('job/1', views.show_details),
}
