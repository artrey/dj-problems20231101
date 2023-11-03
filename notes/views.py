from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.permissions import IsAuthorOrReadOnly
from notes.serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['post'], detail=True, url_path='toggle-favourite')
    def toggle_favourite(self, request, *args, **kwargs):
        note = self.get_object()
        user = request.user
        if note.favourite_by.filter(id=user.id).exists():
            note.favourite_by.remove(user)
        else:
            note.favourite_by.add(user)
        serializer = self.get_serializer(note)
        return Response(serializer.data)
