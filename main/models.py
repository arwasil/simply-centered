from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from utils import image

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    spling_code = models.IntegerField(blank=True, default=0)
    background = models.ImageField(upload_to='categories', null=True, blank=True, default=None)
    article = models.URLField(max_length=255, blank=True, default='')
    position = models.SmallIntegerField(blank=True, default=0)
    full_url = models.CharField(max_length=255, editable=False, blank=True, default='')

    show_in_menu = models.BooleanField(blank=True, default=True)
    show_in_video = models.BooleanField(blank=True, default=False)
    show_in_shop = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return self.name

    def sub_menu(self):
        return Category.objects.filter(show_in_menu=True, parent=self)

    def sub_menu_2(self):
        return self.sub_menu()[0:2]

    def sub_menu_4(self):
        return self.sub_menu()[0:4]

    def facet_icon(self):
        return 'img/facet-' + self.slug + '-big-icon.png'

    @property
    def parent_categories(self):
        parents = [self]
        for level in (1, 2, 3):
            if not parents[0].parent:
                break
            parents = [parents[0].parent] + parents
        return parents

    @property
    def root(self):
        return self.parent_categories[0]

    def sub_categories(self, area=None):
        list = Category.objects.filter(parent=self)

        if area == 'menu': 
            list = list.filter(show_in_menu=True)
        elif area == 'shop': 
            list = list.filter(show_in_shop=True)
        elif area == 'video': 
            list = list.filter(show_in_video=True)

        return list

    @property
    def shop_slug(self):
        return 'market-%s' % self.slug

    @property
    def video_slug(self):
        return 'video-%s' % self.slug

    def save(self):
        self.full_url = '/' + '/'.join([parent.slug for parent in self.parent_categories]) + '/'

        super(Category, self).save()

        if self.background:
            image.resize_image(self.background, (284, 300))
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ("position",)


class Promotion(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, default='')
    background = models.ImageField(upload_to='promotions', null=True, blank=True, default=None)

    def __unicode__(self):
        return "%s - %s" % (self.category, self.name)

    def save(self):
        super(Promotion, self).save()

        if self.background:
            image.resize_image(self.background, (142, 300))
