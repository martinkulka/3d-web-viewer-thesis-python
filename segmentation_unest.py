import subprocess
import os
from utils import get_model_path


async def segmentation_unest(model):
    model_path = get_model_path(model)
    metadata_path = os.path.join(os.getcwd(), "monaimodels", "wholeBrainSeg_Large_UNEST_segmentation", "configs", "metadata.json")
    inference_path = os.path.join(os.getcwd(), "monaimodels", "wholeBrainSeg_Large_UNEST_segmentation", "configs", "inference.json")
    logging_path = os.path.join(os.getcwd(), "monaimodels", "wholeBrainSeg_Large_UNEST_segmentation", "configs", "logging.conf")

    runInferenceCommand = [
        "python",
        "-m",
        "monai.bundle",
        "run",
        "evaluating",
        "--meta_file",
        f"./monaimodels/{model}/configs/metadata.json",
        "--config_file",
        f"./monaimodels/{model}/configs/inference.json",
        "--logging_file",
        f"./monaimodels/{model}/configs/logging.conf",
        "--bundle_root",
        model_path
    ]

    return subprocess.run(
        runInferenceCommand, check=True, capture_output=True, text=True
    )
