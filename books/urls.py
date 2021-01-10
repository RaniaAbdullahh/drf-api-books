from django.urls import path, include


from .views import BooksDetailsView,  BooksListView


urlpatterns = [
    path('', BooksListView.as_view(), name='books'),
    path('<int:pk>/', BooksDetailsView.as_view(), name='book_details'),
]