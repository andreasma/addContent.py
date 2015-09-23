# addContent.py

This is a script to directly create a new tupcenter (http://github.com/tdf/tdf.templateuploadcenter 
has to installed) inside a Plone instance. The script creates a title of the new object and fills 
all required fields, that has no default content, with some content. You can change the strings in the script 
to your own purpose.

Usage: If your Plone instance get started with the command ./bin/instance start and is e.g. named 'testing' you could run this script with:

`./bin/instance -O testing run addContent.py`