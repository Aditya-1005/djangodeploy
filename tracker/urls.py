from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    # path('state/',views.state,name='state'),
    # path('district/',views.district,name='district')
]