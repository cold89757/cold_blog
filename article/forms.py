# 引入表单类
from django import forms
# 引入文章模型
from .models import ArticlePost
from django.core.exceptions import ValidationError
# 写文章的表单类
class ArticlePostForm(forms.ModelForm):

    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body', 'tags', 'avatar')

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar', False)
        if avatar:
            if avatar.size > 1 * 1024 * 1024:  # 文件大小限制为1M
                raise ValidationError("图片大小不能超过1MB")

            # 验证文件类型
            if not avatar.content_type in ['image/jpeg', 'image/png']:
                raise ValidationError("只接受JPG或PNG格式的图片")

        return avatar
