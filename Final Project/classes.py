import requests
from fastapi import FastAPI


class Exercise():

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def find_plan():
        pass

    def find_equipment():
        pass

    def find_books():
        pass

    def find_facilities():
        pass

    def find_groups():
        pass

    def find_events():
        pass

class Running (Exercise):

    def __init__(self):

        super().__init__()



    def __repr__(self):
       return f"Running, {self.distance}"

    def set_distance(self, distance):
        self.distance = distance

    #Return Plan based on Race Distance
    def find_plan(self):

        if self.distance == "mile":
            return "Courtesy of the Harlem 1 Miler organization", "https://static1.squarespace.com/static/587fa2b36a49633c1bea89b7/t/58eff7081e5b6c95575800c9/1492121353190/One+Miler+Training+Plan.pdf"
        elif self.distance == "5k":
            return "Courtesy of the Mayo Clinic", "https://www.mayoclinic.org/documents/fsm14-5k-run-pdf/doc-20086108"
        elif self.distance == "10k":
            return "Courtesy of the Ortho Carolina organization", "https://www.orthocarolina.com/storage/wysiwyg/orthocarolina_10k_training_plan_-_beginner.pdf"
        elif self.distance == "halfmarathon":
            return "Courtesy of verywellfit.com", "https://files.verywellfit.com/Training+Plans/12+Week+Beginner+Half+Marathon+Training+Plan+.pdf"
        elif self.distance == "marathon":
            return "Courtesy of verywellfit.com", "https://files.verywellfit.com/Training+Plans/22+Week+Beginner+Marathon+Training+Plan+.pdf"
        elif self.distance == "ultramarathon":
            return "Courtesy of podiumrunner.com","https://www.podiumrunner.com/wp-content/uploads/2012/11/46_nat_r1.pdf"

     #Just Shoes
    def find_equipment(self, athlete):

        url = "https://www.yelp.com/search/snippet?find_desc=running%20shoes&find_loc="+str(athlete.zipcode)+"&request_origin=user"

        response = requests.get(url)
        response_data = response.json()
        searchPageProps = response_data['searchPageProps']
        consumerHeaderProps = searchPageProps['mainContentComponentsListProps']

        lst = []
        for i in range(3,8):
            cur_dict = consumerHeaderProps[i]
            lst.append((f'Store Name: {cur_dict.get("searchResultBusiness").get("name")}', \
            f'yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}'))
        
        return lst

#     #Have some queued up, others depending on distance
#     def find_books():

#         #Born to Run: https://www.amazon.com/Born-Run-Hidden-Superathletes-Greatest/dp/0307279189/ref=sr_1_5?keywords=Books+on+Running&qid=1636644863&qsid=140-5700113-7714932&sr=8-5&sres=0307279189%2C1465489576%2C0936070854%2C014312319X%2C0578230437%2C1937715418%2C0345528808%2C1579659888%2CB073Z4CXFZ%2C1609618025%2CB09K1WVDJ3%2C1609619196%2C0764207598%2C1733527303%2CB078PMQPH7%2C0593231716%2C1782551654%2C1482046628%2C161448242X%2C1635651832&srpt=ABIS_BOOK
#         #The Ultimate Beginner's Running Guide: https://www.amazon.com/Ultimate-Beginners-Running-Guide-Inspired/dp/1482046628/ref=sr_1_1_sspa?crid=3U9F0SUS8KV2T&keywords=books+on+running+for+beginners&qid=1636644926&sprefix=Books+on+Running+for+%2Caps%2C173&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyV1VBODRXMFg2QU5EJmVuY3J5cHRlZElkPUEwODczMjE1MjQxQUVOR0lZM1FNTiZlbmNyeXB0ZWRBZElkPUEwNjMxMDMyM0ZFVzJGQlpOSk1IMSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=
#         #What I Talk About When I Talk About Running: https://www.amazon.com/dp/B0015DWJ8W/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1

#         pass

#     #A silly message about looking outside
#     def find_facilities():

#         return ("May we suggest looking outside? The open road is the only facility you'll need!")

#     #Return local running groups
#     def find_groups():
#         pass

#     #racefinder
#     def find_events():
#         pass

# class Swimming(Exercise):
#     def __init__(self, distance):
#         super().__init__()
#         self.distance = distance

#     def __repr__(self):
#         return super().__repr__()

#     #Return Plan based on Race Distance
#     def find_plan():
#         pass

#     #Swim suits based on clothing size, goggles, swim caps
#     def find_equipment():
#         pass

#     #Have some queued up, others depending on distance
#     def find_books():
#         pass

#     #Find local lap pools
#     def find_facilities():

#         # response = requests.get('https://www.yelp.com/search/snippet?find_desc=gym%20pools&find_loc=60615&request_origin=user')
#         # response_data = response.json()
#         # searchPageProps = response_data['searchPageProps']
#         # consumerHeaderProps = searchPageProps['mainContentComponentsListProps']

#         # for i in range(3,8):
#         #     cur_dict = consumerHeaderProps[i]
#         #     print(f'Gym Name: {cur_dict.get("searchResultBusiness").get("name")}, \
#         #     Gym URL: yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}')
#         pass

#     #Maybe master's swim teams?
#     def find_groups():
#         pass

#     #racefinder
#     def find_events():
#         pass

# class Cycling(Exercise):

