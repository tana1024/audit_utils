from rest_framework import serializers
from .models import Spot
from .models import ClientUpdateStatus


class ClientUpdateStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientUpdateStatus
        fields = ('audit_code', 'status', 'update_datetime')


class SpotListSerializer(serializers.ModelSerializer):
    # 名前
    name = serializers.CharField(max_length=50)
    # カテゴリー
    category = serializers.CharField(max_length=5, allow_blank=True)
    # 都道府県
    address_prefecture = serializers.CharField(max_length=10, allow_blank=True)

    class Meta:
        model = Spot
        fields = ('id', 'name', 'category', 'address_prefecture')


class SpotSerializer(serializers.ModelSerializer):
    # 名前
    name = serializers.CharField(max_length=50)
    # カテゴリー
    category = serializers.CharField(max_length=5, allow_blank=True)
    # ジャンル
    genre = serializers.CharField(max_length=50, allow_blank=True)
    # 都道府県
    address_prefecture = serializers.CharField(max_length=10, allow_blank=True)
    # 市区町村
    address_city = serializers.CharField(max_length=10, allow_blank=True)
    # 丁目番地等
    address_street = serializers.CharField(max_length=100, allow_blank=True)
    # 緯度
    latitude = serializers.CharField(max_length=50, allow_blank=True)
    # 経度
    longitude = serializers.CharField(max_length=50, allow_blank=True)

    class Meta:
        model = Spot
        fields = (
            'name', 'category', 'genre', 'address_prefecture', 'address_city', 'address_street', 'latitude',
            'longitude')