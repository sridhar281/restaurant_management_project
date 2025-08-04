from django.urls import path
from .views import *
from .views import homepage, HardcodedMenuView

urlpatterns = [
      path('items/', ItemView.as_view(), name='item-list'),
    path('', homepage, name='homepage'),
    path('menu-static/', HardcodedMenuView.as_view(), name='hardcoded-menu'),
]

