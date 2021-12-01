README FINAL


GETTING STARTED

Ensure that you download the entirety of thee "Final Project", which contains files app_main.py,
classes.py, Pipfile, Pipfile.lock, and a subfolder called Templates. All of those files are needed for
this app to run, so be sure they are all there.

This app is reliant on a the Pipenv virtual environment tool. Please be sure you have it installed on your
machine. If it it not, you can read how to install it here:

https://pipenv.pypa.io/en/latest/

Once you've ensure this step is complete and indexed into the "Final Project" Folder, initiate the virtual
environment with the following command:

$ pipenv shell


Once the shell has been launched, enter the following command to launch the app:

$ hypercorn app_main:app

This should result in a message along the lines of "Running on http://127.0.0.1:8000". Copy and paste that
URL into your browser.


USING THE APP

The app is quite straightforward. Enter all requested information on the landing page. Zipcode is
restricted to inputs consisting of 5 numeric characters. Regardless of which exercise is chosen, once you
submit the first form, you will be brought to a page that asks for you to select some additional,
exercise-specific information. Select this and submit.

At this point, you will land on the exercise-specific page of the site. There will be some collection of
the following functionalities: "Find a Training Plan", "Find Equipment", "Find Books", "Find Facilities",
"Find Events". The specifics of which appear will be determined by which exercise you choose. For example,
there is no "Find Facilities" option for Running, and no "Find Events" option for Cycling, Swimming, or
Weightlifting.

The Training Plan returned will be dependent on the distance goals (Running, Swimming, Cycling, Triathlon)
or exercise type (Yoga, Weightlifting). There will be a hyperlink out to various sites on the Internet
where these plans can be found.

The Equipment that is returned will be based on your inputs to the previous forms, such as your shoe and
clothing sizes, gender category of clothing, and, in the case of Weightlifting, the budget. Hyperlinks to
all of these buying options will be included. In the event that you may need to buy equipment in a store
(running shoes, a bicycle), local shops near your zipcode will be displayed with hyperlinks to their Yelp
reviews.

The Books that are returned are specific to each exercise, but identical for all variations of a given
exercise. In other words, regardless of your aforementioned distance goals for exercise type, you will be
recommended the same books on your exercise. The page will display the book titles, the authors, and blurb
for the book, and a hyperlink to a site to buy a copy.

Find Facilities is tied exclusively to the zipcode that has been input. The results returned are based on
a Yelp search of the appropriate facilities (i.e. Spin Studios for Cycling, Gyms with Pools for Swimming,
etc). The names of the businesses will be displayed, with a hyperlink to their Yelp review pages.

The Events that a returned for the race-based exercises (Running, Triathlon) will be based on the user's
zip code and the distance they've chosen. The Events for Yoga are retreats across the country that cost
less than the budget specified by the user. A hyperlink is included to a site with a comprehensive list of
these events. 


FINAL NOTE/CHANGES FROM ORIGINAL PROPOSAL

My original proposal include one more function for the exercises: Find_Groups. Unfortunately, my app is
heavily reliant on other sites that house the content needed by our users. I was unable to find sites that
helped with the search, and creating a database of these groups was outside the scope of this project, as
that would essentially be a final product in its own right. 

Similarly, though Swimming and Cycling may have benefitted from a Find_Events function, the sites that
were available invariably returned lackluster (and oftentimes unusable) results. With this in mind, I
decided to exclude this function for these two events.

