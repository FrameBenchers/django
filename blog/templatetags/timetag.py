from django import template
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

register = template.Library()

@register.filter
def current_time(obj):
    # logger.info("Article Rendering Ended - 0001")
    return True
