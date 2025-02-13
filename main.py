from fastapi import FastAPI
 
# Create a FastAPI instance
app = FastAPI()
 
# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running on Kubernetes!"}
 
# Example endpoint with a parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
 
# Health check endpoint (useful for Kubernetes readiness and liveness probes)
@app.get("/health")
def health_check():
    return {"status": "healthy"}
