# -*- coding:utf-8 -*-

from django.db import models


class User(models.Model):
    '''
    仅用户模拟用户
    '''
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'ele_user'

    def __unicode__(self):
        return u'{id}-{name}'.format(id=self.id, name=self.name)


class WiningRecord(models.Model):
    '''
    记录实际使用的上证 & 深证指数 & 获奖号码，用于回溯
    '''

    sh_index = models.IntegerField()
    sz_index = models.IntegerField()
    wining_number = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    def save(self):
        '''
        只允许insert
        '''
        super(MarketIndex, self).save(force_insert=True)

    class Meta:
        db_table = 'wining_record'

    def __unicode__(self):
        return self.id


class NumberUser(models.Model):
    '''
    记录每个抽奖号码对应的用户
    '''
    number = models.IntegerField(unique=True, db_index=True)
    user = models.ForeignKey('User')

    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'number_user'

    def __unicde__(self):
        return self.number
