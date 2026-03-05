from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.filter(is_deleted=False)
    serializer_class = TodoSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()