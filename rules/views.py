from rest_framework import generics, permissions
from .models import Rule
from .serializers import RuleSerializer


class RuleListCreateView(generics.ListCreateAPIView):
    serializer_class = RuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rule.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rule.objects.filter(owner=self.request.user)
