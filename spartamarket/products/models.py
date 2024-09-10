from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='products/image/',null=True,blank=True) # 이미지필드 , 추가설정


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE,null=True,blank=True) #null=True (데이터 없어도 db저장가능)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)