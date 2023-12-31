# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Products(models.Model):
    product_name = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)
    price = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)
    seller = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)
    inverntory_stock = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class PurchaseHistory(models.Model):
    product_name = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)
    price = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)
    user_id = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)
    order_date = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase history'


class Users(models.Model):
    user_type = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)
    user_id = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)
    password = models.TextField(db_collation='Latin1_General_CI_AI', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
