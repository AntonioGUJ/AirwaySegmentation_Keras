#
# created by
# Antonio Garcia-Uceda Juarez
# PhD student
# Medical Informatics
#
# created on 09/02/2018
# Last update: 09/02/2018
########################################################################################

import numpy as np
np.random.seed(2017)


FORMATINTDATA   = np.int16
FORMATSHORTDATA = np.uint8
FORMATREALDATA  = np.float32

FORMATIMAGESDATA     = FORMATINTDATA
FORMATMASKSDATA      = FORMATINTDATA
FORMATPHYSDISTDATA   = FORMATREALDATA
FORMATPROBABILITYDATA= FORMATREALDATA
FORMATFEATUREDATA    = FORMATREALDATA



# ******************** SET-UP WORKDIR ********************
DATADIR = '/home/antonio/Data/LUVAR_Processed/'
BASEDIR = '/home/antonio/Results/AirwaySegmentation_EXACT/'

# Names input and output directories
NAME_RAWIMAGES_RELPATH      = 'RawImages/'
NAME_RAWLABELS_RELPATH      = 'RawAirways/'
NAME_RAWROIMASKS_RELPATH    = 'RawLungs/'
NAME_RAWEXTRALABELS_RELPATH = 'RawCentrelines/'
NAME_REFERKEYS_RELPATH      = 'RawImages/'
NAME_PROCIMAGES_RELPATH     = 'ImagesWorkData/'
NAME_PROCLABELS_RELPATH     = 'LabelsWorkData/'
NAME_PROCEXTRALABELS_RELPATH= 'ExtraLabelsWorkData/'
NAME_CROPBOUNDINGBOX_FILE   = 'cropBoundingBoxes_images.npy'
NAME_RESCALEFACTOR_FILE     = 'rescaleFactors_images.npy'
NAME_PROCREFERKEYS_FILE     = 'referenceKeys_images.npy'
NAME_TRAININGDATA_RELPATH   = 'TrainingData/'
NAME_VALIDATIONDATA_RELPATH = 'ValidationData/'
NAME_TESTINGDATA_RELPATH    = 'TestingData/'
NAME_CONFIGPARAMS_FILE      = 'configparams.txt'
NAME_LOGDESCMODEL_FILE      = 'logdescmodel.txt'
# ******************** SET-UP WORKDIR ********************


# ******************** DATA DISTRIBUTION ********************
#PROPDATA_TRAINVALIDTEST = (0.84, 0.16, 0.0) # for EXACT
PROPDATA_TRAINVALIDTEST = (0.5, 0.14, 0.36) # for DLCST+LUVAR
# ******************** DATA DISTRIBUTION ********************


# ******************** PREPROCESS PARAMETERS ********************
SHUFFLETRAINDATA = True
NORMALIZEDATA    = False
ISBINARYTRAINMASKS = True

if ISBINARYTRAINMASKS:
    FORMATXDATA = FORMATIMAGESDATA
    FORMATYDATA = FORMATMASKSDATA
else:
    FORMATXDATA = FORMATIMAGESDATA
    FORMATYDATA = FORMATPHYSDISTDATA

MASKTOREGIONINTEREST = True

RESCALEIMAGES = False
ORDERINTERRESCALE = 3
#FIXEDRESCALERES = (0.6, 0.55, 0.55)   # for LUVAR
FIXEDRESCALERES = (0.8, 0.69, 0.69)   # for EXACT
FIXEDRESCALERES = None

CROPIMAGES = True
ISSAMEBOUNDBOXSIZEALLIMAGES = False
ISCALCBOUNDINGBOXINSLICES = False
FIXEDSIZEBOUNDINGBOX = (352, 480)

SLIDINGWINDOWIMAGES = False
PROPOVERLAPSLIDINGWINDOW_Z_X_Y = (0.25, 0.0, 0.0)
PROPOVERLAPSLIDINGWINDOW_TESTING_Z_X_Y = (0.5, 0.5, 0.5)

RANDOMCROPWINDOWIMAGES = True
NUMRANDOMIMAGESPERVOLUMEEPOCH = 8

TRANSFORMATIONRIGIDIMAGES = True
ROTATION_XY_RANGE = 10
ROTATION_XZ_RANGE = 5
ROTATION_YZ_RANGE = 5
HEIGHT_SHIFT_RANGE = 24
WIDTH_SHIFT_RANGE = 35
DEPTH_SHIFT_RANGE = 7
HORIZONTAL_FLIP = True
VERTICAL_FLIP = True
AXIALDIR_FLIP = True
ZOOM_RANGE = 0.25
FILL_MODE_TRANSFORM = 'reflect'

