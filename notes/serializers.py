from rest_framework import serializers

from notes.models import Note

from django.conf import settings


class NoteSerializer(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField(method_name='get_is_favourite')

    class Meta:
        model = Note
        fields = ['id', 'user', 'text', 'created_at', 'is_favourite']
        read_only_fields = ['user']

    def get_is_favourite(self, obj):
        if settings.MAX_COURSES > 5:
            ...
        user = self.context['request'].user
        if not user.is_authenticated:
            return False
        return obj.favourite_by.filter(id=user.id).exists()
