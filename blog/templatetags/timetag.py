from django import template
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

register = template.Library()

@register.filter
def current_time(counter):
    logger.info("%d Article Rendering Ended - 0001" % counter)
    return True
