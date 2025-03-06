
My First Project - v2 2025-03-06 10:37am
==============================

This dataset was exported via roboflow.com on March 6, 2025 at 1:38 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 967 images.
Objects are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Randomly crop between 0 and 25 percent of the image
* Random rotation of between -45 and +45 degrees
* Random shear of between -15° to +15° horizontally and -14° to +14° vertically
* Random brigthness adjustment of between -23 and +23 percent
* Random exposure adjustment of between -13 and +13 percent
* Random Gaussian blur of between 0 and 3.9 pixels
* Salt and pepper noise was applied to 1.65 percent of pixels


