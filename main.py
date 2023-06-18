from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import Puppy

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World!"}

@app.get("/health")
def health():
    return status.HTTP_200_OK

@app.post("/new_puppy")
def new_puppy(puppy: Puppy):
    return puppy

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)