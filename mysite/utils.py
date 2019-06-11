from django.contrib.contenttypes.models import ContentType
from blog.models import ReadNum,LikeNum

def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # 存在记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            # 不存在对应的记录
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        # 计数加1
        readnum.read_num += 1
        readnum.save()
    return key

def like_statistics_once_like(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_like" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        if LikeNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # 存在记录
            likenum = LikeNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            # 不存在对应的记录
            likenum = LikeNum(content_type=ct, object_id=obj.pk)
        # 计数加1
        likenum.like_num += 1
        likenum.save()
    return key