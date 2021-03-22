from django.contrib import admin
from testModel.models import Test, Contact, Tag


# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])