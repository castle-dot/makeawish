from django.urls import path
from . import views
app_name = 'comments'

urlpatterns = [
    path('add/<int:wish_id>/', views.add_comment, name='add'),
]