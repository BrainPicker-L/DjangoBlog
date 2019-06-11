
from django import template
from django.contrib.contenttypes.models import ContentType
from blog.models import LikeNum


register = template.Library()

@register.simple_tag
def get_like_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    like_count, created = LikeNum.objects.get_or_create(content_type=content_type, object_id=obj.pk)
    return like_count.like_num