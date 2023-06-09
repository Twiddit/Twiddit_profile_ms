# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    email = models.TextField(unique=True, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    profile_photo = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'