from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import time
import calendar
import random
from django.conf import settings
import os


from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0



class LikeNum(models.Model):
    like_num = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class LikeNumExpandMethod():
    def get_like_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            likenum = LikeNum.objects.get(content_type=ct, object_id=self.pk)
            return likenum.like_num
        except exceptions.ObjectDoesNotExist:
            return 0


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name
class Blog(models.Model,ReadNumExpandMethod,LikeNumExpandMethod):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=None)
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING,default=None)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=False)
    last_updated_time = models.DateTimeField(auto_now=True)
    create_month = models.CharField(max_length=50,blank=False,default=calendar.month_name[int(time.localtime().tm_mon)])
    img_url = models.ImageField(upload_to='images',blank=True)  # upload_to指定图片上传的途径，如果不存在则自动创建
    def __str__(self):
        return "<Blog: %s>" % self.title
    def getImage(self):
        if self.img_url:
            return self.img_url.url
        else:
            return os.path.join("/media/images","project-"+str(random.randint(1,8))+".jpg")
    class Meta:
        ordering = ['-created_time']






