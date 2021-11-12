
# #import classes
# #import requests


from typing import Optional

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from classes import Athlete

# class Athlete_JSON(BaseModel):
#     name: str
#     zipcode: int
#     clothes: str
#     shoes: str
#     exercise: str

app = FastAPI()

templates = Jinja2Templates(directory="templates")

athlete = Athlete("temp", 0, "temp", "temp", "temp")



@app.get("/")
def welcome(request: Request, name: Optional[str] = None, zipcode: Optional[int] = None , clothes: Optional[str] = None , shoes: Optional[str] = None ,\
    exercise: Optional[str] = None ):
  
    return templates.TemplateResponse("set_athlete.html", {"request": request, "name": name, "zipcode": zipcode, \
        "clothes": clothes, "shoes": shoes, "exercise": exercise})
    
@app.post("/submission")
def submission_confirmation(request: Request, name: str = Form(...), zipcode: int = Form(...), clothes: str = Form(...), shoes: str = Form(...), exercise: str = Form(...)):
    
    global athlete
    athlete = Athlete(name, zipcode, shoes, clothes, exercise)

    if exercise == "running":
        return templates.TemplateResponse("running_distance.html", {"request": request})
    else:
        return templates.TemplateResponse("page1.html", {"request": request})


#RUNNER METHODS

@app.get("/runner_distance")
def runner_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("running_distance.html", {"request": request})

@app.post("/runner")
def runner(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)

    return templates.TemplateResponse("runner_control.html", {"request": request})

@app.get("/runner")
def runner(request: Request):

    return templates.TemplateResponse("runner_control.html", {"request": request})


#NEEDS
    #find plan
@app.get('/runner/find_plan/', response_class=HTMLResponse)
def runner_find_plan(request: Request):

    source, link = athlete.exercise.find_plan()

    return f"""
    <html>
    <body>

        <img alt="{athlete.exercise.distance}" src={link}
        width="500" height="500">
    </body>

    <h1>
        {source}
    </h1>
    <form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """

# @app.get('/runner/get_books')

@app.get('/runner/find_equipment', response_class=HTMLResponse)
def runner_find_equipment(request: Request):

    lst = athlete.exercise.find_equipment(athlete)

    return f"""
    <html>
    <body>
        <b><a href= https://{lst[0][1]}>{lst[0][0]}</a></b>
    </body>
    <form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """

# @app.___('/runner/find_facilities')
# #@app.___('/runner/find_groups') #I think I'm going to get rid of this functionality
# @app.___('/runner/find_events')




