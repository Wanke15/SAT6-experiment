def read_single(f):
    '''
    Read single image.
    '''
    from skimage import io as skio
    rgb=skio.imread(f)
    return rgb
    
def load_batch_images(data_dir):
    '''
    Load all images in a folder and convert to numpy array, make sure all images are the same size. 
    Supports jpg and png format.
    '''
    from skimage import io as skio
    assert data_dir.endswith('/'), 'data_file should end with "/"'
    img_str = data_dir + '*.jpg' + ':' + data_dir + '*.png'
    image_collection = skio.ImageCollection(img_str, load_func=read_single)
    try:
        image_collection = skio.concatenate_images(image_collection)
    except:
        print('All image sizes are not equal, \
              return ImageCollection object instead of numpy array!!!')
    return image_collection
    