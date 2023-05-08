import os
import monai
import tempfile
import subprocess
from monai.apps.utils import download_and_extract
from monai.bundle.config_parser import ConfigParser
from monai.data.utils import decollate_batch
from monai.handlers.mlflow_handler import MLFlowHandler
from monai.config.deviceconfig import print_config
from monai.visualize.utils import blend_images

from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from skimage.measure import marching_cubes
import numpy as np

import torch

async def segmentation_unest():
    runInferenceCommand = [
        'python', '-m', 'monai.bundle', 'run', 'evaluating',
        '--meta_file', './configs/metadata.json',
        '--config_file', './configs/inference.json',
        '--logging_file', './configs/logging.conf'
    ]

    return subprocess.run(runInferenceCommand, check=True, capture_output=True, text=True)
