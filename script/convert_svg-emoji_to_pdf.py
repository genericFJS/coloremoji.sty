# -*- coding: UTF-8 -*-
import os
import sys
import cairosvg

print "Converting svg emojis to pdf ..."
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
# get emoji path (either by command line arguments or by input):
emojiPath = ''
if len(sys.argv) > 1:
	emojiPath = sys.argv[1]
else:
	print "Enter [1] for emojitwo, [2] for twemoji or a path to another svg emoji source:"
	emojiPath = str(raw_input())
if emojiPath == '1' or emojiPath == '[1]':
	emojiPath = '../emojitwo/svg'
elif emojiPath == '2' or emojiPath == '[2]':
	emojiPath = '../emojitwo/svg'
# check if valid diretory:
if not (os.path.isdir(emojiPath)):
	print 'Directory "'+emojiPath+'" does not exist. It has to be relative to the location of this script. I.e. "../emojies/svg" for the folder "emojies" in the repository root folder.'
	sys.exit(1)
# process SVGs:
hasSVG = False
processedCount = 0
for filename in os.listdir(emojiPath):
	processedCount += 1
	if os.path.isfile(emojiPath+'/'+filename) and filename.endswith('.svg'):
		hasSVG = True
		cairosvg.svg2pdf(url=emojiPath+'/'+filename, write_to='../emoji_images/'+filename.split('.svg')[0]+'.pdf')
		sys.stdout.write('Processing: '+str(processedCount)+'\r')
# check if SVGs were processed:
if not hasSVG:
	print 'There are no svg-files in the folder "'+emojiPath+'".'
	sys.exit(1)
print "\nDone."