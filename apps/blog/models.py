from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()



# Create your models here.


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    
    created_at = models.DateField(_("created at"), auto_now_add=True)
    updated_at = models.DateField(_("updated at"), auto_now=True)
    class Meta:
        ordering=['category', 'created_at', 'updated_at']
        verbose_name = _('Category')
        verbose_name_plural=_("Categories")
    
    def __str__(self):
        try:
            return self.category
        except:
            return f"category name {self.id}"
        

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='category_posts', verbose_name=_('Category'))
    
    image    = models.ImageField(_("Cover Image"), upload_to='post-images/cover/%d/%m/%Y/', blank=True, null=True)
    title    = models.CharField(_("Post Title"),  max_length=350, blank=True, null=True, unique=True)
    slug     = models.SlugField(max_length=400, unique=True)
    subtitle = models.CharField(_("Subtitle"), max_length=400, blank=True, null=True)
    author   = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_posts', verbose_name=_("Author"))
    body     = models.TextField(_("Body"), blank=True, null=True)
    
    likes       = models.ManyToManyField()
    views_count = models.PositiveIntegerField(_("Views Count"), default=0)
    
    created_at = models.DateField(_("created at"), auto_now_add=True)
    updated_at = models.DateField(_("updated at"), auto_now=True)
    
    class Meta:
        ordering = ['id', 'category', 'author',]
    
    def __str__(self):
        try:
            author = f"{self.author.username}" or ""
            category = f"{self.category.name}" or ""
            title    = f"{self.title}" or f"{self.id}"
            text = f"{category} | {title} ({author})"
        except:
            text = f"post - {self.id}"
        else:
            text = "uncompleted post"
        return text
    
    # @property
    # def likes_count(self):
    #     return self.likes.
    

class PostImages(models.Model):
    post  = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images', verbose_name='Post')
    
    image = models.ImageField(_("Post Image"), upload_to='post-images/body/%d/%m/%Y/')
    caption = models.CharField(_("Caption"), max_length=300, blank=True, null=True)
    
    class Meta:
        ordering = ['id', 'post']
        verbose_name = _("Post Image")
        verbose_name_plural = _("Post Images")
        
    def __str__(self):
        try:
            return f"image id {self.id} | post id {self.post.id}"
        except:
            return f"image id {self.id}"