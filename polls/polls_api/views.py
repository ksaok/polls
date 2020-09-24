from .models import poll, question
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import poll_serializer, question_serializer
from datetime import datetime


class polls_view_set(viewsets.ModelViewSet):
    queryset = poll.objects.filter(
        start_date__lte=datetime.now(),
        end_date__gte=datetime.now()
    )
    serializer_class = poll_serializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class questions_view_set(viewsets.ModelViewSet):
    queryset = question.objects.all()
    serializer_class = question_serializer
    permission_classes = [IsAuthenticatedOrReadOnly]
