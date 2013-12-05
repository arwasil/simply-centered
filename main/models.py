from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.core.files.storage import default_storage as storage

from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    spling_code = models.IntegerField(blank=True, default=0)
    background = models.ImageField(upload_to='categories', null=True, blank=True, default=None)
    article = models.URLField(max_length=255, blank=True, default='')
    position = models.SmallIntegerField(blank=True, default=0)

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

    def has_sub_menu(self):
        return len(self.sub_menu()) >= 2

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

    def save(self, background_size=(284, 300)):
        super(Category, self).save()

        if self.background:
            # prepare thumbnail for uploaded background image
            try:
                image = Image.open(self.background)
            except:
                image = None
        
            if image:
                src_width, src_height = image.size
                src_ratio = float(src_width) / float(src_height)
                dst_width, dst_height = background_size
                dst_ratio = float(dst_width) / float(dst_height)
                
                if dst_ratio < src_ratio:
                    crop_height = src_height
                    crop_width = crop_height * dst_ratio
                    x_offset = int(float(src_width - crop_width) / 2)
                    y_offset = 0
                else:
                    crop_width = src_width
                    crop_height = crop_width / dst_ratio
                    x_offset = 0
                    y_offset = int(float(src_height - crop_height) / 3)
                image = image.crop((x_offset, y_offset, x_offset+int(crop_width), y_offset+int(crop_height)))
                image = image.resize(background_size, Image.ANTIALIAS)
                fh = storage.open(self.background.name, "w")
                image.save(fh)
                fh.close()
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ("position",)