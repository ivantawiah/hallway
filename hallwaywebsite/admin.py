from django.contrib import admin
from .models import Testimony
from .models import MostFeaturedArticle
from .models import Team
from .models import HallwayEvent
from .models import GeneralArticle
from .models import TopPerformingProfessionalArticle
from .models import TrendingVendorArticle

# Register your models here.
admin.site.register(Testimony)
admin.site.register(MostFeaturedArticle)
admin.site.register(Team)
admin.site.register(HallwayEvent)
admin.site.register(GeneralArticle)
admin.site.register(TopPerformingProfessionalArticle)
admin.site.register(TrendingVendorArticle)
