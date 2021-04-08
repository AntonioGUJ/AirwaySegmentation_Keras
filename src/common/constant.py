
import numpy as np
np.random.seed(2017)

DATADIR = '/home/antonio/Data/MRIenhance_GRASE2CUBE_Processed/'
# DATADIR = '/data/scratch/agarcia/Data/MRIenhance/'         # cluster
BASEDIR = '/home/antonio/Results/MRIenhanceTests/'
# BASEDIR = '/data/scratch/agarcia/Results/MRIenhanceTests/' # cluster


# NAMES INPUT / OUTPUT DIR
NAME_RAW_IMAGES_RELPATH = 'Images/'
NAME_RAW_LABELS_RELPATH = 'Labels/'
NAME_RAW_ROIMASKS_RELPATH = 'RoiMasks/'
NAME_RAW_EXTRAIMAGES_RELPATH = 'NOUSE/'
NAME_RAW_EXTRALABELS_RELPATH = 'NOUSE/'
NAME_REFERENCE_FILES_RELPATH = 'Images/'
NAME_PROC_IMAGES_RELPATH = 'ImagesWorkData/'
NAME_PROC_LABELS_RELPATH = 'LabelsWorkData/'
NAME_PROC_EXTRALABELS_RELPATH = 'ExtraLabelsWorkData/'
NAME_CROP_BOUNDBOXES_FILE = 'cropBoundingBoxes_images.npy'
NAME_RESCALE_FACTORS_FILE = 'rescaleFactors_images.npy'
NAME_REFERENCE_KEYS_PROCIMAGE_FILE = 'referenceKeys_procimages.npy'
NAME_TRAININGDATA_RELPATH = 'TrainingData/'
NAME_VALIDATIONDATA_RELPATH = 'ValidationData/'
NAME_TESTINGDATA_RELPATH = 'TestingData/'
NAME_CONFIG_PARAMS_FILE = 'configparams.txt'
NAME_DESCRIPT_MODEL_LOGFILE = 'descriptmodel.txt'
NAME_TRAINDATA_LOGFILE = 'traindatafiles.txt'
NAME_VALIDDATA_LOGFILE = 'validdatafiles.txt'
NAME_LOSSHISTORY_FILE = 'losshistory.csv'
NAME_SAVEDMODEL_EPOCH_KERAS = 'model_e%0.2d.hdf5'
NAME_SAVEDMODEL_LAST_KERAS = 'model_last.hdf5'
NAME_SAVEDMODEL_EPOCH_TORCH = 'model_e%0.2d.pt'
NAME_SAVEDMODEL_LAST_TORCH = 'model_last.pt'
NAME_TEMPO_POSTERIORS_RELPATH = 'Predictions/PosteriorsWorkData/'
NAME_POSTERIORS_RELPATH = 'Predictions/Posteriors/'
NAME_REFERENCE_KEYS_POSTERIORS_FILE = 'Predictions/referenceKeys_posteriors.npy'
NAME_PRED_RESULT_METRICS_FILE = 'Predictions/result_metrics.csv'


# PREPROCESSING
IS_BINARY_TRAIN_MASKS = False
IS_MASK_REGION_INTEREST = False
IS_NORMALIZE_DATA = False
IS_CROP_IMAGES = False
IS_RESCALE_IMAGES = False
IS_SHUFFLE_TRAINDATA = True
IS_MERGE_TWO_IMAGES_AS_CHANNELS = False


# DATA AUGMENTATION IN TRAINING
IS_SLIDING_WINDOW_IMAGES = False
PROP_OVERLAP_SLIDING_WINDOW = (0.5, 0.5, 0.5)
IS_RANDOM_WINDOW_IMAGES = False
NUM_RANDOM_PATCHES_EPOCH = 8
IS_TRANSFORM_RIGID_IMAGES = True
TRANS_ROTATION_XY_RANGE = 0
TRANS_ROTATION_XZ_RANGE = 0
TRANS_ROTATION_YZ_RANGE = 0
TRANS_HEIGHT_SHIFT_RANGE = 0
TRANS_WIDTH_SHIFT_RANGE = 0
TRANS_DEPTH_SHIFT_RANGE = 0
TRANS_HORIZONTAL_FLIP = True
TRANS_VERTICAL_FLIP = True
TRANS_AXIALDIR_FLIP = True
TRANS_ZOOM_RANGE = 0
TRANS_FILL_MODE_TRANSFORM = 'nearest'
IS_TRANSFORM_ELASTIC_IMAGES = False
TYPE_TRANSFORM_ELASTIC_IMAGES = 'gridwise'


# DISTRIBUTE DATA TRAIN / VALID / TEST
DIST_PROPDATA_TRAINVALIDTEST = (0.65, 0.15, 0.20)


# TRAINING MODELS
SIZE_IN_IMAGES = (288, 288, 96)
MAX_TRAIN_IMAGES = 500
MAX_VALID_IMAGES = 200
TYPE_NETWORK = 'UNet3DPlugin3levels'    # 'UNet3DPlugin5levels'
NET_NUM_FEATMAPS = 16
TYPE_OPTIMIZER = 'Adam'
LEARN_RATE = 1.0e-04
TYPE_LOSS = 'DSSIM'         # 'Perceptual' #'MultiScaleSSIM'
WEIGHT_COMBINED_LOSS = 1000.0
LAYERS_VGG16_LOSS_PERCEPTUAL = ['block1_conv1', 'block2_conv1', 'block3_conv1']
WEIGHTS_VGG16_LOSS_PERCEPTUAL = [0.65, 0.30, 0.05]
PROP_REDSIZE_VGG16_LOSS_PERCEPTUAL = 0.33
LIST_TYPE_METRICS = ['DSSIM']
BATCH_SIZE = 1
NUM_EPOCHS = 500
IS_VALID_CONVOLUTIONS = False
IS_USE_VALIDATION_DATA = True
IS_TRANSFORM_VALIDATION_DATA = True
FREQ_VALIDATE_MODEL = 1
FREQ_SAVE_INTER_MODELS = 10
IS_WRITEOUT_DESCMODEL_TEXT = False
IS_RESTART_ONLY_WEIGHTS = False
TYPE_DNNLIB_USED = 'Keras'
IS_MODEL_IN_GPU = True
IS_MODEL_HALF_PRECISION = False


# NOT USED - TRAINING MODELS
NET_NUM_LEVELS = 3
TYPE_ACTIVATE_HIDDEN = 'relu'
TYPE_ACTIVATE_OUTPUT = 'linear'
NET_IS_USE_DROPOUT = False
NET_IS_USE_BATCHNORMALIZE = False
IS_DISABLE_CONVOL_POOLING_LASTLAYER = False
IS_MULTITHREADING = False


# PREDICTIONS / POST-PROCESSING
PROP_OVERLAP_SLIDING_WINDOW_PRED = (0.5, 0.5, 0.5)
LIST_TYPE_METRICS_RESULT = ['SNR', 'PSNR', 'SSIM']
IS_FILTER_PRED_PROBMAPS = False
PROP_VALID_OUTPUT_NNET = 0.75
IS_SAVE_FEATMAPS_LAYER = False
NAME_LAYER_SAVE_FEATS = 'convU12'
