import os
import shutil
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fast_marching import fast_marching_segmentation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

input_file_name = "input.nii.gz"

@app.put("/api/set_input_file")
async def set_input_file(input_file: UploadFile = File(...)):
    file_path = os.path.join(os.getcwd(), input_file_name)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(input_file.file, f)
    
    return 'received'

@app.get("/api/input_file")
async def get_input_file():
    return FileResponse(input_file_name, media_type="application/gzip", filename="current_file.nii.gz")

@app.post("/api/fast_marching/")
async def segment_using_fast_marching(seed: str = Form(...)):
    segmentation_file_name = "segmentation.nii.gz"
    seed_tuple =  tuple(int(coordinate) for coordinate in seed.split(" "))

    fast_marching_segmentation(input_file_name, segmentation_file_name, 1.0, -0.5, 3.0, 100, 110, [seed_tuple])

    return FileResponse(segmentation_file_name, media_type="application/gzip", filename="segmentation.nii.gz")