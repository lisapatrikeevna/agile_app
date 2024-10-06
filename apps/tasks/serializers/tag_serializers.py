from rest_framework import serializers

from apps.tasks.models.tag import Tag


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'












