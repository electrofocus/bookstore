from django.urls import path
from store import views

urlpatterns = [
    path('book/list/', views.BookListView.as_view()),
    path('author/list/', views.AuthorListView.as_view()),
    path('order/create/', views.OrderCreateView.as_view()),
]
