#
# created by
# Antonio Garcia-Uceda Juarez
# PhD student
# Medical Informatics
#
# created on 09/02/2018
# Last update: 09/02/2018
########################################################################################

from DataLoaders.BatchDataGenerators.BatchDataGenerator import *
from tensorflow.python.keras.utils import Sequence
import numpy as np
np.random.seed(2017)



class BatchDataGenerator_Keras(BatchDataGenerator, Sequence):

    def __init__(self, size_image,
                 list_xData_array,
                 list_yData_array,
                 images_generator,
                 num_channels_in= 1,
                 num_classes_out= 1,
                 is_outputUnet_validconvs= False,
                 size_output_image= None,
                 batch_size= 1,
                 shuffle= True,
                 seed= None,
                 iswrite_datagen_info= True):
        super(BatchDataGenerator_Keras, self).__init__(size_image,
                                                       list_xData_array,
                                                       list_yData_array,
                                                       images_generator,
                                                       num_channels_in=num_channels_in,
                                                       num_classes_out=num_classes_out,
                                                       is_outputUnet_validconvs=is_outputUnet_validconvs,
                                                       size_output_image=size_output_image,
                                                       batch_size=batch_size,
                                                       shuffle=shuffle,
                                                       seed=seed,
                                                       iswrite_datagen_info=iswrite_datagen_info)

    def __len__(self):
        return super(BatchDataGenerator_Keras, self).__len__()

    def on_epoch_end(self):
        super(BatchDataGenerator_Keras, self).on_epoch_end()

    def __getitem__(self, index):
        return super(BatchDataGenerator_Keras, self).__getitem__(index)


    def get_reshaped_output_array(self, in_array):
        return np.expand_dims(in_array, axis=-1)


    def get_formated_output_xData(self, in_array):
        return self.get_reshaped_output_array(in_array)

    def get_formated_output_yData(self, in_array):
        if self.is_outputUnet_validconvs:
            out_array = self.get_cropped_output(in_array)
        else:
            out_array = in_array
        return self.get_formated_output_xData(out_array)


    def get_item(self, index):
        (out_xData_elem, out_yData_elem) = super(BatchDataGenerator_Keras, self).get_item(index)
        return (self.get_formated_output_xData(out_xData_elem),
                self.get_formated_output_yData(out_yData_elem))