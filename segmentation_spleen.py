import subprocess
import os
from utils import get_model_path


async def segmentation_spleen(model):
    model_path = get_model_path(model)

    runInferenceCommand = [
        "python",
        "-m",
        "monai.bundle",
        "run",
        "--config_file",
        f"./monaimodels/{model}/configs/inference.json",
        "--bundle_root",
        model_path
    ]

    return subprocess.run(
        runInferenceCommand, check=True, capture_output=True, text=True
    )
