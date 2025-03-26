from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import *
from django.http import HttpRequest

class BolimListCreateAPIView(ListCreateAPIView):
    serializer_class = BolimSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bolim.objects.all().order_by('nom')


class MahsulotListCreateAPIView(ListCreateAPIView):
    serializer_class = MahsulotSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Mahsulot.objects.filter(bolim__user=self.request.user).order_by('nom')

    def perform_create(self, serializer):
        serializer.save(bolim=self.request.user.bolim, sotuvchi=self.request.user)


class MahsulotRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MahsulotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Mahsulot.objects.filter(bolim__user=self.request.user).order_by('nom')

    def perform_update(self, serializer):
        serializer.save(bolim=self.request.user.bolim, sotuvchi=self.request.user)


class MijozListCreateAPIView(ListCreateAPIView):
    serializer_class = MijozSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Mijoz.objects.filter(mahsulot__bolim__user=self.request.user).order_by('nom')

    def perform_create(self, serializer):
        serializer.save(sotuvchi=self.request.user)


class MijozRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MijozSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Mijoz.objects.filter(mahsulot__bolim__user=self.request.user).order_by('nom')

    def perform_update(self, serializer):
        serializer.save(sotuvchi=self.request.user)


class SotuvchiListCreateAPIView(ListCreateAPIView):
    queryset = Sotuvchi.objects.all()
    serializer_class = SotuvchiSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class SotuvchiRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sotuvchi.objects.all()
    serializer_class = SotuvchiSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class SotuvListCreateAPIView(ListCreateAPIView):
    serializer_class = SotuvSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sotuv.objects.filter(sotuvchi__bolim__user=self.request.user).order_by('nom')

    def perform_create(self, serializer):
        serializer.save(sotuvchi=self.request.user)


class SotuvRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SotuvSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sotuv.objects.filter(sotuvchi__bolim__user=self.request.user).order_by('nom')

    def perform_update(self, serializer):
        serializer.save(sotuvchi=self.request.user)
