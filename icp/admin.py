from django.contrib import admin
from .models import (
    Student, GeneralInformation, LearningProfile, DevelopmentalArea,
    SkillsStrengths, AccessibleLearningSupport, Goal, InterventionService,
    SupplementaryService, ICPParticipant, ImportantDates
)

admin.site.register(Student)
admin.site.register(GeneralInformation)
admin.site.register(LearningProfile)
admin.site.register(DevelopmentalArea)
admin.site.register(SkillsStrengths)
admin.site.register(AccessibleLearningSupport)
admin.site.register(Goal)
admin.site.register(InterventionService)
admin.site.register(SupplementaryService)
admin.site.register(ICPParticipant)
admin.site.register(ImportantDates)
