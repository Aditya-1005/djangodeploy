from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('hello/',views.hello,name='hello'),
    # path('district/',views.district,name='district')
]