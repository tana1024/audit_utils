from django.db import models
from django.utils import timezone


class ClientUpdateStatus(models.Model):

    STATUS_CHOICES = (
        ('0', '未更新'),
        ('1', '更新開始'),
        ('2', '更新完了'),
        ('9', '異常終了')
    )

    # 監査法人コード
    audit_code = models.CharField(primary_key=True, max_length=2)
    # 更新ステータス 0:未更新、1:更新開始、2:更新完了、9:異常終了
    status = models.CharField(max_length=1, blank=False, default='0', choices=STATUS_CHOICES)
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
    # 従業員数
    employees = models.IntegerField(null=True, default=0)
    # 平均年齢
    average_age = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    # 平均勤続年数
    service_years = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    # 年収
    income = models.IntegerField(null=True, default=0)
    # 売上高
    sales = models.BigIntegerField(null=True, default=0)
    # 経常利益
    ordinary_income = models.BigIntegerField(null=True, default=0)
    # 当期純利益
    net_income = models.BigIntegerField(null=True, default=0)
    # 監査法人コード
    audit_code = models.CharField(max_length=2, blank=True)

    class Meta:
        ordering = ('s_code',)

class News(models.Model):
    # ニュースID
    news_id = models.AutoField(primary_key=True)
    # ソース元ID
    source_id = models.CharField(max_length=100, blank=True)
    # ソース元名称
    source_name = models.CharField(max_length=300, blank=True)
    # 著者
    author = models.CharField(max_length=100, blank=True)
    # タイトル
    title = models.CharField(max_length=500, blank=True)
    # タイトル(日本語訳)
    title_jp = models.CharField(max_length=500, blank=True)
    # 詳細
    description = models.CharField(max_length=1000, blank=True)
    # 詳細(日本語訳)
    description_jp = models.CharField(max_length=1000, blank=True)
    # 記事のURL
    url = models.CharField(max_length=300, blank=True)
    # イメージ画像のurl
    url_to_image = models.CharField(max_length=300, blank=True)
    # 出版日時
    published_at = models.DateTimeField(null=True)
    # コンテンツ
    content = models.CharField(max_length=1000, blank=True)

class NewsUpdateStatus(models.Model):

    STATUS_CHOICES = (
        ('0', '未更新'),
        ('1', '更新開始'),
        ('2', '更新完了'),
        ('9', '異常終了')
    )

    # api id
    api_id = models.CharField(primary_key=True, max_length=1)
    # 更新ステータス 0:未更新、1:更新開始、2:更新完了、9:異常終了
    status = models.CharField(max_length=1, blank=False, default='0', choices=STATUS_CHOICES)
    # 更新件数
    update_count = models.IntegerField(null=True)
    # 更新日時
    update_datetime = models.DateTimeField(default=timezone.now)

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
