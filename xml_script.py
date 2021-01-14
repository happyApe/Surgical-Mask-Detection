# A simple script to edit the path tag in xml of annotated files
# Created by me!
import os
import xml.etree.ElementTree as ET

basepath = 'annotations'
count = 0;
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath,entry)):
                tree = ET.parse(basepath+'/'+entry)
                elem = tree.findall('path')[0]
                elem2 = tree.findall('file_name')[0]
    
                elem.text = 'new+path'
  
                tree.write(basepath+'/'+entry)

# tree = ET.parse('annotations/train1.xml')
# elem = tree.findall('path')[0]
# elem.text = 'new+path'
# tree.write('annotations/train1_new.xml')
