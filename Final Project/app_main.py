
# #import classes
# #import requests


from typing import Optional

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from classes import Athlete


app = FastAPI()

templates = Jinja2Templates(directory="templates")

athlete = Athlete("temp", 0, "temp", "temp", "temp", "temp")


@app.get("/")
def welcome(request: Request, name: Optional[str] = None, zipcode: Optional[int] = None , clothes: Optional[str] = None , gen_clothes: Optional[str] = None, shoes: Optional[str] = None ,\
    exercise: Optional[str] = None ):
  
    return templates.TemplateResponse("set_athlete.html", {"request": request, "name": name, "zipcode": zipcode, \
        "clothes": clothes, "gen_clothes": gen_clothes, "shoes": shoes, "exercise": exercise})
    
@app.post("/submission")
def submission_confirmation(request: Request, name: str = Form(...), zipcode: int = Form(...), clothes: str = Form(...), gen_clothes: str = Form(...), shoes: str = Form(...), exercise: str = Form(...)):
    
    global athlete
    athlete = Athlete(name, zipcode, shoes, clothes, gen_clothes, exercise)

    if exercise == "running":
        return templates.TemplateResponse("running_distance.html", {"request": request})
    elif exercise == "swimming":
        return templates.TemplateResponse("swimming_distance.html", {"request": request})
    elif exercise == "cycling":
        return templates.TemplateResponse("cycling_distance.html", {"request": request})
    elif exercise == "triathlon":
        return templates.TemplateResponse("triathlon_distance.html", {"request": request})
    elif exercise == "weightlifting":
        return templates.TemplateResponse("weightlifting_additional.html", {"request": request})
    elif exercise =="yoga":
        return templates.TemplateResponse("yoga_additional.html", {"request": request})
    else:
        raise ValueError


#RUNNER METHODS

@app.get("/runner_distance")
def runner_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("running_distance.html", {"request": request})

@app.post("/runner")
def runner(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)

    return templates.TemplateResponse("runner_control.html", {"request": request})

