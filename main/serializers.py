from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import *


class BolimSerializer(ModelSerializer):
    class Meta:
        model = Bolim
        fields = ['id', 'nom']


class MahsulotSerializer(ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'


class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'

    def validate(self, data):
        mijoz = data.get('qarz')

        if mijoz.qarz > 500000:
            raise ValidationError("Mahsulot olib ketishingiz mumkin emas")
        return data



class SotuvSerializer(ModelSerializer):
    class Meta:
        model = Sotuv
        fields = '__all__'


class SotuvchiSerializer(ModelSerializer):
    class Meta:
        model = Sotuvchi
        fields = '__all__'
