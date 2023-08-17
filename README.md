# maldetect

  This program is used to detect if a cell is infected with malaria or not. As, you may already know, humans make lots of errors whether, its math or just what we see. What our program does is transfer the job of detecting malaria from people to computers. This makes the process easier for humans, with the benefit of almost always higher accuracy. This program could prove very useful in medical fields and in places less developed, which could use my program to diagnos many cells at a time.

![This image is showing, the program doing its job and seeing that the image of the cell has malaria]
(https://github.com/Boupai/maldetect/assets/66483875/ab04dba4-28f9-4e16-9eb8-e8464de3e248)

## The Algorithm

The algorithm is working to classify a cell as infected or uninfected. The algorithm does this by being trained by many pictures of parasitized and uninfected pictures of cells, which is classified before by a human, so the computer can correctly classify the image. This whole process is done before putting in new images in, so the computer can learn what malaria looks like, before making a decision.  There were only two options for the computer to chose as a cell either has malaria or does not.

## Running this project

1. Install Python3 and setup the Jetson Infrence library to your system
2. Install resnet and googlenet(sudo apt-get install libpython3-dev python3-numpy)
3. Find your dataset, by collecting you own pictures or, by finding them online. I used Kagle, to find my dataset. Try to find one with at least 2 categories, so your program can see which category it is instead of only giving it one option.
4. Download it and if you must unzip it. I used https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria?select=cell_images
5. Then create a folder for your new dataset(and name it), and create 3 more folders called, "test", "train", and "val".
6. Then create more folders inside of them with each name of the category, for example for the infected pictures I named the folder Parasitized, and create a folder for every single category in your dataset, with a name that corresponds to the data inside of it.
7. Create a labels.txt file in the folder with all the dataset, and list the catergories.
8. You may then go to the docker using, make sure you are in the jetson-inference
   ```
   $./docker/run.sh
   ```
9. You may then train the program, make sure you move to the classification folder cd jetson-inference/python/training/classification
    ```
     $python3 train.py --model-dir=models/(what you want the file to be called) data/(what you nameds the folder for 
     your dataset)
   ```
10. Then onnx export the script
   ```
   $ python3 onnx_export.py --model-dir=models/(what you named the model)
   ```
  11. Exit the docker and make sure you are in jetson-inference/python/training/classification
12. Set the NET and DATASET variables
13. test an image
   ```  
   $ model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/<Name of Category 1>/.jpg .jpg
   ```
14. See if it worked by finding the image you outputed.

[Video explination](https://youtu.be/FEoWe28eWvs)
