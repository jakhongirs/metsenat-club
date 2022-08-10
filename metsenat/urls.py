from django.urls import path
from metsenat import views

urlpatterns = [
    # Sponsor
    path("sponsor/register/", views.RegisterSponsorView.as_view(), name="register_sponsor"),
    path("sponsors/", views.ListSponsorsView.as_view(), name="sponsors"),
    path('sponsor/<int:id>/', views.DetailSponsorView.as_view(), name="detail_sponsor"),
    path('sponsor/update/<int:id>/', views.UpdateSponsorView.as_view(), name="update_sponsor"),

    # University:
    path("university/create/", views.CreateUniversityView.as_view(), name="create_university"),

    # Student:
    path("student/register/", views.RegisterStudentView.as_view(), name="register_student"),
    path("students/", views.ListStudentsView.as_view(), name="students"),
    path('student/<int:id>/', views.DetailStudentView.as_view(), name="detail_student"),
    path('student/update/<int:id>/', views.UpdateStudentView.as_view(), name="update_student"),
]
