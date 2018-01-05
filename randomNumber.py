import math
import urllib2
from PIL import Image

'''
This program generates a random bitmap image of size imageSize by pulling
random integers from random.org
'''
def main():
	imageSize = 10 # variable that controls image size
	imageArray = [[[0, 0, 0] for x in xrange(imageSize)] for y in xrange(imageSize)] # array containing randomly generated rgb tuples
	
	for i in range(len(imageArray)): # go row by row generating array because random.org can only return 10,000 integers at a time
		imageArray[i] = pullRandomNumber(imageSize) # call to pullRandomNumber which generates one row of the array
	generateImage(imageArray, imageSize) # generate image using the randomly generated rgb tuples

def pullRandomNumber(imageSize):
	num = imageSize*3
	URL = "https://www.random.org/integers/?num=" + str(num) + "&min=0&max=255&col=1&base=10&format=plain&rnd=new"

	try:
		array = urllib2.urlopen(URL).read() # pull random integers from random.org
		array = array.split() # split array on newline characters
		parsedArray = [[0, 0, 0] for x in xrange(imageSize)] # to format the array into an array of rgb tuples
		for i in xrange(len(array)): # go through the array from random.org reformat so that it is an imageSize array containing rgb tuples
			x = i/3
			y = i%3
			parsedArray[x][y] = int(array[i])
		return parsedArray

	except urllib2.HTTPError as e:
		print e.code
		print e.read()

def generateImage(imageArray, imageSize):
	img = Image.new( 'RGB', (imageSize,imageSize), "black") # create a new black image
	pixels = img.load() # create the pixel map

	for i in range(img.size[0]):    # for every pixel:
	    for j in range(img.size[1]):
	        pixels[i,j] = tuple(imageArray[i][j]) # set the colour accordingly

	img.show()
	
if __name__ == '__main__':
	main()