TRANSFORMELASTICDEFORMIMAGES = False
TYPETRANSFORMELASTICDEFORMATION = 'gridwise'
# ******************** PREPROCESS PARAMETERS ********************


# ******************** TRAINING PARAMETERS ********************
TYPE_DNNLIBRARY_USED = 'Pytorch'
TYPEGPUINSTALLED     = 'larger_GPU'

#(IMAGES_DEPTHZ, IMAGES_HEIGHT, IMAGES_WIDTH) = (176, 352, 240)
#(IMAGES_DEPTHZ, IMAGES_HEIGHT, IMAGES_WIDTH) = (256, 256, 256) # for Non-valid convolutions
(IMAGES_DEPTHZ, IMAGES_HEIGHT, IMAGES_WIDTH) = (252, 252, 252) # for Valid convolutions
#(IMAGES_DEPTHZ, IMAGES_HEIGHT, IMAGES_WIDTH) = (452, 252, 364) # try large images
IMAGES_DIMS_Z_X_Y = (IMAGES_DEPTHZ, IMAGES_HEIGHT, IMAGES_WIDTH)

IMODEL       = 'Unet'
NUM_LAYERS   = 5
NUM_FEATMAPS = 16

TYPE_NETWORK         = 'classification'
TYPE_ACTIVATE_HIDDEN = 'relu'
TYPE_ACTIVATE_OUTPUT = 'sigmoid'
TYPE_PADDING_CONVOL  = 'same'
DISABLE_CONVOL_POOLING_LASTLAYER = False
ISUSE_DROPOUT        = False
ISUSE_BATCHNORMALIZE = False
TAILORED_BUILD_MODEL = True

NUM_EPOCHS = 1000
BATCH_SIZE = 1
IOPTIMIZER = 'Adam'
LEARN_RATE = 8.0e-05
ILOSSFUN   = 'DiceCoefficient'
LISTMETRICS = []
#LISTMETRICS = ['DiceCoefficient', 'TruePositiveRate', 'FalsePositiveRate', 'TrueNegativeRate', 'FalseNegativeRate']

NUMMAXTRAINIMAGES = 50
NUMMAXVALIDIMAGES = 15

ISVALIDCONVOLUTIONS = True
USEVALIDATIONDATA = True
FREQVALIDATEMODEL = 3
FREQSAVEINTERMODELS = 5
USETRANSFORMONVALIDATIONDATA = True

USEMULTITHREADING = False
WRITEOUTDESCMODELTEXT = False

# GNN-module parameters
ISTESTMODELSWITHGNN = False
SOURCEDIR_ADJS 	  = 'StoredAdjacencyMatrix/'
ISGNNWITHATTENTIONLAYS = False
# ******************** TRAINING PARAMETERS ********************


# ******************** RESTART PARAMETERS ********************
RESTART_MODEL = False
RESTART_EPOCH = 0
RESTART_ONLY_WEIGHTS = False
RESTART_FROMFILE = True
RESTART_FROMDIFFMODEL = False
# ******************** RESTART PARAMETERS ********************


# ******************** PREDICTION PARAMETERS ********************
PREDICTONRAWIMAGES = False
SAVEFEATMAPSLAYERS = False
NAMESAVEMODELLAYER = 'convU12'
FILTERPREDICTPROBMAPS = False
PROP_VALID_OUTUNET = 0.75
# ******************** PREDICTION PARAMETERS ********************


# ******************** POST-PROCESSING PARAMETERS ********************
LISTRESULTMETRICS = ['DiceCoefficient',
                     'AirwayCompleteness',
                     'AirwayVolumeLeakage',
                     'AirwayCompletenessModified',
                     'AirwayCentrelineLeakage',
                     'AirwayCentrelineFalsePositiveDistanceError',
                     'AirwayCentrelineFalseNegativeDistanceError']

THRESHOLDPOST = 0.5
ATTACHTRACHEAPREDICTION = False
REMOVETRACHEARESMETRICS = True

LISTMETRICSROCCURVE = ['DiceCoefficient',
                       'AirwayCompleteness',
                       'AirwayVolumeLeakage',
                       'AirwayCentrelineFalsePositiveDistanceError',
                       'AirwayCentrelineFalseNegativeDistanceError']
# ******************** POST-PROCESSING PARAMETERS ********************
