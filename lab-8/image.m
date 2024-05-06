input_file = "C:/Users/Hrushi'/Documents/Computational lab/lab-8/Pic.jpg"

image_data = imread(input_file);
red = image_data(:, :, 1);
blue = image_data(:, :, 2);
green = image_data(:, :, 3);

red_file = 'R.csv';
blue_file = 'B.csv';
green_file = 'G.csv';
csvwrite(red_file, red)
csvwrite(green_file, green)
csvwrite(blue_file, blue)
