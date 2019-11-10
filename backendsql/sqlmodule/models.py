from django.db import models

# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=256)
    category_id = models.IntegerField(blank=True, null=True)
    promotion = models.CharField(max_length=256, blank=True, null=True)
    keyword = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=45, blank=True, null=True)
    tags = models.CharField(max_length=256, blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    base_sale = models.IntegerField(blank=True, null=True)
    base_click = models.IntegerField(blank=True, null=True)
    base_share = models.IntegerField(blank=True, null=True)
    product_code = models.CharField(max_length=128, blank=True, null=True)
    starttime = models.DateField(blank=True, null=True)
    validity_period = models.IntegerField(blank=True, null=True)
    inventory = models.IntegerField(blank=True, null=True)
    inventory_warn = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=256, blank=True, null=True)
    sku_ids = models.CharField(max_length=512, blank=True, null=True)
    photo = models.CharField(max_length=256, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    media = models.CharField(max_length=256, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsAlbum(models.Model):
    name = models.CharField(max_length=128)
    sort = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_album'


class GoodsBrand(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)
    is_recommend = models.SmallIntegerField(blank=True, null=True)
    photo = models.CharField(max_length=256, blank=True, null=True)
    brand_photo = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_brand'


class GoodsCategory(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    name_simple = models.CharField(max_length=128, blank=True, null=True)
    goods_type = models.IntegerField(blank=True, null=True)
    is_show = models.SmallIntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=256, blank=True, null=True)
    keyword = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_category'


class GoodsPic(models.Model):
    album_id = models.IntegerField()
    path = models.CharField(max_length=512, blank=True, null=True)
    size = models.CharField(max_length=45, blank=True, null=True)
    width = models.CharField(max_length=45, blank=True, null=True)
    height = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_pic'


class GoodsSku(models.Model):
    goods_id = models.IntegerField()
    name = models.CharField(max_length=128)
    attr_values_items = models.CharField(max_length=256, blank=True, null=True)
    market_price = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    promote_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    stock = models.IntegerField()
    photo = models.CharField(max_length=256, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=256, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_sku'


class GoodsSpec(models.Model):
    name = models.CharField(max_length=45)
    sort = models.IntegerField(blank=True, null=True)
    is_used = models.SmallIntegerField(blank=True, null=True)
    values = models.CharField(max_length=128)
    desc = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_spec'


class GoodsSupplier(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    contact = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    desc = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_supplier'


class GoodsTag(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=256, blank=True, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_tag'


class GoodsType(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    is_used = models.SmallIntegerField(blank=True, null=True)
    attrs = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_type'
