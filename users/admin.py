from django.contrib import admin
from users.models import Review, RequestsNew

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'mentor', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('student__username', 'mentor__username', 'text')


@admin.register(RequestsNew)
class RequestsNewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student', 'mentor', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'student__username', 'mentor__username')
