from django.urls import path
from store import views

urlpatterns = [
    path('book/list/', views.BookListView.as_view()),
    path('book/create/', views.BookCreateView.as_view()),
    path('book/<int:pk>/', views.BookDetailUpdateDeleteView.as_view()),
    path('author/list/', views.AuthorListView.as_view()),
    path('author/create/', views.AuthorCreateView.as_view()),
    path('order/create/', views.OrderCreateView.as_view()),
    path('order/list/', views.OrderListView.as_view()),
]
