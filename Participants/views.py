from rest_framework import generics
from Participants.serializers import ParticipantsDetailSerializer, ParticipantsListSerializer
from Participants.models import Participants
from Participants.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class ParticipantsCreateView(generics.CreateAPIView):
    serializer_class = ParticipantsDetailSerializer


class ParticipantsListView(generics.ListAPIView):
    serializer_class = ParticipantsListSerializer
    queryset = Participants.objects.all()
    permission_classes = (IsAuthenticated, )


class ParticipantsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParticipantsDetailSerializer
    queryset = Participants.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )