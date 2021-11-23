"""Core > admin.py"""
# DJANGO IMPORTS
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# PLUGIN IMPORTS
# PROJECT IMPORTS
from Core import models




@admin.register(models.User)
class UserAdmin(UserAdmin):
    ordering = ('-date_joined', )
    list_display = (
        'id', 'email', 'user_type', 'last_login', 'last_updated',
        'date_joined', 'is_staff', 'is_superuser', 'is_active'
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'email', 'password',
                )
            }
        ),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        (
            'Roles', {
                'fields': (
                    'user_type', 'is_staff', 'is_superuser', 'is_active'
                )
            }
        ),
        ('Dates', {'fields': ('last_login', 'last_updated', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'email', 'user_type', 'password1', 'password2'
            )
        }),
    )
    readonly_fields = ('last_login', 'last_updated', 'date_joined')
    search_fields = ('id', 'email')

    def get_inline_instances(self, request, obj=None):
        """hides inlines during 'add user' view"""
        return obj and super().get_inline_instances(request, obj) or []



@admin.register(models.StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'name', 'organization', 'designation', 'phone_no',
        'created_at', 'updated_at'
    ]


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'first_name', 'phone_no', 'created_at', 'updated_at'
    ]


admin.site.site_header = "BUBT নিউজ Admin"
admin.site.site_title = "দৈনিক BUBT নিউজ Admin Portal"
admin.site.index_title = "Welcome to দৈনিক BUBT নিউজ Portal"