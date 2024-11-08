from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (BookDetailApiView, BookUpdateApiView, BookCreateListApiView, BookUpdateDeleteApiView,
                    BookDeleteApiView, BookCreateApiView, BookListApiView, BookViewSet)

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('booklistcreate/', BookCreateListApiView.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    path('bookupdatedelete/<int:pk>/', BookUpdateDeleteApiView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    path('books/create/', BookCreateApiView.as_view()),
]

urlpatterns += router.urls