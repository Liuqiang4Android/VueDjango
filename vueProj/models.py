from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

#只有两个字段，书名book_name和添加时间add_time。如果没有指定主键的话django会自动新增一个自增id作为主键