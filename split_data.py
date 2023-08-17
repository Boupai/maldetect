import splitfolders


input_folder = '/home/nvidia/jetson-inference/final-project/malaria_original'


# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, (.8, .2).
# Train, val, test
splitfolders.ratio(input_folder, 
                   output="malaria_split", 
                   seed=42, 
                   ratio=(.8, .1, .1), 
                   group_prefix=None) 