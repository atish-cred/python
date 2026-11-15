from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Query
from client.rq_client import queue
from queues.worker import process_query

app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"status": "Hello World"}


# Chat route
@app.post("/chat")
def chat(
    query: str = Query(..., description="The chat query of user")
):
    # process_query(user_query)
    # It will return id of the job/queue
    job = queue.enqueue(process_query, query)
    return {"status": "queued", "job_id": job.id}


@app.get("/job-status")
def get_result(job_id: str = Query(..., description="The job id of the queued job")):
    job = queue.fetch_job(job_id)
    result = job.return_value()
    return {"status": "finished", "result": result} 
