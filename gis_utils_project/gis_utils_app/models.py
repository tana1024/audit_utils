from django.db import models
from django.utils import timezone


class ClientUpdateStatus(models.Model):
    # 監査法人コード
    audit_code = models.CharField(primary_key=True, max_length=2)
    # 更新ステータス 0:未更新、1:更新開始、2:更新完了、9:異常終了
    status = models.CharField(max_length=1, blank=False, default='0')
    # 更新件数
    update_count = models.IntegerField(null=True)
    # 更新日時
    update_datetime = models.DateTimeField(default=timezone.now)


class Client(models.Model):
    # 証券コード
    s_code = models.CharField(primary_key=True, max_length=4)
    # クライアント名
    name = models.CharField(max_length=50, blank=True)
    # 住所
    street_address = models.CharField(max_length=100, blank=True)
    # 経度
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)
    # 緯度
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)
    # 監査法人コード
    audit_code = models.CharField(max_length=2, blank=True)

    class Meta:
        ordering = ('s_code',)


class Spot(models.Model):
    # 名前
    name = models.CharField(max_length=50)
    # カテゴリー
    category = models.CharField(max_length=5, blank=True)
    # ジャンル
    genre = models.CharField(max_length=50, blank=True)
    # 都道府県
    address_prefecture = models.CharField(max_length=10, blank=True)
    # 市区町村
    address_city = models.CharField(max_length=10, blank=True)
    # 丁目番地等
    address_street = models.CharField(max_length=100, blank=True)
    # 緯度
    latitude = models.CharField(max_length=50, blank=True)
    # 経度
    longitude = models.CharField(max_length=50, blank=True)
    # 作成日
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
