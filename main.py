from fastapi import FastAPI
app = FastAPI()

@app.get("/") #when a user sends a GET request to the path "/", run this function
def health_check():
	return {"status": "ok", "message": "Bank API is running"}
