from datetime import datetime
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..models import Project
from ..serializers.project_serializer import AllProjectSerializer, CreateProjectSerializer


class ProjectApi(APIView):

    @staticmethod
    def get(date_from=None, date_to=None):
        if not date_from or not date_to:
            projects = Project.objects.all()
            serializer = AllProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        date_from = timezone.make_aware(datetime.strptime(date_from, '%Y-%m-%d'))
        date_to = timezone.make_aware(datetime.strptime(date_to, '%Y-%m-%d'))

        filtered_projects = Project.objects.filter(created_at__range=(date_from, date_to))
        serializer = AllProjectSerializer(filtered_projects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = CreateProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









