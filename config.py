#%%

parent_directory = ''

#%%

root_directory = '/home/shalini'

#%%

parent_directory = root_directory+'/car-person-detection'

# project_directory = parent_directory+'/Pinterest_BB_Data_Creation'



# dataframe_directory = project_directory+'/dataframes'


datasets_directory = parent_directory+'/datasets'


dataset_name = 'car-person'
yoloData_directory = datasets_directory+'/'+dataset_name

yoloData_images_directory = yoloData_directory+'/images'
yoloData_label_directory = yoloData_directory+'/labels'

# yoloData_all_images_directory = yoloData_images_directory+'/all_images'
yoloData_images_train_directory = yoloData_images_directory+'/train'
yoloData_images_val_directory = yoloData_images_directory+'/val'

yoloData_labels_train_directory = yoloData_label_directory+'/train'
yoloData_labels_val_directory = yoloData_label_directory+'/val'

yolo_image_size = 640
#%%

DATA_LINK = 'https://evp-ml-data.s3.us-east-2.amazonaws.com/ml-interview/openimages-personcar/trainval.tar.gz'

DATA_FILE_NAME = 'cars_persons'

# ZIP_FILE_PATH = datasets_directory+'/'+DATA_FILE_NAME+'.tar.gz'

TARGET_DOWNLOAD_FILEPATH = datasets_directory+'/'+DATA_FILE_NAME+'.tar.gz'

unzipped_data_directory = datasets_directory+'/'+DATA_FILE_NAME+'_unzipped'

all_images_directory = unzipped_data_directory+'/trainval/images'
