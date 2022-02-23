from django.urls import path

from labs import views

urlpatterns = [
    path('labs/<pk>', views.LabDetailView.as_view(), name='lab-detail'),
    path('groups/<pk>', views.GroupDetailView.as_view(), name='group-detail'),
    path('labs/', views.LabListView.as_view(), name='lab-list'),
    path('', views.root_view, name='root-redirect'),
]
