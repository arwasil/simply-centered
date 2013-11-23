from django.db import models
from django.core.urlresolvers import reverse

SPLING_CATEGORIES = {
    "food": 265,
    "cooking": 266,
    "healthy diets": 267,
    "recipes": 268,
    "natural kitchen": 269,
    "diets": 270,
    "superfoods": 271,
    "health": 272,
    "beauty": 273,
    "natural health": 274,
    "inner beauty": 275,
    "outer beauty": 276,
    "wellness": 277,
    "longevity": 278,
    "fitness": 279,
    "mindful fitness": 280,
    "optimum body": 281,
    "yoga": 282,
    "alternative exercise": 283,
}

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    spling_code = models.IntegerField(blank=True, default=0)
    image = models.URLField(blank=True, default='')

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

    class Meta:
        verbose_name_plural = "categories"