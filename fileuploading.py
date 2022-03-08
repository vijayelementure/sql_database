from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile=File(...)):
    return {"filename": file.filename}
