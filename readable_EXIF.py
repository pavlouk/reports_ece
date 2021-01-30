# -*- coding: utf-8 -*-
from PIL.ExifTags import TAGS

def readable_EXIF(exifdata):
    exifList = []
    try:
        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            exifList.append(f"{tag:25}: {data}")
    except UnicodeDecodeError:
        return exifList
    return exifList
        