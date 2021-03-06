# coding: utf-8

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Block(models.Model):
	name = models.CharField(u"版块名称", max_length=10)
	desc = models.CharField(u"版块描述", max_length=30)
	admin = models.ForeignKey(User, verbose_name=u"管理员")

	create_timestamp = models.DateTimeField(u"创建时间", auto_now_add=True)
	last_update_timestamp = models.DateTimeField(u"最后更新时间", auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta: # 表的元属性
		verbose_name_plural = u"版块"