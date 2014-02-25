from django.conf.urls import patterns, url


urlpatterns = patterns('librarinars.library.views',
    url(r'^$', 'index', name='index'),
)
