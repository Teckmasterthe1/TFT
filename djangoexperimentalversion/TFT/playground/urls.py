from django.urls import path
from . import views

#URLConf
app_name = 'polls'
urlpatterns = [\
    path('main/', views.main),
    path('main/calculator/', views.calculator),
    path('main/calculator/basicmath/', views.basicmath),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]