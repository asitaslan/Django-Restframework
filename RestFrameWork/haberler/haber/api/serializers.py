from django.db.models import fields
from rest_framework import serializers
from haber import models
from haber.models import Makale, Gazeteci

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince


class MakaleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()

    class Meta:
        model = Makale
        fields = '__all__'
        read_only_fields = ['id','yaratilma_tarihi','guncelleme_tarihi']

    def get_time_since_pub(self,object):
        now = datetime.now()
        pub_date = object.yayinlanma_tarihi
        if object.aktif == True:
            time_delta = timesince(pub_date,now)
            return time_delta
        else:
            return 'Aktif degil!'
    
    def validate_yayinlanma_tarihi(self,tarihdegeri):
        today = date.today()
        if tarihdegeri > today:
            raise serializers.ValidationError('Yayinlanma tarihi ileri bir tarih olamaz!')
        return tarihdegeri

class GazeteciSerializer(serializers.ModelSerializer):
    makaleler = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name= 'makale-detay',
    )

    class Meta:
        model = Gazeteci
        fields ='__all__'













### standart serializers
class MakaleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayinlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Makale.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayımlanma_tarihi = validated_data.get('yayımlanma_tarihi', instance.yayımlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance
         