from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from os import getcwd, remove, stat
from datetime import datetime

router = APIRouter()

#function and path to upload file.
@router.post("/upload")
async def upload_file(file: UploadFile=File(...)):
    date = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    with open(getcwd() +  '/' + "factura-"+date, 'wb') as myfile:
        content = await file.read()
        myfile.write(content)
    return {'success': "factura-"+date + file.filename}


@router.get("/file/{name_file}")
def get_file(name_file: str):
    return FileResponse(getcwd() + "/" + name_file)

@router.get("/download/{name_file}")
def download_file(name_file: str):
    return FileResponse(getcwd() + "/" + name_file, media_type='application/octet-stream', filename=name_file)


@router.delete("/delete/{name_file}")
def delete_file(name_file: str):
    try:
        remove(getcwd()+ "/" + name_file)
        return JSONResponse(content=
        {"removed": True
        }, status_code=200)
    except FileNotFoundError:
        return JSONResponse(content={"removed": False, "message": "File not found"}, status_code=404)
    