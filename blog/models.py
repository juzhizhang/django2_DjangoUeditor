from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')

    content = UEditorField(width=600, height=300, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    class Meta:
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
