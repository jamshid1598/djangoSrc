from django.db.models.signals import (
    pre_save,
    post_save,
)
from django.utils.text import slugify
from django.dispatch import receiver

# @receiver(post_save, sender=Category)
def create_category_slug(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.name)
        instance.save()
# post_save.conntect(create_category_slug, sender=Category)
