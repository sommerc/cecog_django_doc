from features.models import FeatureGroup, FeatureCategory, Feature, ParametrizedFeature, Parameter
from django.contrib import admin

admin.site.register(FeatureGroup)
admin.site.register(FeatureCategory)
admin.site.register(Feature)
admin.site.register(ParametrizedFeature)
admin.site.register(Parameter)