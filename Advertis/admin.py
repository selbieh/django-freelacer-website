from django.contrib import admin
from . models import adver_m


def change_to_p(modeladmin, request, queryset):
        queryset.update(status='approved')
change_to_p.short_description = "approve selected advertises to be published"



class adver_m_Admin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['-date']
    exclude=None
    actions = [change_to_p]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.is_superuser:
            return actions
        else:
            return []


    def get_exclude(self,request,obj=None):
        if request.user.is_superuser:
            return ['user']
        else:
           return ['user','status']

    def get_queryset(self, request):
        qs = super(adver_m_Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
         return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
admin.site.register(adver_m,adver_m_Admin)

# Register your models here.
