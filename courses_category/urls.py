from django.db import router

from courses_category.views.category_views import CategoryViewSet

router.register(r'categories', CategoryViewSet)