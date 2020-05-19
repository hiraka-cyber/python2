from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
   path('index',views.index,name='index'),
   path('detail',views.detail,name='detail'),
   path('results',views.results,name="results"),
   path('good',views.good,name="good"),
   path('meet',views.meet,name="meet"),
   path('beef',views.beef,name="beef"),
   path('chicken',views.chicken,name="chicken"),
   path('fish',views.fish,name="fish"),
   path('home',views.home,name='home'),
   path('',views.all,name='all'),
]
