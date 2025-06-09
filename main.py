from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict
import uvicorn

# Temporary Estimation Logic
def simple_estimator(job_description: str) -> Dict:
    # Very basic logic for demo purposes
    if "ac unit" in job_description.lower():
        return {
            "total_estimate": 8200,
            "breakdown": {
                "labor": 3200,
                "materials": 4500,
                "other": 500
            },
            "timeline": "3-5 days"
        }
    else:
        return {
            "total_estimate": 5000,
            "breakdown": {
                "labor": 2000,
                "materials": 2500,
                "other": 500
            },
            "timeline": "1-2 weeks"
        }

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "EstiGPT backend is live!"}

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import openai

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "EstiGPT backend is live!"}

@app.post("/estimate")
async def estimate(file: UploadFile = File(...)):
    contents = await file.read()
    
    try:
        text = contents.decode("utf-8", errors="ignore")
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a cost estimator."},
            {"role": "user", "content": f"Estimate this:\n{text}"}
        ]
    )

    estimate = response["choices"][0]["message"]["content"]
    return JSONResponse(content={"estimate": estimate})
Added /estimate route for file uploads and AI prediction

