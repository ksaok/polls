from rest_framework import serializers
from .models import poll, question, choice

class poll_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = poll
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'questions']


class question_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = question
        fields = ['poll', 'id', 'text', 'type']

