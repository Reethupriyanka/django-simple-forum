from django.conf import settings

DJANGO_SIMPLE_FORUM_TOPICS_PER_PAGE = getattr(settings, 'DJANGO_SIMPLE_FORUM_TOPICS_PER_PAGE', 10)
DJANGO_SIMPLE_FORUM_REPLIES_PER_PAGE = getattr(settings, 'DJANGO_SIMPLE_FORUM_REPLIES_PER_PAGE', 10)
