from django.contrib import admin
from blog.models import Article, Person
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)
    search_fields = ('title', 'content',)
    list_filter = ('title',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
