from django.urls import path
from . import views

urlpatterns = [
    # path('portfolio/',views.portfolio, name='portfolio'),
    # path('',views.home,name='home'),
    path('',views.portfolio, name='portfolio'),

]
