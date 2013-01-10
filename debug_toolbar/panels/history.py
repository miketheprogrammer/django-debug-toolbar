try:
    import resource
except ImportError:
    pass  # Will fail on Win32 systems
import time
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from debug_toolbar.panels import DebugPanel


class AjaxHistoryPanel(DebugPanel):
    """
    Panel that displays the time a response took in milliseconds.
    """
    name = 'AjaxHistory'
    template = 'debug_toolbar/panels/history.html'

    try:  # if resource module not available, don't show content panel
        resource
    except NameError:
        has_content = False
        has_resource = False
    else:
        has_content = True
        has_resource = True

    def process_request(self, request):
        pass
    def process_response(self, request, response):
        pass

    def nav_title(self):
        return _('Ajax History')
    def nav_subtitle(self):
        return _('0 REQUESTS')

    def title(self):
        return _('Ajax History')

    def url(self):
        return ''
