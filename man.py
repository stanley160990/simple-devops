from fastapi import FastAPI, File, UploadFile, Form, Response, Depends, HTTPException, status
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse

import uvicorn
import subprocess
import shlex

app = FastAPI()


# Update Firmware

@app.post("/firmware")
async def firmware():
    try:
        directory = "/opt/frimware"
        command = "git pull"
        args = shlex.split(command)

        subprocess.run(args, cwd=directory, capture_output=True, text=True)

        return {'error': False, 'message': "Firmware telah di update"}
    except:
        return {'error': True, 'message': 'firmware gagal di update'}

@app.post("/firmware-restart")
async def firmware():
    try:
        directory = "/opt/software"
        command = "reboot"
        args = shlex.split(command)

        subprocess.run(args, cwd=directory, capture_output=True, text=True)

        return {'error': False, 'message': "Firmware telah di reboot"}
    except:
        return {'error': True, 'message': 'firmware gagal di reboot'}
    

@app.post("/firmware-shutdown")
async def firmware():
    try:
        directory = "/opt/software"
        command = "shutdown now"
        args = shlex.split(command)

        subprocess.run(args, cwd=directory, capture_output=True, text=True)

        return {'error': False, 'message': "Firmware telah di shutdown"}
    except:
        return {'error': True, 'message': 'firmware gagal di shutdown'}


@app.post("/container-up")
async def composer_up():
    try:
        directory = "/opt/firmware"
        command = "docker-compose up -d"
        args = shlex.split(command)

        subprocess.run(args, cwd=directory, capture_output=True, text=True)

        return {'error': False, 'message': "Container telah diupdate"}
    except:
        return {'error': True, 'message': "Container Gagal diupdate"}

@app.get('/firmware')
async def firmware_version():
    return "wow"

# Restart Firmware
@app.post("/container-restart")
async def container_restart():
    try:
        directory = "/opt/firmware"
        command = "docker-compose restart"
        args = shlex.split(command)

        subprocess.run(args, cwd=directory, capture_output=True, text=True)

        return {'error': False, 'message': "System telah direstart"}
    except:
        return {'error': True, 'message': "System Gagal direstart"}


if __name__=="__main__":
    uvicorn.run("man:app",host='0.0.0.0', port=8000, reload=True, workers=3) 
