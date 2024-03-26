from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
import pytz

app = FastAPI()

# CORS configuration to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Convert the current time to Beijing time
    beijing_tz = pytz.timezone('Asia/Shanghai')
    date_time_bj = datetime.now(beijing_tz)

    # Format the date and time in the desired format (YYYYMMDD_HHMM)
    date_str = date_time_bj.strftime("%Y%m%d_%H%M")

    # Determine the size of the file
    file.file.seek(0, os.SEEK_END)  # Seek to end of file
    file_size = file.file.tell()  # Get the file size
    file.file.seek(0, 0)  # Seek back to the start of the file

    # Add the date, time, and file size to the filename with 'BJT' suffix
    filename = f"{date_str}_BJT_{file_size}_{file.filename}"

    # Define the location to save the file
    file_location = f"/media/yiyun/seagate/Timeline/{filename}"

    # Write the file in chunks to the specified location
    with open(file_location, "wb") as buffer:
        for data in iter(lambda: file.file.read(1024 * 1024), b""):  # 1 MB chunks
            buffer.write(data)

    return {"filename": filename}


