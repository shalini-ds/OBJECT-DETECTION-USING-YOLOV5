

import json
from CONFIG import *
import pandas as pd
import os

import random

from PIL import Image

from tqdm import tqdm

#%%

def create_bb_coords(x):
    top_left_x,top_left_y,width,height = x
    x1 = top_left_x
    y1 = top_left_y
    x2 = top_left_x+width
    y2 = top_left_y+height
    return [x1,y1,x2,y2]

def return_yolo_centre_width_height(x):
    top_left_x,top_left_y,width,height = x
    x1 = top_left_x
    y1 = top_left_y
    x2 = top_left_x+width
    y2 = top_left_y+height
    return {'centre_x':int((x1+x2)/2),
            'centre_y':int((y1+y2)/2),
            'width':width,
            'height':height}

#%%

def create_yolo_data(train_images_df,labels_df,yoloData_images_train_directory,yoloData_labels_train_directory):
    
    for i in tqdm(range(len(train_images_df))):
        
        #% RESIZE and SAVE IMAGE
        image_file_name = train_images_df['file_name'][i]
        img = Image.open(all_images_directory+'/'+image_file_name)
        actual_width,actual_height = img.width,img.height
        img = img.resize([yolo_image_size,yolo_image_size])
        img.save(yoloData_images_train_directory+'/'+image_file_name)
        
        image_labels_df = labels_df[labels_df['image_id']==train_images_df['image_id'][i]].reset_index(drop=True)
        
        image_labels_df['centre_x'] /= actual_width
        image_labels_df['centre_y'] /= actual_height
        image_labels_df['width'] /= actual_width
        image_labels_df['height'] /= actual_height
        
        # image_labels_df['yolov5_coords'] = image_labels_df['bbox'].apply(return_yolo_centre_width_height)
        
        image_labels_df.drop(['image_id'],axis=1,inplace=True)
        
        # SAVE THE LABEL FILE
        labels_file_name = image_file_name.replace('jpg','txt')
        image_labels_df.to_csv(yoloData_labels_train_directory+'/'+labels_file_name,header=False,index=False,sep=' ')
        
        # img2 = Image.open(all_images_directory+'/'+image_file_name).crop(create_bb_coords([846, 145, 146, 477]))
    

#%%

def create_yolov5_data():

    #%%
    with open(unzipped_data_directory+'/trainval/annotations/bbox-annotations.json') as json_file:
        data = json.load(json_file)
     
    #%%
    
    labels_df = pd.DataFrame(data['annotations'])
    
    labels_df['yolov5_coords'] = labels_df['bbox'].apply(return_yolo_centre_width_height)
    
    labels_df = pd.concat([labels_df.drop(['yolov5_coords'], axis=1), labels_df['yolov5_coords'].apply(pd.Series)], axis=1)
    
    labels_df = labels_df[['image_id','category_id','centre_x','centre_y','width','height']]
    
    labels_df['category_id'] = labels_df['category_id'].replace({2:0})
    
    images_df = pd.DataFrame(data['images']).rename({'id':'image_id'},axis=1)
    
    #%%
    
    # if not os.path.exists(yoloData_all_images_directory):
    #     os.makedirs(yoloData_all_images_directory)
        
    if not os.path.exists(yoloData_images_train_directory):
        os.makedirs(yoloData_images_train_directory)
    
    if not os.path.exists(yoloData_images_val_directory):
        os.makedirs(yoloData_images_val_directory)
        
    if not os.path.exists(yoloData_labels_train_directory):
        os.makedirs(yoloData_labels_train_directory)
    
    if not os.path.exists(yoloData_labels_val_directory):
        os.makedirs(yoloData_labels_val_directory)    
        
    #%%
    
    random_test_indices = random.sample(range(len(images_df)),100)
    
    train_images_df = images_df[~images_df.index.isin(random_test_indices)].reset_index()
    
    val_images_df = images_df[images_df.index.isin(random_test_indices)].reset_index()

    #%%

    create_yolo_data(train_images_df,labels_df,yoloData_images_train_directory,yoloData_labels_train_directory)
    create_yolo_data(val_images_df,labels_df,yoloData_images_val_directory,yoloData_labels_val_directory)            
    #%%

