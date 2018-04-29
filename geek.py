# -*- coding: utf-8 -*-
#!/usr/bin/env python
import signal
import sys
import axi
import random
import subprocess

# TODO : attraper le ctrl-c et faire un raise-pen - retour a zero ...
def signal_handler(signal, frame):
	print('You pressed Ctrl+C! Back home AxiDraw!')
	device = axi.Device()
	device.pen_up()
	device.goto(0, 0)
	device.disable_motors()
	sys.exit(0)
        
signal.signal(signal.SIGINT, signal_handler)
#print('Press Ctrl+C')
#signal.pause()

def replaceSpecialCharacters(inputText):
	outputText = inputText.replace('ç', 'c')
	outputText = outputText.replace('é', 'e')
	outputText = outputText.replace('è', 'e')
	outputText = outputText.replace('ê', 'e')
	outputText = outputText.replace('î', 'i')
	outputText = outputText.replace('ï', 'i')
	outputText = outputText.replace('à', 'a')
	outputText = outputText.replace('ö', 'o')
	outputText = outputText.replace('ô', 'o')
	return outputText

def getWikiquotes():
	proc = subprocess.Popen(["python3", "-c", "import geekwikiquotes; geekwikiquotes.getCitations()"], stdout=subprocess.PIPE)
	out = proc.communicate()[0]
	return out
	
def drawAxi(citation):
	#t = axi.text(citation, axi.FUTURAL)
	t = axi.text(citation, axi.GOTHICENG)
	drawing = axi.Drawing(t)
	drawing = drawing.rotate_and_scale_to_fit(11, 1, step=180) #8.5
	axi.draw(drawing)


def main():
	#citation = replaceSpecialCharacters( getWikiquotes() )
	citation = "Z"
	#print("citation = %s" % citation)
	drawAxi(citation)
    

if __name__ == '__main__':
    main()

