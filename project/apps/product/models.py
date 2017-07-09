from django.core.urlresolvers import reverse
from django.db import models

from ..user_profile.models import Profile


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail',
                       kwargs={
                           'slug': self.slug
                       })


class ProductComments(models.Model):
    user = models.ForeignKey(Profile, related_name='user_profile_comments')
    product = models.ForeignKey(Product, related_name='comments')
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return (self.text).encode('utf-8')

    def get_absolute_url(self):
        return reverse('products:product_detail',
                       kwargs={
                           'slug': self.product.slug
                       })


class ProductLikes(models.Model):
    user = models.ForeignKey(Profile, related_name='user_profile_likes')
    product = models.ForeignKey(Product, related_name='likes')
    text = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_absolute_url(self):
        return reverse('products:product_detail',
                       kwargs={
                           'slug': self.product.slug
                       })
