from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("login", views.CvLoginView.as_view(), name="login-page"),
    path("upload", login_required(views.UploadCVView.as_view()), name="upload-cv"),
    path("", login_required(views.StartingPageView.as_view()), name="starting-page"),
    path("<slug:slug>", views.CandidateDetailView.as_view(), name="candidate-detail"),
    path("interviewee/", views.IntervieweeView.as_view(),name="interviewee"),
    path("tags/", views.TagsSelectView.as_view(), name="tags-select"),
]