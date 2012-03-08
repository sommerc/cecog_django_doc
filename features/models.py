import os
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
import sys
sys.path.append("C:/Users/sommerc/code/python/mysite")

from django.db import models
from feature_documentation import group_doc

class FeatureGroup(models.Model):
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200) 
    doc = models.TextField()
    
    def __unicode__(self):
        return self.name

class FeatureCategory(models.Model):
    name = models.CharField(max_length=200)
    doc = models.TextField()
    old_name = models.CharField(max_length=200)
    group = models.ForeignKey(FeatureGroup)
    
    def __unicode__(self):
        return self.name
    
class Feature(models.Model):
    prefix = models.CharField(max_length=200)
    suffix = models.CharField(max_length=200)
    category = models.ForeignKey(FeatureCategory)
    doc = models.TextField()
    
    @property
    def identifier(self):
        return "_".join((self.prefix, self.suffix))
    
    def __unicode__(self):
        return self.identifier
    
class Parameter(models.Model):
    key = models.CharField(max_length=200, default="")
    value = models.CharField(max_length=200, default="")
    
    def __unicode__(self):
        return " : ".join((self.key, self.value))
    
class ParametrizedFeature(models.Model):
    feature = models.ForeignKey(Feature)
    parameter = models.ManyToManyField(Parameter)
    old_identifier = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "_".join([self.feature.prefix,] + [obj.key +"_"+ obj.value for obj in self.parameter.all()] + [self.feature.suffix,]) 
    

    
def fill_database(table_filen_name):
    import csv
    reader = csv.DictReader(open(table_filen_name,'r'), delimiter='\t')
    
    for row in reader:
        group_label = row['new_group']
        group_name = row['new_group_name']
        if group_name in [obj.name for obj in FeatureGroup.objects.all()]:
            feature_group = FeatureGroup.objects.get(name=group_name)
        else:
            try:
                doc = group_doc[group_name]
                print doc
            except:
                doc =""
            feature_group = FeatureGroup(name=group_name, label=group_label, doc=doc)
            feature_group.save()
        
        category_name = row['new_category']
        old_category_name = row['category']
        if category_name in [obj.name for obj in FeatureCategory.objects.all()]:
            feature_category = FeatureCategory.objects.get(name=category_name)
        else:
            feature_category = FeatureCategory(name=category_name, old_name=old_category_name, doc="", group=feature_group)
            feature_category.save()
            
            
        prefix = row['new_prefix']
        suffix = row['suffix']
        if (prefix, suffix) in [(obj.prefix, obj.suffix) for obj in Feature.objects.all()]:
            feature = Feature.objects.get(prefix=prefix, suffix=suffix)
        else:
            feature = Feature(prefix=row['new_prefix'],
                          suffix=row['suffix'],
                          category=feature_category,
                          )
            feature.save()
        
        param_feature = ParametrizedFeature(feature=feature, old_identifier=row['identifier'])
        param_feature.save()
        
        parameter_str = row['parameter']
        if parameter_str:
            for key, value in zip(parameter_str.split("_")[::2], parameter_str.split("_")[1::2]):
                if (key, value) in [(obj.key, obj.value) for obj in Parameter.objects.all()]:
                    param = Parameter.objects.get(key=key, value=value)
                else:
                    param = Parameter(key=key, value=value)
                    param.save()
            
                param_feature.parameter.add(param)
                print " add parameter",key,value,"to",feature.prefix,feature.suffix
                param_feature.save()
        else:
            print " no parameter for found", feature.prefix, feature.suffix

        
if __name__ == '__main___':
#    fill_database("C:/Users/sommerc/cellcognition/doc/feature_table.txt")
    pass
            
    
    
    
    
    