import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.http import require_POST

from .forms import EventForm, ProfileForm
from .models import Event, Profile, Photo

from jfu.http import upload_receive, UploadResponse, JFUResponse


def contest_home(request, template_name="contest_home.html"):
    form = ProfileForm()
    context = {
        'form': form,
    }
    return render_to_response(template_name, context, RequestContext(request))


@require_POST
def jfu_upload(request):
    event = get_object_or_404(Event, id=request.session['event_id'])
    profile = get_object_or_404(Profile, id=request.session['profile_id'])

    uploaded_file = upload_receive(request)

    instance = Photo(
        photo=uploaded_file,
        event=event,
        profile=profile,
    )
    instance.save()

    basename = os.path.basename(instance.photo.path)

    file_dict = {
        'name': basename,
        'size': uploaded_file.size,

        'url': instance.photo.url,
        'thumbnailUrl': instance.get_thumbnail().url,

        #'deleteUrl': reverse('jfu_delete', kwargs={'pk': instance.pk}),
        #'deleteType': 'POST',
    }

    return UploadResponse(request, file_dict)


def profile_view(request, template_name="profile.html"):
    profile_id = request.session.get('profile_id', None)
    try:
        instance = Profile.objects.get(id=profile_id)
    except Profile.DoesNotExist:
        instance = None
    form = ProfileForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save()
            request.session['profile_id'] = profile.id
            return HttpResponseRedirect(reverse('event'))
    context = {'form': form,}
    return render_to_response(template_name, context, RequestContext(request))


def event_view(request, template_name="event.html"):
    if not request.session.get('profile_id', None):
        return HttpResponseRedirect(reverse('profile'))

    event_id = request.session.get('event_id', None)

    form = EventForm(request.POST or None, initial={'event': event_id})
    if request.method == 'POST':
        if form.is_valid():
            request.session['event_id'] = form.cleaned_data['event'].id
            return HttpResponseRedirect(reverse('submit'))
    context = {'form': form,}
    return render_to_response(template_name, context, RequestContext(request))


def submit(request, template_name="submit.html"):
    if not request.session.get('event_id', None):
        return HttpResponseRedirect(reverse('event'))

    event = get_object_or_404(Event, id=request.session['event_id'])
    profile = get_object_or_404(Profile, id=request.session['profile_id'])
    context = {
        'event': event,
        'profile': profile,
    }
    return render_to_response(template_name, context, RequestContext(request))


def gallery(request, template_name="gallery.html"):
    return render_to_response(template_name, context, RequestContext(request))


def about(request, template_name="about.html"):
    return render_to_response(template_name, context, RequestContext(request))


def contact(request, template_name="contact.html"):
    return render_to_response(template_name, context, RequestContext(request))