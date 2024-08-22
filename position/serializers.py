from django.contrib.auth.models import User
from rest_framework import serializers

from position.models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            "id",
            "title",
            "valid_date",
            "working_hours",
            "salary",
            "image",
            "category",
            "employer_name",
        ]

    read_only_fields = ('id')
