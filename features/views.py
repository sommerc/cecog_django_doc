from django.template import Context, loader
from features.models import FeatureGroup, FeatureCategory, Feature, ParametrizedFeature, Parameter
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    feature_groups = FeatureGroup.objects.all()
    feature_category = FeatureCategory.objects.all()
    feature = Feature.objects.all()
    param_feature = ParametrizedFeature.objects.all()
    return render_to_response('features/feature_groups.html', {'feature_groups': feature_groups,
                                                               'feature_category': feature_category,
                                                               'feature': feature,
                                                               'param_feature': param_feature})