#     def __init__(self, distance):
#         super().__init__()
#         self.distance = distance

#     def __repr__(self):
#         return super().__repr__()

#     #Return Plan based on Race Distance
#     def find_plan():
#         pass

#     #Direct People to local bike shops
#     def find_equipment():

#         ###Finding Bike Shops Near You###
#         ##https://www.bikeflights.com/bicycleshops

#         # response = requests.get("https://www.bikeflights.com/api/BikeShops/getShopsNear?latitude=41.8003921&longitude=-87.603826&range=25&units=m")
#         # response_data = response.json()


#         # print("Buying a bycle is best done in person. Here are five bike shops within 25 miles of you:")
#         # print('------------')

#         # for i in range(0,5):
#         #     cur_dict = response_data[i].get("ShipLocation")
#         #     print(f'Shop Name: {cur_dict.get("label")}')
#         #     print(f'Shop Address: {cur_dict.get("address1")}, {cur_dict.get("city")} {cur_dict.get("state")}')
#         #     print(f'Shop Website: {cur_dict.get("website")}')
#         #     print('------------')
#         pass

#     #Have some queued up
#     def find_books():
#         pass

#     #Return spinning locations
#     def find_facilities():
#         pass

#     #Return kocal cycling groups
#     def find_groups():
#         pass

#     #racefinder
#     def find_events():
#         pass

# class Triathlon(Running, Swimming, Cycling): #Might actually want to inherit from 

#     def __init__(self):
#         super().__init__()

#     def __repr__(self):
#         return super().__repr__()

#     def set_distance(self, distance):
#         if distance.lower().strip() not in ['sprint', 'olympic', 'halfironman', 'ironman']:
#             raise ValueError
#         else:
#             self.distance = distance.lower().strip()

#     #Return Plan based on Race Distance
#     def find_plan():
#         pass

#     #Would like to be able to call all three Super methods within
#     def find_equipment():
#         pass

#     #Have some queued up, others depending on distance
#     def find_books():
#         pass

#     #Would like to call Cycling and Swimming Super methods within
#     def find_facilities():
#         pass

#     #Return triathlon groups
#     def find_groups():
#         pass

#     #racefinder
#     def find_events():
#         pass

# class Weight_Lifting(Exercise):

#     def __init__(self):
#         pass

#     def __repr__(self):
#         pass

#     #Sets the kind of lifting
#     def lifting_type(self, weight):

#         if weight.lower().strip() not in ['heavy', 'highrep', 'bodyweight']:
#             raise ValueError
#         else:
#             self.weight = weight.lower().strip()

#     #return based on type of lifting
#     def find_plan():
#         pass

#     #return based on type of lifting
#     def find_equipment():
#         pass

#     #return based on type of lifting
#     def find_books():
#         pass

#     def find_facilities():
#         pass

#     #Unsure if there will be groups for this
#     def find_groups():
#         pass

#     #No events, just pump!
#     def find_events():
#         pass

# class Yoga(Exercise):

#     def __init__(self):
#         pass

#     def __repr__(self):
#         pass
    
#     #return a few different routines from a few different styles of Yoga
#     def find_plan():
#         pass

#     #Really just a mat and clothing
#     def find_equipment():
#         pass

#     #Some books on the physicality, others on meditation, origins of Yoga
#     def find_books():
#         pass

#     #Yoga studios
#     def find_facilities():
#         pass

#     #Outdoor/free yoga meet-ups
#     def find_groups():
#         pass

#     #Maybe Yoga retreats?
#     def find_events(self, athlete):
#         pass
    
# #Gotta think a bit more about what this looks like
# class Cross_Training(Exercise):
#     def __init__(self):
#         pass

#     def __repr__(self):
#         pass

#     def find_plan():
#         pass

#     def find_equipment():
#         pass

#     def find_books():
#         pass

#     def find_facilities():
#         pass

#     def find_groups():
#         pass

#     def find_events():
#         pass


class Athlete():


    def __init__(self, name, zipcode, shoes, clothes, exercise):
        self.name = name
        self.shoes = shoes
        self.clothes = clothes
        self.zipcode = zipcode
        self.exercise = Running()


#         stripped_string = exercise.lower().strip()
#         #checks to make sure it's an exceptable exercise:
#         if stripped_string not in ['running', 'cycling', 'swimming', 'triathlon', 'weightlifting', 'yoga', 'crosstraining']:
#             raise ValueError
#         else:
#             if stripped_string == 'running':
#                 self.exercsise = Running()
#             elif stripped_string == 'cycling':
#                 self.exercsise = Cycling()
#             elif stripped_string == 'swimming':
#                 self.exercsise = Swimming()
#             elif stripped_string == 'triathlon':
#                 self.exercsise = Triathlon()
#             elif stripped_string == 'weightlifting':
#                 self.exercsise = Weight_Lifting()

        

    def __repr__(self):
        # if self.exercise == "Running" or self.exercise == "cycling" or self.exercise == "triathlon":
        #     s =  s = f'Name: {self.name}, Shoe Size: {self.shoes}, Clothing Size: {self.clothes}, Zipcode: {self.zipcode}, Exercise: {self.exercise}, Distance = {self.distance}'
        # else:
        s = f'Name: {self.name}, Shoe Size: {self.shoes}, Clothing Size: {self.clothes}, Zipcode: {self.zipcode}, Exercise: {self.exercise}'
        return s
