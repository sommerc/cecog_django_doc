from features.models import FeatureGroup, FeatureCategory, Feature, ParametrizedFeature, Parameter, ParameterSet,FeatureReference
from django.contrib import admin

admin.site.register(FeatureGroup)
admin.site.register(FeatureCategory)
admin.site.register(Feature)
admin.site.register(ParametrizedFeature)
admin.site.register(Parameter)
admin.site.register(ParameterSet)
admin.site.register(FeatureReference)