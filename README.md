# OBJECT-DETECTION-USING-YOLOV5
Training a model to detect cars and persons in an image. 

--------------------------------------------------------------------------------------------

## Overview
* We have a **dataset** and we need to train an object detector to predict labels & bounding boxes for 2 classes.
* The model chosen should have ***high Mean Average Precision (mAP for boxes)*** & ***accuracy(classification of labels) & speed***
* The model chosen is **YoloV5**.

--------------------------------------------------------------------------------------------

## Model Overview
* YOLO an acronym for 'You only look once', is an object detection algorithm that divides images into a grid system. Each cell in the grid is responsible for detecting objects within itself.
* YOLO is one of the most famous object detection algorithms due to its speed and accuracy. **YoloV5** is used to train the model.

## YOLO v5 Model Architecture
*As YOLO v5 is a single-stage object detector, it has three important parts like any other single-stage object detector.*
1. Model Backbone
2. Model Neck
3. Model Head

* Model Backbone is mainly used to extract important features from the given input image. In YOLO v5 the CSP (Cross Stage Partial Networks) are used as a backbone to extract rich in informative features from an input image.
* Model Neck is mainly used to generate feature pyramids. Feature pyramids help models to generalized well on object scaling. It helps to identify the same object with different sizes and scales. Feature pyramids are very useful and help models to perform well on unseen data. In YOLO v5 PANet is used for as neck to get feature pyramids.
* The model Head is mainly used to perform the final detection part. It applied anchor boxes on features and generates final output vectors with class probabilities, objectness scores, and bounding boxes.
* In YOLO v5 the Leaky ReLU activation function is used in middle/hidden layers and the sigmoid activation function is used in the final detection layer.
* In YOLO v5, the default optimization function for training is SGD.

--------------------------------------------------------------------------------------------

## Assumptions
* The distribution is balanced. If there are very less number of bounding boxes for any class, then it will not produce a very accurate model.
* The bounding boxes are drawn with a consistent pattern, i.e., the padding for each box drawn is same when scaled.

--------------------------------------------------------------------------------------------

## Framework
* I chose to use [YOLOv5](https://github.com/ultralytics/yolov5) as it eases the training process using the transfer learning on COCO dataset. Moreover, [YOLOv5 outperforms](https://towardsdatascience.com/detecting-objects-in-urban-scenes-using-yolov5-568bd0a63c7) all the other models like SSD as an object-detector.	

--------------------------------------------------------------------------------------------


## Preprocessing Stage

* There were two things as inputs 1) Annotations Json 2) Images folder
* I preprocessed the dataset in the format required by the Yolo standards.
* Please refer to the [Train Custom Data](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data) for detailed understanding.
* Rather than shuffling and splitting the dataset in a traditional 75-25 or 80-20 train-test split, I randomly picked 100 images out of the total 2239 available images as a validation set.
* In YOLOv5 the dataset directory is made in a specific way, with training and validation images stored seperately, and output/labels for each image are stored in the labels directory with the **.txt** extension.(if no objects in image, no **.txt** file is required). The **.txt** file specifications are:
1. One row per object
2. Each row is class x_center y_center width height format.
3. Box coordinates must be in normalized xywh format (from 0 - 1). If your boxes are in pixels, divide x_center and width by image width, and y_center and height by image height.
4. Class numbers are zero-indexed (start from 0). 


--------------------------------------------------------------------------------------------

## Training
* A YOLOv5l model pretrained on COCO128 was used to apply transfer learning, by specifying the custom dataset, batch-size, image size. (Weights can be randomly initialized --weights '' --cfg yolov5s.yaml). Pretrained weights are auto-downloaded from the latest YOLOv5 release.

* Please refer to the [Colab Training Jupyter Notebook](https://github.com/shalini-ds/OBJECT-DETECTION-USING-YOLOV5/commit/52912abeaf64fc05827167aa84725a9756528b4b)
* Ultralytics YOLOv5 public repo was cloned and all the dependencies were set up.

## Inference Code
--------------------------------------------------------------------------------------------

* After training following is the report obtained from evaluation on ***VALIDATION SET***.


## Observations
* Since the free version of colab has limited threshold for inactivity as well as limited compute time, the model trained for ***10 epochs***. As expected, the performance deteriorates on unseen intersections, but the quality of the detection remains excellent to the human eye, as shown below for the small model. With the ***IoU threshold of 0.5*** the model achieved an **mAP:75%** The model did draw very nice bounding boxes, but for higher IoU thresholds, mAP as well as the clasification precision can be improved.
* False positives can definitely be improved with further training.
* The follwoing image represents the image status is the status obtained on the <br />



## Output on the Validation Set from the [output Images folder](https://github.com/keshavgarg139/car-person-detection/tree/main/predictions)
* The format on the bounding boxes is (label, confidence)
* The IoU threshold was set as 0.5 as the model was trained for a very small amount of time, and mAP of 74.5% was achieved.
