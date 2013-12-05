from django.core.files.storage import default_storage as storage

from PIL import Image

def resize_image(source_image, size):
    try:
        image = Image.open(source_image)
    except:
        image = None

    if image:
        src_width, src_height = image.size
        dst_width, dst_height = size
        if src_width <= dst_width and src_height <= dst_height:
            return
    
        src_ratio = float(src_width) / float(src_height)
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
        
        image = image.crop((x_offset, y_offset, x_offset + int(crop_width), y_offset + int(crop_height)))
        image = image.resize(size, Image.ANTIALIAS)
        fh = storage.open(source_image.name, "w")
        image.save(fh)
        fh.close()