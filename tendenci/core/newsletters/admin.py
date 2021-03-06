from django.conf import settings
from django.contrib import admin
from django.core.urlresolvers import reverse

from tendenci.core.newsletters.models import NewsletterTemplate


class NewsletterTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'rendered_view', 'content_view']

    def rendered_view(self, obj):
        link_icon = '%simages/icons/external_16x16.png' % settings.STATIC_URL
        link = '<a href="%s" title="%s"><img src="%s" /></a>' % (
            obj.get_absolute_url(),
            obj,
            link_icon,
        )
        return link
    rendered_view.allow_tags = True
    rendered_view.short_description = 'view rendered template'

    def content_view(self, obj):
        link_icon = '%simages/icons/external_16x16.png' % settings.STATIC_URL
        link = '<a href="%s" title="%s"><img src="%s" /></a>' % (
            obj.get_content_url(),
            obj,
            link_icon,
        )
        return link
    content_view.allow_tags = True
    content_view.short_description = 'view template content'


admin.site.register(NewsletterTemplate, NewsletterTemplateAdmin)
