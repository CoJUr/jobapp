from django.urls import path
from app import views  # rather than   from app.views import hello, show_details


urlpatterns = [
    path('', views.job_list, name='jobs_home'),
    path('job/<int:id>', views.show_details, name='jobs_detail'),
    # path('job/<str:id>', views.show_details)
]

# path converters  slug   uuid    str     int
# slug matches any slug string, and contains only letters numbers underscores and hyphens   "my-first-blog"
# universally unique identifier  e.g:  c5ecbde1-cbf4-11e5-a759
