from django.shortcuts import render
from django.http import Http404
from blog.models import Blog
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page rendering')
    return render(request, 'index.html', {})

def entity(request, pk):
    try:
        logger.info("Object access requested - 0002")
        article = Blog.objects.get(pk=pk)
        logger.info("Object access completed - 0002")
    except Blog.DoesNotExist:
        raise Http404("Blog post not found")
    # logger.info("Article Rendering Started - 0001")
    return render(request, 'entity.html', {'article': article})
