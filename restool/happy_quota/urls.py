from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:project_id>/', views.add_leads_here, name='add_leads_here'),
    # ex: /polls/5/results/
    path('<int:project_id>/results/', views.lead_added, name='lead_added'),
]