@app.get("/runner")
def runner(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("runner_control.html", {"request": request})


@app.get(f'/runner/find_plan', response_class=HTMLResponse)
def runner_find_plan(): 

    text, link = athlete.exercise.find_plan()

    return f"""
    <html
    <body>
        {text}
    </body>
    <br>
    <br>
    <form action='{link}' target="_blank">
    <input type="submit" value="Offsite Training Plan" />
    </form>
    <br>
    <br>
    <form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """
    

@app.get('/runner/find_equipment', response_class=HTMLResponse)
def runner_find_equipment():

    lst = athlete.exercise.find_equipment(athlete)

    return f"""
    <html>
    <h1>
    Here are some local shops that sell running shoes near you.
    </h1>
    <body>
        <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
    </body>
    <h1>
    You can also check out Amazon for options online
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+running+shoes+size+{athlete.shoes}&ref=nb_sb_noss_2" target="_blank">Shoes on Amazon</a></b>
        <br>
        <br>
    </body>
    <form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """


@app.get('/runner/find_events', response_class=HTMLResponse)
def runner_find_events():

    url = athlete.exercise.find_events(athlete)

    return f"""
    <html>
    <h1>
     <u><b><a href= "{url}" target="_blank">Click Here to Find Upcoming Races In Your Area</a></b></u>

    <br><br>
    <br><form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """


@app.get('/runner/find_books', response_class=HTMLResponse)
def runner_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    Here are some books on running that might inspire you:
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[2][1]}" target="_blank">{books[2][0]}</a></b></u>
         <br>{books[2][2]}
    </body>

    <br><br>
    <br><form action='/runner'>
    <input type="submit" value="Back To Runner Options" />
    </form>
    </html>
    """


#Swimmer METHODS

@app.get("/swimmer_distance")
def swimmer_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("swimmer_distance.html", {"request": request})

@app.post("/swimmer")
def swimmer(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)

    return templates.TemplateResponse("swimmer_control.html", {"request": request})

@app.get("/swimmer")
def swimmer(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("swimmer_control.html", {"request": request})

@app.get('/swimmer/find_plan', response_class=HTMLResponse)
def swimmer_find_plan(): 


    text, link = athlete.exercise.find_plan()

    return f"""
    <html
    <body>
        {text}
    </body>
    <br>
    <br>
    <form action='{link}' target="_blank">
    <input type="submit" value="Offsite Training Plan" />
    </form>
    <br>
    <br>
    <form action='/swimmer'>
    <input type="submit" value="Back To Swimmer Options" />
    </form>
    </html>
    """

@app.get('/swimmer/find_equipment', response_class=HTMLResponse)
def swimmer_find_equipment():

    return f"""
    <html>
    <h1>
    Swim Suits
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+competitive+swim+suits+{athlete.clothes}&ref=nb_sb_noss" target="_blank">Suits on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    Goggles
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k=swim+goggles+competitive&crid=32YJIV94RJNIO&sprefix=swim+goggles+compe%2Caps%2C169&ref=nb_sb_ss_ts-doa-p_1_18" target="_blank">Goggles on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    Swim Caps
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k=Swim+Caps&ref=nb_sb_noss_2" target="_blank">Swim Caps on Amazon</a></b>
        <br>
        <br>
    </body>
     <h1>
    Training Extras
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k=swim+accessories+for+lap+swimming&crid=LSFIQRMWDXLR&sprefix=Swim+ac%2Caps%2C165&ref=nb_sb_ss_ts-doa-p_3_7" target="_blank">Training Accessories on Amazon</a></b>
        <br>
        <br>
    </body>
    <form action='/swimmer'>
    <input type="submit" value="Back To Swimmer Options" />
    </form>
    </html>
    """

@app.get('/swimmer/find_facilities', response_class=HTMLResponse)
def swimmer_find_facilities():

    lst = athlete.exercise.find_facilities(athlete)

    return f"""
    <html>
    <h1>
    Here are some gyms that seem to have pools.
    </h1>
    <body>
        <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
    </body>
    <br>
    <form action='/swimmer'>
    <input type="submit" value="Back To Swimmer Options" />
    </form>
    </html>
    """


@app.get('/swimmer/find_books', response_class=HTMLResponse)
def swimmer_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    Here are some books on swimming that might inspire you:
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[2][1]}" target="_blank">{books[2][0]}</a></b></u>
         <br>{books[2][2]}
    </body>

    <br><br>
    <br><form action='/swimmer'>
    <input type="submit" value="Back To Swimmer Options" />
    </form>
    </html>
    """



#Cyclist METHODS

@app.get("/cycling_distance")
def cyclist_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("cycling_distance.html", {"request": request})

@app.post("/cyclist")
def cyclist(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)
    
    return templates.TemplateResponse("cyclist_control.html", {"request": request})

