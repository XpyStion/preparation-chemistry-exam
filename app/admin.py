from django.contrib import admin


class AdminModel(admin.ModelAdmin):
    class Media:
        css = {
            'all': '/static/styles/admin.css'
        }
