from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView

# from ..models import Tag
from ..serializers.tag_serializers import TagSerializers
from ..models.tag import Tag


class TagApi(APIView):

    @staticmethod
    def get(request):
        tag = Tag.objects.get(pk=request.query_params.get('pk'))
        serializer = TagSerializers(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request):
        tag = Tag.objects.get(pk=request.data.get('pk'))
        # tag = Tag.objects.get(pk=request.query_params.get('pk'))
        serializer = TagSerializers(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        tag = Tag.objects.get(pk=request.query_params.get('pk'))
        tag.delete()
        return Response(data={'Message': 'deleted successful'}, status=status.HTTP_200_OK)


class TagListApi(APIView):

    @staticmethod
    def get(request):
        tags = Tag.objects.all()
        serializer = TagSerializers(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = TagSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









