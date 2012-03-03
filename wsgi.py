import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "linux_org_hk.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
# only available in Django 1.4+
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

import sys, site

vepath = '/srv/linux.org.hk/hklug-web/env_hklug/lib/python2.6/site-packages'

prev_sys_path = list(sys.path)
# add the site-packages of our virtualenv as a site dir
site.addsitedir(vepath)
# add the app's directory to the PYTHONPATH
sys.path.append('/srv/linux.org.hk/hklug-web/')

# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
    sys.path[:0] = new_sys_path

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
