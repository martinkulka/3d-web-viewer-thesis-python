import os
import shutil
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fast_marching import fast_marching_segmentation

app = FastAPI()

origins = ["http://localhost/", "http://localhost:5173/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/fast_marching/")
async def segment_using_fast_marching(input_file: UploadFile = File(...), seed: str = Form(...)):
    input_file_name = "input.nii.gz"
    file_path = os.path.join(os.getcwd(), input_file_name)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(input_file.file, f)

    seed_tuple =  tuple(int(coordinate) for coordinate in seed.split(" "))

    fast_marching_segmentation(input_file_name, input_file_name, 1.0, -0.5, 3.0, 100, 110, [seed_tuple])

    return FileResponse(input_file_name, media_type="application/x-gzip", filename="modified_image.nii.gz")