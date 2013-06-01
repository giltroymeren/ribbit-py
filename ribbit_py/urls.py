from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ribbit_py_app.views.index'), # root
    url(r'^login$', 'ribbit_py_app.views.login_view'), # login
    url(r'^logout$', 'ribbit_py_app.views.logout_view'), # logout
    url(r'^signup$', 'ribbit_py_app.views.signup'), # signup
)
