import os
# from scipy import misc
import csv
import cv2
from sklearn.neighbors import KNeighborsClassifier

class ImageClassifier(object):

    def __init__(self, train_dir, labels, test_dir):
        self._train_dir = train_dir
        self._labels_path = labels
        self._train_data = {}
        self._train_labels = []
        self._train_features = []
        self._model = None
        self._test_dir = test_dir
        self._test_data = {}

    # def _image_to_rgb(self, image):
    #     rgb = misc.imread(image)
    #     return rgb

    def _image_to_feature_vector(self, image_path):
        size = (32, 32)
        image = cv2.imread(image_path)
        return cv2.resize(image, size).flatten()

    def _add_labes_to_train_data(self):
        with open(self._labels_path , 'r') as labels_csv:
            csv_reader = csv.reader(labels_csv)
            csv_reader.next()

            for row in csv_reader:
                if row[0] in self._train_data:
                    self._train_data[row[0]]['label'] = row[1]
                else:
                    print 'Label does not exists'

    def _get_data_and_labels(self):
        for k, v in self._train_data.iteritems():
            self._train_features.append(v['data'])
            self._train_labels.append(v['label'])

    def _prepare_data(self):
        files = os.listdir(self._train_dir)
        for data_file in files:
            features = self._image_to_feature_vector(image_path=os.path.join(self._train_dir,  data_file))
            file_name = data_file.split('.')[0]
            self._train_data[file_name] = {}
            self._train_data[file_name]['data'] = features

        self._add_labes_to_train_data()

        self._get_data_and_labels()

    def _prepare_test_data(self):
        files = os.listdir(self._test_dir)
        for data_file in files:
            # import pdb; pdb.set_trace()
            try:
                features = self._image_to_feature_vector(image_path=os.path.join(self._test_dir, data_file))
                file_name = data_file.split('.')[0]
                self._test_data[file_name] = {}
                self._test_data[file_name]['data'] = features
            except:
                pass

    def train(self):
        print 'Training'
        self._prepare_data()
        self._run_knn()

    def _run_knn(self):
        self._model = KNeighborsClassifier(n_neighbors=3)
        self._model.fit(self._train_features, self._train_labels)


    def test(self):
        print 'Testing'
        self._prepare_test_data()

        test_features = []
        for k, v in self._test_data.iteritems():
            test_features.append(v['data'])

            self._predictions = self._model.predict(test_features)

    def print_results(self):
        print self._predictions