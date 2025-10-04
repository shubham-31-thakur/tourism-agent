# from fastapi import FastAPI, Form, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from agent import route_query  # your routing function

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/", response_class=HTMLResponse)
# async def get_response(request: Request, user_query: str = Form(...)):
#     # Call your routing function (Tourism/Travel)
#     agent_response = route_query(user_query)
#     return templates.TemplateResponse("index.html", {"request": request, "response": agent_response})

# from fastapi import FastAPI, Form, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from agent import tourism_agent

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/", response_class=HTMLResponse)
# async def get_response(
#     request: Request, 
#     user_query: str = Form(...), 
#     agent_prompt: str = Form(...)
# ):
#     if not agent_prompt.strip():
#         # default prompt if user leaves it blank
#         agent_prompt = """
#         You are a Tourism Agent specialized in Indian cities.
#         Answer queries about tourist attractions, entry fees, timings, and highlights from your knowledge base.
#         Respond clearly in short JSON or text format depending on the user query.
#         """

#     response = tourism_agent(user_query, agent_prompt)
    
#     return templates.TemplateResponse(
#         "index.html", 
#         {"request": request, "response": response, "agent_prompt": agent_prompt}
#     )

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from agent import route_query

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def get_response(
    request: Request, 
    user_query: str = Form(...), 
    agent_prompt: str = Form(None)
):
    response = route_query(user_query, agent_prompt)
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "response": response, "agent_prompt": agent_prompt}
    )
