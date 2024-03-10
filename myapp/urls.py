from django.urls import path
from . import views
from .views import HomePageView
from .views import AboutView
from .views import SurfingView
from .views import LocationView
from .views import WipeoutView
from .views import DangerView


urlpatterns = [
  path("", HomePageView.as_view(), name="home"),
  path("about/", AboutView.as_view(), name="about"),
  path('surfing/', SurfingView.as_view(), name='bigwavesurfing'),
  path('location/', LocationView.as_view(), name='location_view'),
  path('wipeout/', WipeoutView.as_view(), name= 'wipeout_view'),
  path('danger/', DangerView.as_view(), name='danger_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('function/', views.function_view, name='function_view'),
  
]
