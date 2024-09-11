from django.urls import path
from . import views
from .views import (
    StudentCreateView, GeneralInformationView, LearningProfileView,
    DevelopmentalAreasView, SkillsStrengthsView,
    AccessibleLearningSupportView, MeasurableGoalsView,
    InterventionServicesView, SupplementaryServicesView, ICPListView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', ICPListView.as_view(), name='list_icps'),
    path('create/', views.StudentCreateView.as_view(), name='create_icp'),
    path('success/', views.icp_success, name='icp_success'),
    path('<int:student_id>/general-information/', GeneralInformationView.as_view(), name='general_information'),
    path('<int:student_id>/learning-profile/', LearningProfileView.as_view(), name='learning_profile'),
    path('<int:student_id>/developmental-areas/', DevelopmentalAreasView.as_view(), name='developmental_areas'),
    path('<int:student_id>/skills-strengths/', SkillsStrengthsView.as_view(), name='skills_strengths'),
    path('<int:student_id>/accessible-learning-support/', AccessibleLearningSupportView.as_view(), name='accessible_learning_support'),
    path('<int:student_id>/measurable-goals/', MeasurableGoalsView.as_view(), name='measurable_goals'),
    path('<int:student_id>/goal-added/', views.goal_added, name='goal_added'),
    path('<int:student_id>/intervention-services/', InterventionServicesView.as_view(), name='intervention_services'),
    path('<int:student_id>/supplementary-services/', SupplementaryServicesView.as_view(), name='supplementary_services'),
    path('<int:student_id>/generate-icp/', views.generate_icp, name='generate_icp'),

]
