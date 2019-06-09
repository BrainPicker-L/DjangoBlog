from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import time
import calendar
import random
from django.conf import settings
import os
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=None)
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
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
