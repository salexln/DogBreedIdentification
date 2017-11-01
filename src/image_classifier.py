import os
from scipy import misc

class ImageClassifier(object):

    def __init__(self, train_dir):
        self._train_dir = train_dir

    def _image_to_rgb(self, image):
        rgb = misc.imread(image)
        # print rgb


    def _prepare_data(self):
        files = os.listdir(self._train_dir)
        for data_file in files:
            self._image_to_rgb(image=os.path.join(self._train_dir,  data_file))

    def train(self):
        print 'Training'
        self._prepare_data()

    def test(self):
        print 'Testing'