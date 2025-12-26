from django.contrib import admin
from .models import OctoUser, Team, Activity, Workout, Leaderboard

admin.site.register(OctoUser)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Leaderboard)
