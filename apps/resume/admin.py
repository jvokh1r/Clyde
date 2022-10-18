from django.contrib import admin
from .models import Skill, Service, Project, Advantage, FeedBack, ResumeModel


class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', )


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', )


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', )


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(ResumeModel)
admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(FeedBack)


