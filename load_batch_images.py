from skimage import io as skio
#skimage.__version__ == '0.13.0'

def read_single(f):
    '''
    Read single image.
    '''
    img=skio.imread(f)
    return img
    
def load_batch_images(data_dir):
    '''
    Load all images in a folder and convert to numpy array, 
    Note: make sure all images are the same size. 
    Supports jpg and png format.
    '''
    assert data_dir.endswith('/'), 'data_file should end with "/"'
    img_str = data_dir + '*.jpg' + ':' + data_dir + '*.png'
    image_collection = skio.ImageCollection(img_str, load_func=read_single)
    try:
        image_collection = skio.concatenate_images(image_collection)
    except:
        print('''All image sizes are not equal, \
              return ImageCollection object instead of numpy array!!!''')
    return image_collection
    
