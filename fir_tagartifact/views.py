from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import render_to_string
from django.http import JsonResponse

from incidents import views as incidents_views
from fir_artifacts.models import Artifact
from fir_tagartifact.forms import TagForm

from fir_tagartifact.tag import Tag


@login_required
@user_passes_test(incidents_views.is_incident_handler)
def tagartifact_addtag(request, content_type=None, object_id=None):
	object_type = ContentType.objects.get(pk=content_type)
	obj = get_object_or_404(object_type.model_class(), pk=object_id)

	if request.method == "GET":
		tag_form = TagForm(obj.category)

	if request.method == 'POST':
		tag_form = TagForm(obj.category, request.POST)

		if tag_form.is_valid():
			value = "{name}: {value}".format(name=tag_form.cleaned_data['name'].name,
											 value=tag_form.cleaned_data['value'])
			try:
				artifact = Artifact.objects.get(type=Tag.key, value__iexact=value)
			except Artifact.DoesNotExist:
				artifact = Artifact.objects.create(type=Tag.key, value=value)
			except Artifact.MultipleObjectsReturned:
				try:
					artifact = Artifact.objects.get(type=Tag.key, value=value)
				except Artifact.DoesNotExist:
					artifact = Artifact.objects.create(type=Tag.key, value=value)
				except Artifact.MultipleObjectsReturned:
					artifact = Artifact.objects.get(type=Tag.key, value=value)[0]
			artifact.relations.add(obj)
			artifact.save()
			ret = {'status': 'success'}
			return JsonResponse(ret)
		else:
			errors = render_to_string("fir_tagartifact/tag_form.html", {'tag_form': tag_form, 'obj_id': object_id, 'obj_type': content_type})
			ret = {'status': 'error', 'data': errors}
			return JsonResponse(ret)

	return render(request, "fir_tagartifact/tag_form.html", {'tag_form': tag_form, 'obj_id': object_id, 'obj_type': content_type})
