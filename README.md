# Proposals
My idea for my final project is as follows.

1. I would like to create an API that helps introduce people into new exercising routines. I've found that starting to get into a fitness routine can be very intimidating, and I am hopeful my app will help to centralize the process.

My app will handle a select list of exercise modalities, which is currently restricted to the following: Running, Cycling, Swimming, Triathlon, Weight Lifting, Yoga, Cross-Training. It will have methods to:

- Take in one's general fitness goals and find online workout plans that might fit one (run a certain distance, do a certain type of yoga, heavy vs high rep lifting, etc). A stretch goal for this would be adding that plan to one’s Google Calendar using the Google Calender API mentioned in the Project Proposal Example, though I am unsure if I will be able to achieve this in time.
- Return a list of equipment/apparel one might need to begin exercise. If people would like to explore buying certain equipment, they can input their size and price restrictions per item and the program will return links to possible items.
- Take in a zip-code/city and return local groups (names, contact info) pertaining to that fitness routine
- Take in a zip-code and find local fitness facilities (locations, pricing if available) where one might go to workout
- Return a list of (and links to) popular books on the exercise with brief descriptions
- For race-based exercises (running, cycling, tri, etc), take in date range and zipcode to return a list of upcoming events

I will start by gathering all the different sites and data sources I will need. For example, sites like trifind.com, which can be used to find triathlon races close to a given zip code, datasets relating to zip codes that will allow me to calculate distances and restrict searches on that, and compiling my own relatively limited datasets regarding equipment for each exercise. After that, I will work on  getting the logic and methods up and running, and then work on the web searches/API integration.


My execution plan for the Project will follow this timeline:

End of Week 4: I will research and decide upon a web framework, and create a basic web app that allows the user to input their name, zipcode, shoe/clothing sizes, and desired type of exercise. I will also work to aggregate all external sites that my site will be referencing (i.e. sites to buy equipment/apparel, find gyms/pools, find races, workout plans)

End of Week 5: I will have a basic homepage, as well as classes for each type of exercise, which will include attributes for equipment/apparel of that each of the exercises, as well as writing out (but not implementing) the methods of each class.

End of Week 6: Finish writing all the methods for each class, returning stock answers for now just to ensure the logic works. I will also try to ensure I've made good progress with working out how to seach other sites based on user input and returning the results, though I may not be able to implement this week. Begin working on code for calculating adjacent zip-codes of the user.

End of Week 7: Continue figuring out how to return a specified range of search results from other websites (Amazon for materials, race websites for upcoming events, etc) and adding these external searches to the otherwise finished methods. Finish Zipcode search function. Begin work on Stretch Goal of adding workout plan/races to Google Calendar Via API.

End of Week 8: Finish external search result aspect of project. Clean up site appearance. Continue on Google Calendar stretch goal if time permits.

Final Touch-Ups: Work on User-Interface, finish any loose string, alter functionality of any methods I been unable to successfully create.


