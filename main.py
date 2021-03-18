import argparse
from PIL import Image
import math

parser = argparse.ArgumentParser(description='OPTIMAGE - Optimize your images.')

parser.add_argument('-p', action='store', dest='image_path',type=str, help='path of image')
parser.add_argument('-d', action='store', dest='destination_path',type=str, help='destination path of image')
parser.add_argument('-q', action='store', dest='quality',type=int, help='quality of image compression')
parser.add_argument('-f', action='store', dest='factor',type=float, help='factor of reduction')

args = parser.parse_args()

try:
  factor = args.factor
  image_path = args.image_path
  destination_path = args.destination_path
  quality = args.quality

  foo = Image.open(args.image_path)

  x, y = foo.size
  x2, y2 = math.floor(x/factor), math.floor(y/factor)
  foo = foo.resize((x2,y2),Image.ANTIALIAS)              

  foo.save(destination_path, optimize=True, quality=quality)

  print('Done!')
except: 
  print('There is an error. Try to type --help to know more about.')
