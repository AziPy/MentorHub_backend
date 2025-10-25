from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, CartItem


# ---------------- User Admin ----------------
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'get_full_name', 'role', 'is_active', 'created_at')  # ← используй get_full_name вместо name
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('created_at', 'updated_at', 'last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'role', 'avatar', 'bio')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'role'),
        }),
    )

    ordering = ('email',)

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.email
    get_full_name.short_description = 'Name'



@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'quantity', 'total_price', 'added_at')  # status убрал
    search_fields = ('user__email', 'course__title')
    list_filter = ('added_at',)

    def total_price(self, obj):
        # предполагаем, что у курса есть поле price
        return obj.course.price * obj.quantity
    total_price.short_description = 'Total Price'
