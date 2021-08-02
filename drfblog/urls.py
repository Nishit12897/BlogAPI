from django.urls import path
from .api import *


urlpatterns = [
    path('api/create',BlogCreateApi.as_view()),
    path('api', BlogListApi.as_view()),
    path('api/<int:pk>', BlogUpdateApi.as_view()),
    # path('api/<int:pk>/delete', BlogDeleteApi.as_view()),

]