from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status, viewsets


# Create your views here.
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self,request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data

        data = {
            "status":f"Returned {len(books)} Books",
            "data":serializer_data,
        }
        return Response(data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    def get(self,request,pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer_data = BookSerializer(book).data
            data = {
                "status":f"Succesfully retrieved {book}",
                "data":serializer_data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response(
                {
                    "status":f"False",
                    "message":"Book not found"},status=status.HTTP_404_NOT_FOUND
            )


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookUpdateApiView(APIView):
    def put(self,request,pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookDeleteApiView(APIView):
    def delete(self,request,pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(
            {
                "status":f"True",
                "message":f"{book} deleted successfully"
            },status=status.HTTP_204_NO_CONTENT)

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):
    def post(self,request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data ={
                "status":f"Returned Book",
                "book":serializer.data,
            }
        return Response(data)

class BookCreateListApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer