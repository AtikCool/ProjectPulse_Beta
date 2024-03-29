from django.urls import path
from .views import *
app_name = 'accounts'
urlpatterns = [
path('login/', signin_view, name='signin'),
 path('logout/', logout, name='logout' ),
]