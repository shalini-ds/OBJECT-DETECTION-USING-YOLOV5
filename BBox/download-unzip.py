
import os

from CONFIG import DATA_LINK,datasets_directory,TARGET_DOWNLOAD_FILEPATH,unzipped_data_directory

import urllib.request

#%%

def download_and_unzip():

    if not os.path.exists(datasets_directory):
        os.makedirs(datasets_directory)
    
    urllib.request.urlretrieve(DATA_LINK,TARGET_DOWNLOAD_FILEPATH)
    
    #%%
    
    import tarfile
      
    # open file
    file = tarfile.open(TARGET_DOWNLOAD_FILEPATH)
      
    # extracting file
    file.extractall(unzipped_data_directory)
      
    file.close()

#%%