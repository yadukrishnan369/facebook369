from django.contrib import path,include
from.import views

urlpatterns = [
    path('hai',views.testfun,name='hai'),
]