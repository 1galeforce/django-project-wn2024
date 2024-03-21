from django.urls import path
from . import views
from .views import HomePageView
from .views import AboutView
from .views import SurfingView
from .views import CreationView
from .views import LocationView
from .views import WipeoutView
from .views import DangerView
from .views import InventionListView, InventionDetailView

urlpatterns = [
  path("", HomePageView.as_view(), name="home"),
  path("about/", AboutView.as_view(), name="about"),
  path('surfing/', SurfingView.as_view(), name='bigwavesurfing'),
  path('creation/', CreationView.as_view(), name= 'creation_view'),
  path('location/', LocationView.as_view(), name='location_view'),
  path('wipeout/', WipeoutView.as_view(), name= 'wipeout_view'),
  path('danger/', DangerView.as_view(), name='danger_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  path('function/', views.function_view, name='function_view'),
  path('load/', views.load_default_data_view, name='load_default_data'),
  path('inventions/', views.InventionListView.as_view(), name='invention-list'),
  path('invention/<int:pk>/', views.InventionDetailView.as_view(), name='invention-view'),
  path('invention/create/', views.InventionCreateView.as_view(), name='create_invention'),
  path('invention/<int:pk>/update/', views.InventionUpdateView.as_view(), name='update_invention'),
  path('invention/<int:pk>/delete/', views.InventionDeleteView.as_view(), name='delete_invention'),

  
]
