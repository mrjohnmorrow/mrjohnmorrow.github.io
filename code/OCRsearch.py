from PIL import Image
from pytesseract import image_to_string
import os
import time
import datetime
import re
import sys
import csv

args = sys.argv
# grab the second argument if it exists (should be the path)
# first is always the filename since it's running as > python filename args
if len(args) > 1:
    rootDir = args[1]
else:
	rootDir = '.'
print("Root dir: " + os.path.abspath(rootDir))
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d-%H-%M')
csvname = 'OCRtable' + st + '.csv'
with open(csvname, 'a') as csvfile:
    print("CSV Created: " + os.path.abspath(csvfile.name))
    csvwriter = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    csvwriter.writerow(["Root Dir", os.path.abspath(rootDir)])
    for dirName, subdirList, fileList in os.walk(rootDir):
        for filename in fileList:
            if (re.search('.*jpg',filename.lower()) != None):
                fullfilename = os.path.abspath(dirName) + "/" + filename
                try:
                    ocrtxt = image_to_string(Image.open(fullfilename))
                    csvwriter.writerow([fullfilename, ocrtxt])
                except IOError as e:
                    print "I/O error({0}): {1}".format(e.errno, e.strerror)
