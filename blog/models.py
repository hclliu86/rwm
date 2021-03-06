from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(u"姓", max_length=250)
    last_name = models.CharField(u"名字", max_length=250)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = u"姓名"

    full_name = property(my_property)

    def __str__(self):
        return self.full_name
