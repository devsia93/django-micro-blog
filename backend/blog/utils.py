from django.utils.text import slugify

from transliterate import translit

IGNORE_SLUGS = ('create', 'detail', 'update', 'delete')
POST_COUNT_ON_PAGE = 5


def generation_slug(text):
    new_slug = slugify(translit(u"".join(text), 'ru', reversed=True))
    return new_slug
