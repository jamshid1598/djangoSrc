from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()
# from apps.users.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=200, unique=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)
    
    created_at = models.DateField(_("created at"), auto_now_add=True)
    updated_at = models.DateField(_("updated at"), auto_now=True)
    class Meta:
        ordering=['name', 'created_at', 'updated_at']
        verbose_name = _('Category')
        verbose_name_plural=_("Categories")
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        return super(Category, self).save(*args, **kwargs)
        

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='category_posts', verbose_name=_('Category'))
    
    image    = models.ImageField(_("Cover Image"), upload_to='post-images/cover/%d/%m/%Y/', blank=True, null=True)
    title    = models.CharField(_("Post Title"),  max_length=350, blank=True, null=True, unique=True)
    slug     = models.SlugField(max_length=400, unique=True)
    subtitle = models.CharField(_("Subtitle"), max_length=400, blank=True, null=True)
    author   = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_posts', verbose_name=_("Author"))
    body     = models.TextField(_("Body"), blank=True, null=True)

    views_count = models.PositiveIntegerField(_("Views Count"), default=0)    
    
    created_at = models.DateField(_("created at"), auto_now_add=True)
    updated_at = models.DateField(_("updated at"), auto_now=True)
    
    class Meta:
        ordering = ['id', 'category', 'author',]
    
    def __str__(self):
        return self.title
    
    @property
    def reaction_count(self):
        return self.post_reaction.all().count()
    
    @property
    def comment_count(self):
        return self.post_comment.all().count() 

class PostImages(models.Model):
    post  = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images', verbose_name='Post')
    
    image   = models.ImageField(_("Post Image"), upload_to='post-images/body/%d/%m/%Y/')
    caption = models.CharField(_("Caption"), max_length=300, blank=True, null=True)
    
    class Meta:
        ordering = ['id', 'post']
        verbose_name = _("Post Image")
        verbose_name_plural = _("Post Images")
        
    def __str__(self):
        return f"image id {self.id}"

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="user_comment", verbose_name=_("User"))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment', verbose_name=_("Post"))

    comment  = models.CharField(_("Comment"), max_length=500, blank=True, null=True)

    created_at = models.DateField(_("created at"), auto_now_add=True)
    updated_at = models.DateField(_("updated at"), auto_now=True)
    class Meta:
        ordering = ['id', 'updated_at', 'created_at']
        verbose_name = _("Post Comment")
        verbose_name_plural = _("Post Comments")
    
    def __str__(self):
        return f"comment id: {self.id}"

class PostReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_post_reaction', verbose_name=_("User"))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_reaction", verbose_name=_("Post"))
    class ReactionChoice(models.TextChoices):
        LIKE  = 'like',  '👍'
        LOVE  = 'love',  '❤️'
        LOL   = 'lol',   '😂'
        ANGRY = 'angry', '😡'
        CRY   = 'cry',   '😭'
    reaction = models.CharField(_("Reaction"), max_length=10, blank=True, null=True, choices=ReactionChoice.choices)
    
    created_at = models.DateField(_('created at'), auto_now_add=True)
    updated_at = models.DateField(_('updated at'), auto_now=True)
    class Meta:
        ordering = ['id', 'created_at', 'updated_at']
        verbose_name = _('Post Reaction')
        verbose_name_plural = _('Post Reactions')
    
    def __str__(self):
        return f"reaction id: {self.id}"

class CommentReaction(models.Model):
    user    = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='user_comment_reaction', verbose_name=_("User"))
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name="comment_reaction", verbose_name=_("Comment"))
    class ReactionChoice(models.TextChoices):
        LIKE  = 'like',  '👍'
        LOVE  = 'love',  '❤️'
        LOL   = 'lol',   '😂'
        ANGRY = 'angry', '😡'
        CRY   = 'cry',   '😭'
    reaction = models.CharField(_("Reaction"), max_length=10, blank=True, null=True, choices=ReactionChoice.choices)
    
    created_at = models.DateField(_('created at'), auto_now_add=True)
    updated_at = models.DateField(_('updated at'), auto_now=True)
    class Meta:
        ordering = ['id', 'created_at', 'updated_at']
        verbose_name = _('Comment Reaction')
        verbose_name_plural = _('Comment Reactions')
    
    def __str__(self):
        return f"reaction id: {self.id}"