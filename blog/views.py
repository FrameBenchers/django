from django.shortcuts import render
from django.http import Http404
from blog.models import Blog
from counter.models import Counter
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page rendering')
    return render(request, 'index.html', {})

def entity(request, pk):
    counter = Counter.objects.first()
    if not counter:
        counter = Counter.objects.create(value=0)
        counter.save()
    try:
        logger.info("%d Object access requested - 0002" % counter.value)
        article = Blog.objects.get(pk=pk)
        logger.info("%d Object access completed - 0002" % counter.value)
    except Blog.DoesNotExist:
        raise Http404("Blog post not found")
    counter.value += 1
    counter.save()
    logger.info("%d Article Rendering Started - 0001" % counter.value)
    return render(request, 'entity.html', {'article': article, 'counter': counter.value})
