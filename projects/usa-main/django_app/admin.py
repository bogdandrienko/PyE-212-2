from django.contrib import admin
from django_app import models
# Register your models here.


admin.site.site_header = 'Панель 1'
admin.site.index_title = 'Панель 2'
admin.site.site_title = 'Панель 3'


class youtube_video_categoryModelAdmin(admin.ModelAdmin):
    """IcecreamCategoryModel"""

    list_display = (
        'title', 
    )

    list_display_links = (
         
    )


    list_filter = (
         
    )

    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'title',                               
                )
            }
        ),
    )

class youtube_videoModelAdmin(admin.ModelAdmin):
    """youtubevideo"""

    list_display = (
        'title',
        'description',
    )
    filter_horizontal = ('category_id',) # только для полей флрмата many to many fields

    list_display_links = (
        'title',     
    )

    list_editable = (        
        'description',       
    )
    list_filter = (
        'title',
        'description',       
    )
    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'title',
                   'description',   
                   'category_id',
                   'url_from_youtube',               
                )
            }
        ),
    )
    search_fields = [
        'title',
        'description',          
    ]




admin.site.register(models.youtube_video_category, youtube_video_categoryModelAdmin)
admin.site.register(models.youtube_video, youtube_videoModelAdmin)

admin.site.register(models.MyPost)
admin.site.register(models.StoryCategory)
admin.site.register(models.Profile)