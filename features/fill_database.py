import os, sys
sys.path.append("C:/Users/sommerc")
sys.path.append("C:/Users/sommerc/cellcognition-doc")
os.environ["DJANGO_SETTINGS_MODULE"] = "cellcognition-doc.settings"

from features.models import fill_database, clean_databse, fill_reference_table

clean_databse()
fill_reference_table()
fill_database("feature-table.txt")
