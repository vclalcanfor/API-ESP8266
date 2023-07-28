import sys
from fastapi import FastAPI

sys.path.append("db")
from dbConnect  import Backend 

db = Backend()
app = FastAPI()

@app.get("/")
def testAPI():
    return {"msg": "Hello!!"}