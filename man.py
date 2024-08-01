from fastapi import FastAPI, File, UploadFile, Form, Response, Depends, HTTPException, status
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse

import uvicorn
import subprocess
import shlex

app = FastAPI()


# Update Firmware

@app.post("/firmware")

async def firmware_update():
    cmd = 'docker-compose up --force-recreate',
    try:
        directory = "/opt/firmware"
        command = "docker compose up -d"
        args = shlex.split(command)

        subprocess.run(args, cwd=directory, capture_output=True, text=True)

        return {'error': False, 'message': "System telah diupdate"}
    except:
        return {'error': True, 'message': "System Gagal diupdate"}

@app.get('/firmware')

async def firmware_version():
    return "wow"

# Restart Firmware
@app.post("/restart")

async def firmware_update():
    cmd = 'docker-compose restart',
    try:
        directory = "/opt/firmware"
        command = "docker compose restart"
        args = shlex.split(command)

        subprocess.run(args, cwd=directory, capture_output=True, text=True)

        return {'error': False, 'message': "System telah direstart"}
    except:
        return {'error': True, 'message': "System Gagal direstart"}



if __name__=="__main__":
    uvicorn.run("API:app",host='0.0.0.0', port=8000, reload=True, workers=3) 