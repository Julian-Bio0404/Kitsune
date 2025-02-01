from fastapi import FastAPI


app = FastAPI()


@app.get('/club-chat')
async def hello_world():
    """Render club chat template."""
    return {"message": "Hello World!"}
