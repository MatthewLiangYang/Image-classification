import pickle

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

label_name = ['airplane',
              'automobile',
              'bird',
              'cat',
              'deer',
              'dog',
              'frog',
              'horse',
              'ship',
              'truck']

import glob
import numpy as np
import cv2
import os

# train_list = glob.glob('/Users/liangyang/Desktop/Image classification/cifar-10-batches-py/data_batch_*')
# print(train_list)
# save_path = '/Users/liangyang/Desktop/Image classification/cifar-10-batches-py/Train'

train_list = glob.glob('/Users/liangyang/Desktop/Image classification/cifar-10-batches-py/test_batch*')
save_path = '/Users/liangyang/Desktop/Image classification/cifar-10-batches-py/Test'

for l in train_list:
    print(l)
    l_dict = unpickle(l)
    # print(l_dict)
    print(l_dict.keys())

    for im_idx, im_data in enumerate(l_dict[b'data']):
        # print(im_idx)
        # print(im_data)

        im_label = l_dict[b'labels'][im_idx]
        im_name = l_dict[b'filenames'][im_idx]

        print(im_label, im_name, im_data)

        im_label_name = label_name[im_label]
        im_data = np.reshape(im_data, [3, 32, 32])
        im_data = np.transpose(im_data, (1, 2, 0))

        # cv2.imshow('im_data', cv2.resize(im_data, (200, 200)))
        # cv2.waitKey(0)

        if not os.path.exists('{}/{}'.format(save_path, im_label_name)):
            os.mkdir('{}/{}'.format(save_path, im_label_name))

        cv2.imwrite('{}/{}/{}'.format(save_path,
                                      im_label_name,
                                      im_name.decode('utf-8')), im_data)
