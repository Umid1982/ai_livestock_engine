from fastapi import FastAPI

app = FastAPI(
    title="AI Livestock Engine",
    version="0.1.0"
)


@app.get("/")
def root():
    return {"message": "AI Livestock Engine is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
