from rest_framework import serializers
from .models import Spot
from .models import Client, ClientUpdateStatus, NewsUpdateStatus


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

class NewsUpdateStatusSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = NewsUpdateStatus
        fields = ('api_id', 'status', 'update_count', 'update_datetime')

    def get_status(self,obj):
        return obj.get_status_display()

class ClientBarChartSerializer(serializers.Serializer):

    audit_code = serializers.CharField()
    count_section1 = serializers.IntegerField()
    count_section2 = serializers.IntegerField()
    count_section3 = serializers.IntegerField()
    count_section4 = serializers.IntegerField()
    count_section5 = serializers.IntegerField()
    count_section6 = serializers.IntegerField()

class ClientAverageAgeChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('average_age', 'income', 'audit_code')

class ClientServiceYearsChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('service_years', 'income', 'audit_code')

class ClientOrdinaryIncomeChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('ordinary_income', 'sales', 'audit_code')

class ClientNetIncomeChartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('net_income', 'sales', 'audit_code')


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