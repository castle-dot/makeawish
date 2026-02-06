from django.urls import path
from .views import WishDeleteView, WishDetailView, WishListView, WishCreateView, WishUpdateView, mark_granted, toggle_like_simple
from wishes import views 

app_name = 'wishes'

urlpatterns = [
    path('', WishListView.as_view(), name='list'),
    path('create/', WishCreateView.as_view(), name='create'),
    path('<int:pk>/', WishDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', WishUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', WishDeleteView.as_view(), name='delete'),
    path('<int:pk>/grant/', views.mark_granted, name='mark_granted'),
    path('<int:pk>/like/', views.toggle_like_simple, name='like'),
]
