from rest_framework import serializers
from .models import Spot
from .models import Client, ClientUpdateStatus


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('s_code', 'name', 'street_address', 'longitude', 'latitude', 'audit_code')


class ClientUpdateStatusSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = ClientUpdateStatus
        fields = ('audit_code', 'status', 'update_count', 'update_datetime')

    def get_status(self,obj):
        return obj.get_status_display()


class ClientEmployeeChartSerializer(serializers.Serializer):

    audit_code = serializers.CharField()
    count_1_100 = serializers.IntegerField()
    count_100_300 = serializers.IntegerField()
    count_300_1000 = serializers.IntegerField()
    count_1000_3000 = serializers.IntegerField()
    count_3000_10000 = serializers.IntegerField()
    count_10000_over = serializers.IntegerField()

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