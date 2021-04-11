BronchiNet - UNet-GNN method
==============================

Airway segmentation from chest CTs using a novel method as combination of the U-Net and Graph Neural Networks (GNNs). 

Contact: Antonio Garcia-Uceda Juarez (antonio.garciauceda89@gmail.com)

Introduction
------------

This software provides functionality to segment airways from CT scans, using the novel joint UNet-GNN method. The implementation of the segmentation method is described in:

Garcia-Uceda, A., Selvan, R., Saghir, Z. de Bruijne, M. A joint 3D UNet-graph neural network-based method for airway segmentation from chest CTs. Int. Work. on Mach. Learn. Med. Imaging 583–591 (2019).

If using this software influences positively your project, please cite the above paper.

This software includes tools to i) prepare the CT data to use with DL models, ii) perform DL experiments for training and testing, and iii) process the output of DL models to obtain the binary airway segmentation. The tools are entirely implemented in Python, and the UNet-GNN method is developed in Pytorch.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           	<- Makefile with commands like `make data` or `make train`
    ├── README.md          	<- The top-level README for developers using this project.
    │
    ├── docs               	<- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             	<- Trained and serialized models, model predictions, or model summaries
    │
    ├── requirements.txt   	<- The requirements file for reproducing the analysis environment, e.g.
    │                         	   generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           	<- makes project pip installable (pip install -e .) so src can be imported
    ├── src         	   	<- Source code for use in this project.
    │   │
    │   ├── common         	<- General files and utilities
    │   ├── dataloaders    	<- Modules to load data and batch generators
    │   ├── imageoperators 	<- Various image operations
    │   ├── models 	   	<- All modules to define networks, metrics and optimizers
    │   ├── plotting       	<- Various plotting modules
    │   ├── postprocessing 	<- Modules to postprocess the output of networks
    │   ├── preprocessing  	<- Modules to preprocess the images to feed to networks
    │   │
    │   ├── scripts_evalresults	<- Scripts to evaluate results from models
    │   ├── scripts_experiments	<- Scripts to train and test models
    │   ├── scripts_launch 	<- Scripts with pipelines and PBS scripts to run in clusters
    │   ├── scripts_preparedata	<- Scripts to prepare data to train models
    │   └── scripts_util	<- Scripts for various utilities
    │
    ├── tests			<- Tests to validate the method implementation (to be run locally)
    └── tox.ini            	<- tox file with settings for running tox; see tox.readthedocs.io

------------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

Requirements
------------

- python packages required are in "requirements.txt"
- cuda >= 10.2 (https://developer.nvidia.com/cuda-zone)
- cuDNN >= 7.6.5 (https://developer.nvidia.com/rdp/cudnn-download)

(Recommended to use python virtualenv)

- python -m venv <path_new_pyvenv>
- source <path_new_pyvenv>/bin/activate
- pip install -r requirements.txt

Instructions
------------

The user needs only to run the scripts provided: the python files with a 'main()' function. Each script performs a given operation, either to i) prepare data, ii) run experiments, or iii) evaluate results. Typically, the scripts take as arguments i) the path with the input files, ii) the path to store the output files, and iii) a series of optional settings that control the performed operation. All arguments are parsed to the script from the command line.

The typical way to launch the scripts is:

- python <path_script> <path_input_files> <path_output_files> --<option_arg_1>=<value> --<option_arg_2>=<value> ...

The names for the optional input arguments of the given script can be displayed by:

- python <path_script> --help

For the optional arguments that are not given in the command line, they take the default value given in the source file: "src/common/constant.py"

Create working directory
------------

- mkdir <working_dir> && cd <working_dir>
- ln -s <path_data_stored> BaseData
- ln -s <path_thiscode_stored> Code

[IF NEEDED] (include in "~/.bashrc" file: export PYTHONPATH=<path_thiscode_stored>/src/")

Prepare data
------------

1) [IF NEEDED] Preprocess data: apply various operations to input images / masks: rescaling, binarise masks
- python ./Code/scripts_util/apply_operation_images.py <path_input_files> <path_output_files> --type=[various option]

2) Compute bounding-boxes around lung masks, for input images:
- python ./Code/scripts_preparedata/compute_boundingbox_images.py --datadir=[path_dataset]

3) Prepare data: include i) crop images, ii) mask ground-truth to lung regions, iii) rescale images
- python ./Code/scripts_preparedata/prepare_data.py --datadir=[path_dataset]

Train models
------------

1) Distribute data in training / validation / testing:
- python ./Code/scripts_experiments/distribute_data.py --basedir=[path_workdir]

2) Train models:
- python ./Code/scripts_experiments/train_model.py --basedir=[path_workdir] --modelsdir=<path_output_models> [IF RESTART: --is_restart=True --in_config_file=<path_file_config>]

Test models
------------

1) Compute predictions form trained model:
- python ./Code/scripts_experiments/predict_model.py <path_trained_model> <path_output_predictions> --basedir=[path_workdir] --in_config_file=<path_file_config>

2) Compute full-size probability maps from predictions:
- python ./Code/scripts_evalresults/postprocess_predictions.py <path_output_predictions> <path_output_probmaps> --basedir=[path_workdir]

3) Compute airway binary mask from probability maps:
- python ./Code/scripts_evalresults/process_predicted_airway_tree.py <path_output_probmaps> <path_output_binmasks> --basedir=[path_workdir]
- rm -r <path_output_predictions>

4) [IF NEEDED] Compute largest connected component of airway binary masks:
- python ./Code/scripts_util/apply_operation_images.py <path_output_binmasks> <path_output_conn_binmasks> --type=firstconreg
- rm -r <path_output_binmasks> && mv <path_output_conn_binmasks> <path_output_binmasks>

5) Compute centrelines from airway binary masks:
- python ./Code/scripts_util/apply_operation_images.py <path_output_binmasks> <path_output_centrelines> --type=thinning

6) Compute results metrics / accuracy:
- python ./Code/scripts_evalresults/compute_result_metrics.py <path_output_binmasks> <path_output_centrelines> --basedir=[path_workdir]

[ALTERNATIVE] Do steps 1-6 altogether:
- python ./Code/scripts_launch/launch_predictions_full.py <path_trained_model> <path_output_predictions> --basedir=[path_workdir]
