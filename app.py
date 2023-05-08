import os
import shutil
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fast_marching import fast_marching_segmentation
from utils import get_seeds_from_seed_string
from segmentation_unest import segmentation_unest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

input_file_name = "input.nii.gz"
segmentation_file_name = "segmentation.nii.gz"


@app.put("/api/set_input_file")
async def set_input_file(input_file: UploadFile = File(...)):
    file_path = os.path.join(os.getcwd(), input_file_name)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(input_file.file, f)

    return "received"


@app.get("/api/input_file.nii.gz")
async def get_input_file():
    return FileResponse(
        input_file_name, media_type="application/gzip", filename="input_file.nii.gz"
    )


@app.post("/api/fast_marching/")
async def segment_using_fast_marching(
    sigma: str = Form(...),
    alpha: str = Form(...),
    beta: str = Form(...),
    time_threshold: str = Form(...),
    stopping_time: str = Form(...),
    seeds: str = Form(...),
):
    sigma_float = float(sigma)
    alpha_float = float(alpha)
    beta_float = float(beta)
    time_threshold_int = int(time_threshold)
    stopping_time_int = int(stopping_time)
    seeds_separated = get_seeds_from_seed_string(seeds)

    fast_marching_segmentation(
        input_file_name,
        segmentation_file_name,
        sigma_float,
        alpha_float,
        beta_float,
        time_threshold_int,
        stopping_time_int,
        seeds_separated,
    )

    return "segmented successfuly"


@app.get("/api/segmentation.nii.gz")
async def get_segmentation():
    return FileResponse(
        segmentation_file_name,
        media_type="application/gzip",
        filename="segmentation.nii.gz",
    )


@app.post("/api/wholebrain_unest/")
async def segment_brain_unest():
    result = await segmentation_unest();

    return "wholebrain_unest successful"
