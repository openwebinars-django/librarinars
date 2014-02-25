from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from librarinars.library.forms import BookForm


def index(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    form = BookForm(data=data)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
    return render_to_response('index.html',
                              {'form': form},
                              context_instance=RequestContext(request))
