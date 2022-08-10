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

    # Student Sponsor:
    path("student/sponsor/create", views.CreateStudentSponsorView.as_view(), name="create_student_sponsor"),
    path('student/sponsor/update/<int:id>/', views.UpdateStudentSponsorView.as_view(), name="update_student_sponsor"),

    # Dashboard:
    path("dashboard/", views.DashboardData.as_view(), name="dashboard"),
    path("dashboard/students", views.DashboardLineStudent.as_view(), name="dashboard_student"),
    path("dashboard/sponsor", views.DashboardLineSponsor.as_view(), name="dashboard_sponsor"),
]