@app.get("/cyclist")
def cyclist(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("cyclist_control.html", {"request": request})

@app.get('/cyclist/find_plan', response_class=HTMLResponse)
def cyclist_find_plan(): 


    text, link = athlete.exercise.find_plan()

    return f"""
    <html
    <body>
        {text}
    </body>
    <br>
    <br>
    <form action='{link}' target="_blank">
    <input type="submit" value="Offsite Training Plan" />
    </form>
    <br>
    <br>
    <form action='/cyclist'>
    <input type="submit" value="Back To Cyclist Options" />
    </form>
    </html>
    """

@app.get('/cyclist/find_equipment', response_class=HTMLResponse)
def cyclist_find_equipment():

    lst = athlete.exercise.find_equipment(athlete)

    return f"""
    <html>
    <h1>
    Picking out a bike is best done in person. Here are some local Bike Shops near you.
    </h1>
    <body>
        <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
    </body>
    <h1>
    Here are some helmets on Amazon
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+helments&ref=nb_sb_noss_2" target="_blank">Helmets on Amazon</a></b>
        <br>
        <br>
    </body>
     <h1>
    Here are Cycling Shoes on Amazon
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+shoes+size+{athlete.shoes}&ref=nb_sb_noss_1" target="_blank">Shoes on Amazon</a></b>
        <br>
        <br>
    </body>
    <form action='/cyclist'>
    <input type="submit" value="Back To Cyclist Options" />
    </form>
    </html>
    """

@app.get('/cyclist/find_facilities', response_class=HTMLResponse)
def cylist_find_facilities():

    lst = athlete.exercise.find_facilities(athlete)

    return f"""
    <html>
    <h1>
    Here are some places near you that may have Spin Classes.
    </h1>
    <body>
        <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
    </body>
    <br>
    <form action='/cyclist'>
    <input type="submit" value="Back To Cyclist Options" />
    </form>
    </html>
    """

@app.get('/cyclist/find_books', response_class=HTMLResponse)
def cyclist_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    Here are some books on cyling that might inspire you:
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>

    <br><br>
    <br><form action='/cyclist'>
    <input type="submit" value="Back To Cyclist Options" />
    </form>
    </html>
    """

#Triathlete METHODS

@app.get("/triathlon_distance")
def triathlete_distance(request: Request, distance: Optional[str] = None):

    return templates.TemplateResponse("triathlete_distance.html", {"request": request})

@app.post("/triathlete")
def triathlete(request: Request, distance: str = Form(...) ):

    athlete.exercise.set_distance(distance)
    
    return templates.TemplateResponse("triathlete_control.html", {"request": request})

@app.get("/triathlete")
def triathlete(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("triathlete_control.html", {"request": request})

@app.get('/triathlete/find_plan', response_class=HTMLResponse)
def triathlete_find_plan(): 


    text, link = athlete.exercise.find_plan()

    return f"""
    <html
    <body>
        {text}
    </body>
    <br>
    <br>
    <form action='{link}' target="_blank">
    <input type="submit" value="Offsite Training Plan" />
    </form>
    <br>
    <br>
    <form action='/triathlete'>
    <input type="submit" value="Back To Triathlete Options" />
    </form>
    </html>
    """

@app.get('/triathlete/find_equipment', response_class=HTMLResponse)
def triathlete_find_equipment():

    run_lst, bike_lst = athlete.exercise.find_equipment(athlete)

    return f"""
    <html>
    <h1>
    Here are some local shops that sell running shoes near you.
    </h1>
    <body>
        <b><a href= "https://{run_lst[0][1]}" target="_blank">{run_lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{run_lst[1][1]}" target="_blank">{run_lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{run_lst[2][1]}" target="_blank">{run_lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{run_lst[3][1]}" target="_blank">{run_lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{run_lst[4][1]}" target="_blank">{run_lst[4][0]}</a></b>
    </body>
    <h1>
    You can also check out Amazon for shoe options online
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+running+shoes+size+{athlete.shoes}&ref=nb_sb_noss_2" target="_blank">Shoes on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    Picking out a bike is best done in person. Here are some local Bike Shops near you.
    </h1>
    <body>
        <b><a href= "https://{bike_lst[0][1]}" target="_blank">{bike_lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{bike_lst[1][1]}" target="_blank">{bike_lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{bike_lst[2][1]}" target="_blank">{bike_lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{bike_lst[3][1]}" target="_blank">{bike_lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{bike_lst[4][1]}" target="_blank">{bike_lst[4][0]}</a></b>
    </body>
    <h1>
    Here are some helmets on Amazon
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+helments&ref=nb_sb_noss_2" target="_blank">Helmets on Amazon</a></b>
        <br>
        <br>
    </body>
     <h1>
    Here are Cycling Shoes on Amazon
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+cycling+shoes+size+{athlete.shoes}&ref=nb_sb_noss_1" target="_blank">Shoes on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    Here are Swim Suits on Amazon
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+competitive+swim+suits+{athlete.clothes}&ref=nb_sb_noss" target="_blank">Suits on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    Here are Goggles on Amazon
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k=swim+goggles+competitive&crid=32YJIV94RJNIO&sprefix=swim+goggles+compe%2Caps%2C169&ref=nb_sb_ss_ts-doa-p_1_18" target="_blank">Goggles on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    Here are Swim Caps on Amazon
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k=Swim+Caps&ref=nb_sb_noss_2" target="_blank">Swim Caps on Amazon</a></b>
        <br>
        <br>
    </body>
     <h1>
    Here are some Swim training extras
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k=swim+accessories+for+lap+swimming&crid=LSFIQRMWDXLR&sprefix=Swim+ac%2Caps%2C165&ref=nb_sb_ss_ts-doa-p_3_7" target="_blank">Training Accessories on Amazon</a></b>
        <br>
        <br>
    </body>
    <form action='/triathlete'>
    <input type="submit" value="Back To Triathlete Options" />
    </form>
     </html>
    """
    

@app.get('/triathlete/find_facilities', response_class=HTMLResponse)
def triathlete_find_facilities():

    swim_lst, bike_lst = athlete.exercise.find_facilities(athlete)

    return f"""
    <html>
    <h1>
    Here are some places near you that may have Spin Classes.
    </h1>
    <body>
        <b><a href= "https://{bike_lst[0][1]}" target="_blank">{bike_lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{bike_lst[1][1]}" target="_blank">{bike_lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{bike_lst[2][1]}" target="_blank">{bike_lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{bike_lst[3][1]}" target="_blank">{bike_lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{bike_lst[4][1]}" target="_blank">{bike_lst[4][0]}</a></b>
    </body>
    <br>
    <h1>
    Here are some gyms that seem to have pools.
    </h1>
    <body>
        <b><a href= "https://{swim_lst[0][1]}" target="_blank">{swim_lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{swim_lst[1][1]}" target="_blank">{swim_lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{swim_lst[2][1]}" target="_blank">{swim_lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{swim_lst[3][1]}" target="_blank">{swim_lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{swim_lst[4][1]}" target="_blank">{swim_lst[4][0]}</a></b>
    </body>
    <br>
    <form action='/triathlete'>
    <input type="submit" value="Back To Triathlete Options" />
    </form>
    </html>
    """

@app.get('/triathlete/find_events', response_class=HTMLResponse)
def triathlete_find_events():

    url = athlete.exercise.find_events(athlete)

    return f"""
    <html>
    <h1>
     <u><b><a href= "{url}" target="_blank">Click Here to Find Upcoming Races In Your Area</a></b></u>

    <br><br>
    <br><form action='/triathlete'>
    <input type="submit" value="Back To Triathlete Options" />
    </form>
    </html>
    """

@app.get('/triathlete/find_books', response_class=HTMLResponse)
def triathlete_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    Here are some books on Triathlons that might inspire you:
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>

    <br><br>
    <br><form action='/triathlete'>
    <input type="submit" value="Back To Triathlete Options" />
    </form>
    </html>
    """

#WeightLifter METHODS

@app.get("/weightlifter_additional")
def weightlifter_additional(request: Request, weight: Optional[str] = None, budget: Optional[str] = None):

    return templates.TemplateResponse("weightlifter_additional.html", {"request": request})

@app.post("/weightlifter")
def weightlifter(request: Request, weight: str = Form(...), budget: str = Form(...)):

    athlete.exercise.set_additional(weight, budget)
    
    return templates.TemplateResponse("weightlifter_control.html", {"request": request})

@app.get("/weightlifter")
def weightlifter(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("weightlifter_control.html", {"request": request})

@app.get('/weightlifter/find_plan', response_class=HTMLResponse)
def weightlifter_find_plan(): 

    if athlete.exercise.weight == "bodyweight":
        one, two, three = athlete.exercise.find_plan()
        str = f"""
                <html
                <body>
                {one[0]}
                </body>
                <br>
                <br>
                <form action='{one[1]}' target="_blank">
                <input type="submit" value="Six-Week Beginners Plan" />
                </form>
                <br>
                <br>
                <body>
                    {two[0]}
                </body>
                <br>
                <br>
                <form action='{two[1]}' target="_blank">
                <input type="submit" value="Plan with Video Examples" />
                </form>
                <br>
                <br>
                <body>
                {three[0]}
                </body>
                <br>
                <br>
                <form action='{three[1]}' target="_blank">
                <input type="submit" value="Collection of Bodyweight Exercises" />
                </form>
                <br>
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                </html>
                """
    elif athlete.exercise.weight == "highrep" or athlete.exercise.weight == "heavy":
        text, link = athlete.exercise.find_plan()
        str = f"""
                <html
                <body>
                {text}
                </body>
                <br>
                <br>
                <form action='{link}' target="_blank">
                <input type="submit" value="Offsite Training Plan" />
                </form>
                <br>
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                </html>
                """
    else:
        str = f"""
        <form action='/'>
        <input type="submit" value="Start Over!" />
        </form>
        """
    
    return str

@app.get('/weightlifter/find_equipment', response_class=HTMLResponse)
def weightlifter_find_equipment():

    if athlete.exercise.budget == "100":
        top_text, one, two = athlete.exercise.find_equipment()
        str = f"""
                <html>
                <h1>
                {top_text}
                </h1>
                <body>
                    <b><a href= "{one[1]}" target="_blank">{one[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{two[1]}" target="_blank">{two[0]}</a></b>
                </body>
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                """
    elif athlete.exercise.budget == "200":
        top_text, one, two, three = athlete.exercise.find_equipment()
        str = f"""
                <html>
                <h1>
                {top_text}
                </h1>
                <body>
                    <b><a href= "{one[1]}" target="_blank">{one[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{two[1]}" target="_blank">{two[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{three[1]}" target="_blank">{three[0]}</a></b>
                </body>
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                """
    elif athlete.exercise.budget == "500":
        top_text, one, two, three, four = athlete.exercise.find_equipment()
        str = f"""
                <html>
                <h1>
                {top_text}
                </h1>
                <body>
                    <b><a href= "{one[1]}" target="_blank">{one[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{two[1]}" target="_blank">{two[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{three[1]}" target="_blank">{three[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{four[1]}" target="_blank">{four[0]}</a></b>
                </body>
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                """
    elif athlete.exercise.budget == "1000":
        top_text, one, two, three, four, five, six = athlete.exercise.find_equipment()
        str = f"""
                <html>
                <h1>
                {top_text}
                </h1>
                <body>
                    <b><a href= "{one[1]}" target="_blank">{one[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{two[1]}" target="_blank">{two[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{three[1]}" target="_blank">{three[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{four[1]}" target="_blank">{four[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{five[1]}" target="_blank">{five[0]}</a></b>
                </body>
                <br>
                <body>
                    <b><a href= "{six[1]}" target="_blank">{six[0]}</a></b>
                </body>
                <br>
                <form action='/weightlifter'>
                <input type="submit" value="Back To Weightlifter Options" />
                </form>
                """
    else:
        str = f"""
        <form action='/'>
        <input type="submit" value="Start Over!" />
        </form>
        """
    return str
  
@app.get('/weightlifter/find_books', response_class=HTMLResponse)
def weightlifter_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    Here are some books on weightlifting that might inspire you:
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>

    <br><br>
    <br><form action='/weightlifter'>
    <input type="submit" value="Back To Weightlifter Options" />
    </form>
    </html>
    """

@app.get('/weightlifter/find_facilities', response_class=HTMLResponse)
def weightlifter_find_facilities():

    lst = athlete.exercise.find_facilities(athlete)

    return f"""
    <html>
    <h1>
    Here are some gyms near you.
    </h1>
    <body>
        <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
    </body>
    <br>
    <form action='/weightlifter'>
    <input type="submit" value="Back To Weightlifter Options" />
    </form>
    </html>
    """

#Yogi METHODS

@app.get("/yogi_additional")
def yogi_additional(request: Request, practice: Optional[str] = None, budget: Optional[str] = None):

    return templates.TemplateResponse("yoga_additional.html", {"request": request})

@app.post("/yogi")
def yogi(request: Request, practice: str = Form(...), budget: str = Form(...)):

    athlete.exercise.set_additional(practice, budget)
    return templates.TemplateResponse("yogi_control.html", {"request": request})

@app.get("/yogi")
def yogi(request: Request, response_class=HTMLResponse):
    
    return templates.TemplateResponse("yogi_control.html", {"request": request})


@app.get("/yogi/find_plan", response_class=HTMLResponse)
def yogi_find_plan():

    vid1, vid2, vid3, web1, web2 = athlete.exercise.find_plan()
    
    return f"""
            <html>
            <h1>
            Here are some routines on Youtube you can follow along with:
            </h1>
            <body>
            <b><a href= "{vid1[1]}" target="_blank">Courtesy of the {vid1[0]} channel</a></b>
            <br>
             <br>
             <b><a href= "{vid2[1]}" target="_blank">Courtesy of the {vid2[0]} channel</a></b>
            <br>
             <br>
             <b><a href= "{vid3[1]}" target="_blank">Courtesy of the {vid3[0]} channel</a></b>
            <br>
            <h1>
            Here are some links to sights with a collection of poses, for when you begin create your own routines!
            </h1>
            <form action='{web1[1]}' target="_blank">
            <input type="submit" value="{web1[0]}" />
            </form>
            <br>
            <br>
            <form action='{web2[1]}' target="_blank">
            <input type="submit" value="{web2[0]}" />
            </form>
            <br>
            <br>
            <form action='/yogi'>
            <input type="submit" value="Back To Yogi Options" />
            </form>
            </html>
            """

@app.get('/yogi/find_equipment', response_class=HTMLResponse)
def yogi_find_equipment():

    return f"""
    <html>
    <h1>
    Yoga Mats
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k=yoga+mat&ref=nb_sb_noss_1" target="_blank">Yoga Mats on Amazon</a></b>
        <br>
        <br>
    </body>
    <h1>
    You can practice Yoga in anything loose and comfortable, but if you feel you need to look the part, you can find some clothing below:
    </h1>
    <body>
        <b><a href= "https://www.amazon.com/s?k={athlete.gen_clothes}+yoga+clothes+size+{athlete.clothes}&ref=nb_sb_noss" target="_blank">Yoga Attire on Amazon</a></b>
        <br>
        <br>
    </body>
    
    <form action='/yogi'>
    <input type="submit" value="Back To Yogi Options" />
    </form>
    </html>
    """

@app.get('/yogi/find_books', response_class=HTMLResponse)
def yogi_find_books():

    books = athlete.exercise.find_books()

    return f"""
    <html>
    <h1>
    Here are some books on Yoga that might inspire you:
    </h1>
    <body>
        <u><b><a href= "{books[0][1]}" target="_blank">{books[0][0]}</a></b></u>
         <br>{books[0][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[1][1]}" target="_blank">{books[1][0]}</a></b></u>
         <br>{books[1][2]}
    </body>
    <body>
        <br>
        <br><u><b><a href= "{books[2][1]}" target="_blank">{books[2][0]}</a></b></u>
         <br>{books[2][2]}
    </body>

    <br><br>
    <br><form action='/yogi'>
    <input type="submit" value="Back To Yogi Options" />
    </form>
    </html>
    """

@app.get('/yogi/find_facilities', response_class=HTMLResponse)
def yogi_find_facilities():

    lst = athlete.exercise.find_facilities(athlete)

    return f"""
    <html>
    <h1>
    Here are some yoga studios near you.
    </h1>
    <body>
        <b><a href= "https://{lst[0][1]}" target="_blank">{lst[0][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[1][1]}" target="_blank">{lst[1][0]}</a></b>
    </body>
    <body>
        <br><b><a href= "https://{lst[2][1]}" target="_blank">{lst[2][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[3][1]}" target="_blank">{lst[3][0]}</a></b>
    </body>
    <body>
       <br> <b><a href= "https://{lst[4][1]}" target="_blank">{lst[4][0]}</a></b>
    </body>
    <br>
    <form action='/yogi'>
    <input type="submit" value="Back To Yogi Options" />
    </form>
    </html>
    """

@app.get('/yogi/find_events', response_class=HTMLResponse)
def yogi_find_events():

    url = athlete.exercise.find_events()

    return f"""
    <html>
    <h1>
     <u><b><a href= "{url}" target="_blank">Click Here to Find Upcoming Retreats Across The Country!</a></b></u>

    <br><br>
    <br><form action='/yogi'>
    <input type="submit" value="Back To Yogi Options" />
    </form>
    </html>
    """