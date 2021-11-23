from django.apps import AppConfig
from django.db.models.signals import (
    post_save,
    pre_save,
)
from .signals import (
    create_category_slug,
)
class BlogConfig(AppConfig):
    name = 'apps.blog'

    def ready(self):
        Category = self.get_model('Category')
        post_save.connect(create_category_slug, sender=Category)