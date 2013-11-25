from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    spling_code = models.IntegerField(blank=True, default=0)
    background = models.ImageField(upload_to='categories', null=True, blank=True, default=None)
    article = models.URLField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return self.name

    @property
    def parent_categories(self):
        parents = [self]
        for livel in (1, 2, 3):
            if not parents[0].parent:
                break
            parents = [parents[0].parent] + parents
        return parents

    @property
    def root_category(self):
        return self.parent_categories[0]

    @property
    def subcategories(self):
        return Category.objects.filter(parent=self)

    @property
    def has_subcategories(self):
        return len(self.subcategories) >= 2


    class Meta:
        verbose_name_plural = "categories"