from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

from profiles.forms import ProfileInfoForm, ProfileSummaryForm, ProfilePictureForm
from profiles.models import Profile


def index(request):
    latest_profile_list = Profile.objects.order_by("-created_at")[:]
    context = {"latest_profile_list": latest_profile_list}
    return render(request, "profiles/index.html", context)


def detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {"profile": profile}
    return render(request, "profiles/detail.html", context)


def detail_picture_form(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {"profile": profile}
    if request.method == "PUT":
        data = QueryDict(request.body)
        form = ProfilePictureForm(data, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, "profiles/partials/picture.html", context)
    context["form"] = ProfilePictureForm(instance=profile)
    return render(request, "profiles/partials/picture-form.html", context)


def detail_info_form(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {"profile": profile}
    if request.method == "PUT":
        data = QueryDict(request.body)
        form = ProfileInfoForm(data, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, "profiles/partials/info.html", context)
    context["form"] = ProfileInfoForm(instance=profile)
    return render(request, "profiles/partials/info-form.html", context)


def detail_summary_form(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {"profile": profile}
    if request.method == "PUT":
        data = QueryDict(request.body)
        form = ProfileSummaryForm(data, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, "profiles/partials/summary.html", context)
    context["form"] = ProfileSummaryForm(instance=profile)
    return render(request, "profiles/partials/summary-form.html", context)


def delete(request, pk):
    report = Profile.objects.get(id=pk)
    report.delete()
    return index(request)


def test(request):
    return render(request, "profiles/test.html")
