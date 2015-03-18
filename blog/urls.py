from django.conf.urls import patterns, url
from . import views, feed
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url('^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
