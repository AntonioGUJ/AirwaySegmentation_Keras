
DATADIR = '/home/antonio/Data/EXACT_Testing/'
BASEDIR = '/home/antonio/Results/AirwaySegmentation_EXACT/'


# NAMES INPUT / OUTPUT DIR
NAME_RAW_IMAGES_RELPATH = 'Images/'
NAME_RAW_LABELS_RELPATH = 'Airways/'
NAME_RAW_ROIMASKS_RELPATH = 'Lungs/'
NAME_RAW_COARSEAIRWAYS_RELPATH = 'CoarseAirways/'
NAME_RAW_CENTRELINES_RELPATH = 'Centrelines/'
NAME_REFERENCE_FILES_RELPATH = 'Images/'
NAME_PROC_IMAGES_RELPATH = 'ImagesWorkData/'
NAME_PROC_LABELS_RELPATH = 'LabelsWorkData/'
NAME_PROC_EXTRALABELS_RELPATH = 'CenlinesWorkData/'
NAME_CROP_BOUNDBOXES_FILE = 'cropBoundingBoxes_images.npy'
NAME_RESCALE_FACTORS_FILE = 'rescaleFactors_images.npy'
NAME_REFERENCE_KEYS_PROCIMAGE_FILE = 'referenceKeys_procimages.npy'
NAME_TRAININGDATA_RELPATH = 'TrainingData/'
NAME_VALIDATIONDATA_RELPATH = 'ValidationData/'
NAME_TESTINGDATA_RELPATH = 'TestingData/'
NAME_MODELSRUN_RELPATH = 'Models/'
NAME_LOSSHISTORY_FILE = 'losshistory.csv'
NAME_CONFIG_PARAMS_FILE = 'configparams.txt'
NAME_TRAINDATA_LOGFILE = 'traindatafiles.txt'
NAME_VALIDDATA_LOGFILE = 'validdatafiles.txt'
NAME_TEMPO_POSTERIORS_RELPATH = 'Predictions/PosteriorsWorkData/'
NAME_POSTERIORS_RELPATH = 'Predictions/Posteriors/'
NAME_PRED_BINARYMASKS_RELPATH = 'Predictions/BinaryMasks/'
NAME_PRED_CENTRELINES_RELPATH = 'Predictions/Centrelines/'
NAME_REFERENCE_KEYS_POSTERIORS_FILE = 'Predictions/referenceKeys_posteriors.npy'
NAME_PRED_RESULT_METRICS_FILE = 'Predictions/result_metrics.csv'


# PREPROCESSING
IS_BINARY_TRAIN_MASKS = True
IS_NORMALIZE_DATA = False
IS_MASK_REGION_INTEREST = True
IS_CROP_IMAGES = True
SIZE_BUFFER_BOUNDBOX_BORDERS = (20, 20, 20)
IS_TWO_BOUNDBOXES_EACH_LUNG = False
IS_SAME_SIZE_BOUNDBOX_ALL_IMAGES = False
SIZE_FIXED_BOUNDBOX_ALL = None
IS_CALC_BOUNDBOX_IN_SLICES = False
IS_RESCALE_IMAGES = False
FIXED_RESCALE_RESOL = None


# DATA AUGMENTATION IN TRAINING
IS_SLIDING_WINDOW_IMAGES = False
PROP_OVERLAP_SLIDING_WINDOW = (0.25, 0.0, 0.0)
IS_RANDOM_WINDOW_IMAGES = True
NUM_RANDOM_PATCHES_EPOCH = 8
IS_TRANSFORM_RIGID_IMAGES = True
TRANS_RIGID_ROTATION_RANGE = (10.0, 7.0, 7.0)   # (plane_XY, plane_XZ, plane_YZ)
TRANS_RIGID_SHIFT_RANGE = (0.0, 0.0, 0.0)       # (width, height, depth)
TRANS_RIGID_FLIP_DIRS = (True, True, True)      # (horizontal, vertical, axialdir)
TRANS_RIGID_ZOOM_RANGE = 0.25                   # scale between (1 - val, 1 + val)
TRANS_RIGID_FILL_MODE = 'reflect'
IS_TRANSFORM_ELASTIC_IMAGES = False
TYPE_TRANS_ELASTIC_DEFORM = 'gridwise'


# DISTRIBUTE DATA TRAIN / VALID / TEST
PROPDATA_TRAIN_VALID_TEST = (0.5, 0.15, 0.35)


# CHOOSE DL BACKEND
TYPE_DNNLIB_USED = 'Pytorch'    # 'Keras'
IS_MODEL_GPU = True
IS_MODEL_HALFPREC = False


# TRAINING MODELS
SIZE_IN_IMAGES = (252, 252, 252)
MAX_TRAIN_IMAGES = 100
MAX_VALID_IMAGES = 20
TYPE_NETWORK = 'UNet3DPlugin'
NET_NUM_FEATMAPS = 16
TYPE_OPTIMIZER = 'Adam'
LEARN_RATE = 1.0e-04
TYPE_LOSS = 'DiceCoefficient'
WEIGHT_COMBINED_LOSS = 1000.0
LIST_TYPE_METRICS = []
BATCH_SIZE = 1
NUM_EPOCHS = 1000
IS_VALID_CONVOLUTIONS = True
FREQ_SAVE_CHECK_MODELS = 2
FREQ_VALIDATE_MODELS = 2
IS_USE_VALIDATION_DATA = True
IS_TRANSFORM_VALIDATION_DATA = True
IS_SHUFFLE_TRAINDATA = True
MANUAL_SEED_TRAIN = None


# NOT USED - TRAINING MODELS
# NET_NUM_LEVELS = 5
# TYPE_ACTIVATE_HIDDEN = 'relu'
# TYPE_ACTIVATE_OUTPUT = 'sigmoid'
# NET_IS_USE_DROPOUT = False
# NET_IS_USE_BATCHNORMALIZE = False
# IS_DISABLE_CONVOL_POOLING_LASTLAYER = False
# IS_MULTITHREADING = False


# PREDICTIONS / POST-PROCESSING
PROP_OVERLAP_SLIDING_WINDOW_TEST = (0.5, 0.5, 0.5)
POST_THRESHOLD_VALUE = 0.5
IS_ATTACH_COARSE_AIRWAYS = True
IS_REMOVE_TRACHEA_CALC_METRICS = True
LIST_TYPE_METRICS_RESULT = ['DiceCoefficient',
                            'AirwayCompleteness',
                            'AirwayVolumeLeakage',
                            'AirwayCentrelineLeakage',
                            'AirwayTreeLength',
                            'AirwayCentrelineDistanceFalsePositiveError',
                            'AirwayCentrelineDistanceFalseNegativeError']
METRIC_EVALUATE_THRESHOLD = 'AirwayVolumeLeakage'
IS_FILTER_OUT_PROBMAPS_NNET = False
PROP_FILTER_OUT_PROBMAPS_NNET = 0.75
