import subprocess


async def segmentation_unest():
    runInferenceCommand = [
        "python",
        "-m",
        "monai.bundle",
        "run",
        "evaluating",
        "--meta_file",
        "./configs/metadata.json",
        "--config_file",
        "./configs/inference.json",
        "--logging_file",
        "./configs/logging.conf",
    ]

    return subprocess.run(
        runInferenceCommand, check=True, capture_output=True, text=True
    )
