import cv2
import numpy as np

input_file = "C:/Users/Hrushi'/Documents/Computational lab/lab-8/Pic.jpg"

image_data = cv2.imread(input_file)
blue, green, red = cv2.split(image_data)

red_file = 'R.csv'
green_file = 'G.csv'
blue_file = 'B.csv'

np.savetxt(red_file, red, delimiter=',')
np.savetxt(green_file, green, delimiter=',')
np.savetxt(blue_file, blue, delimiter=',')

