from django.shortcuts import get_object_or_404
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required

from drf_spectacular.utils import extend_schema


@extend_schema(request=BookSerializer,responses=BookSerializer)
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])

def book(request):
    all_book =Book.objects.all().order_by("-id")
    if request.method=="GET":
        book_serializer = BookSerializer(all_book,many=True)
        return Response(book_serializer.data,status=status.HTTP_200_OK)

    elif request.method=="POST":
        create_book_serializer=BookSerializer(data=request.data)
        if create_book_serializer.is_valid():
            create_book_serializer.save()
            return Response(create_book_serializer.data,status=status.HTTP_201_CREATED) 
        return Response(create_book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=BookSerializer,responses=BookSerializer)
@api_view(["PUT","PATCH"])
@permission_classes([IsAuthenticated])
def update_book(request,reference_id):
    try:
        get_book=Book.objects.get(id=reference_id)
    except Book.DoesNotExist:
        return Response(
            {"detail":f"{get_book} Does not exist"},status=status.HTTP_400_BAD_REQUEST
        )

    if request.method=="PUT":
        update_book_serializer=BookSerializer(get_book,data=request.data)
        if update_book_serializer.is_valid():
            update_book_serializer.save()
            return Response(update_book_serializer.data,status=status.HTTP_202_ACCEPTED)

    if request.method=="PATCH":
        patch_book_serializer=BookSerializer(get_book,data=request.data,partial=True)
        if patch_book_serializer.is_valid():
            patch_book_serializer.save()
            return Response(patch_book_serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(patch_book_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=BookSerializer,responses=BookSerializer)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_book(request,id):
    get_book =get_object_or_404(Book,id=id)
    get_book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)