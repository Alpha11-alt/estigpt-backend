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

app = FastAPI()

class EstimateRequest(BaseModel):
    job_description: str

@app.post("/estimate")
async def generate_estimate(request: EstimateRequest):
    result = simple_estimator(request.job_description)
    return {"estimate": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
