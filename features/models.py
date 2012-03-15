from django.db import models
from content import group_doc, \
                    category_doc, \
                    feature_doc, \
                    github_prefix, \
                    feature_githublink, \
                    parameter_doc, \
                    reference_doc, \
                    general_doc
                                  
def get_model_fields(model):
    return map(lambda x: x.name, model._meta.fields)

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
    github_link = models.CharField(max_length=300)
    
    @property
    def identifier(self):
        return "_".join((self.prefix, self.suffix))
    
    def __unicode__(self):
        return self.identifier
    
class Parameter(models.Model):
    key = models.CharField(max_length=200, default="")
    description = models.TextField()  
    feature = models.ForeignKey(Feature)  
    
    def __unicode__(self):
        return self.key 

class ParameterSet(models.Model):
    key = models.ForeignKey(Parameter)
    value = models.CharField(max_length=200, default="")

    def __unicode__(self):
        return " : ".join((str(self.key), self.value))
    
class ParametrizedFeature(models.Model):
    feature = models.ForeignKey(Feature)
    parameter = models.ManyToManyField(ParameterSet)
    old_identifier = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "_".join([self.feature.prefix,] + [obj.key.key +"_"+ obj.value for obj in self.parameter.all()] + [self.feature.suffix,]) 
    
class FeatureReference(models.Model):
    key = models.CharField(max_length=42)
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    journal = models.CharField(max_length=300)
    month = models.CharField(max_length=12)
    number = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    volume = models.CharField(max_length=10)
    pages = models.CharField(max_length=10)
    publisher = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=42, default='article')
    label_nr = models.IntegerField()
    
    def __unicode__(self):
        return self.key
    
    
def clean_databse():
    for cls in [ParametrizedFeature, 
                ParameterSet, 
                Parameter, 
                Feature, 
                FeatureCategory, 
                FeatureGroup, 
                FeatureReference]:
        [obj.delete() for obj in cls.objects.all()]
        
def fill_reference_table():
    from pybtex.database.input import bibtex
    parser = bibtex.Parser()
    bib = parser.parse_file("mito.bib")
    for label_nr, key in reference_doc.items():
        ent = bib.entries[key]
        init_args = {}
        for field in get_model_fields(FeatureReference):
            if field in ent.fields.keys():
                init_args[field] = ent.fields[field]
                
        init_args['author'] = ", ".join([" ".join((obj.first()[0], obj.last()[0])) for obj in ent.persons['author']])
        init_args['key'] = key
        init_args['label_nr'] = label_nr
        feat_ref = FeatureReference(**init_args)
        feat_ref.save()
  
def fill_database(table_filen_name):
    import csv
    reader = csv.DictReader(open(table_filen_name,'r'), delimiter='\t')
    
    for row in reader:
        group_label = row['new_group']
        group_name = row['new_group_name']
        if group_name in [obj.name for obj in FeatureGroup.objects.all()]:
            feature_group = FeatureGroup.objects.get(name=group_name)
        else:
            doc = group_doc[group_name]
            feature_group = FeatureGroup(name=group_name, label=group_label, doc=doc)
            feature_group.save()
        
        category_name = row['new_category']
        old_category_name = row['category']
        if category_name in [obj.name for obj in FeatureCategory.objects.all()]:
            feature_category = FeatureCategory.objects.get(name=category_name)
        else:
            doc = category_doc[category_name]
            feature_category = FeatureCategory(name=category_name, 
                                               old_name=old_category_name, 
                                               doc=doc, 
                                               group=feature_group)
            feature_category.save()
            
            
        prefix = row['new_prefix']
        suffix = row['suffix']
        if (prefix, suffix) in [(obj.prefix, obj.suffix) for obj in Feature.objects.all()]:
            feature = Feature.objects.get(prefix=prefix, suffix=suffix)
        else:
            doc_key = "___".join((prefix, suffix))
            feature = Feature(prefix=prefix,
                          suffix=suffix,
                          category=feature_category,
                          doc=feature_doc[doc_key],
                          github_link = github_prefix + feature_githublink[doc_key][0] + "#L%d-%d" % \
                                                                                    (feature_githublink[doc_key][1],
                                                                                     feature_githublink[doc_key][2])
                          )
            feature.save()
            print "Created feature", feature
        
        param_feature = ParametrizedFeature(feature=feature, old_identifier=row['identifier'])
        param_feature.save()
        
        parameter_str = row['parameter']
        if parameter_str:
            for key, value in zip(parameter_str.split("_")[::2], parameter_str.split("_")[1::2]):
                if (key, feature) in [(obj.key, obj.feature) for obj in Parameter.objects.all()]:
                    param_key = Parameter.objects.get(key=key, feature=feature)
                    param_key.save()
                else:
                    param_key = Parameter(key=key, description=parameter_doc[key], feature=feature)
                    param_key.save()
                
                if (param_key, value) in [(obj.key, obj.value) for obj in ParameterSet.objects.all()]:
                    param = ParameterSet.objects.get(key=param_key, value=value)
                else:
                    param = ParameterSet(key=param_key, value=value)
                    param.save()
            
                param_feature.parameter.add(param)
                param_feature.save()
            
    

        

            
    
    
    
    
    