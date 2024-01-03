from django.urls import path
from .views import JobListView, JobDetailView, ClientListView, ClientDetailView

 
urlpatterns = [ 
   path('jobs/', JobListView.as_view(), name='job-list-create'),
   path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-retrieve-update-delete'), 
   path('client/', ClientListView.as_view(), name='job-list-create'),
   path('client/<int:pk>/', ClientDetailView.as_view(), name='job-retrieve-update-delete'),
   #path('jobs/<int:pk>/documents/', DocumentCreateView.as_view(), name='job-retrieve-update-delete'),
]
