from django.template import Context, loader
from features.models import FeatureGroup, \
                            FeatureCategory, \
                            Feature, \
                            ParametrizedFeature, \
                            Parameter, \
                            FeatureReference, \
                            ParameterSet
                            
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    feature_groups = FeatureGroup.objects.all()
    feature_references = FeatureReference.objects.all()
    
    return render_to_response('overview.html', {'feature_groups': feature_groups,
                                                'feature_references': feature_references,}
                                                )
