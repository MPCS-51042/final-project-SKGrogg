import requests


##Finding Swimming Pools near you###

#url = 'https://www.yelp.com/search/snippet?find_desc=gym%20pools&find_loc=60615&request_origin=user' #specific to 60615

# response = requests.get(url)
# response_data = response.json()
# searchPageProps = response_data['searchPageProps']
# consumerHeaderProps = searchPageProps['mainContentComponentsListProps']

# for i in range(3,8):
#     cur_dict = consumerHeaderProps[i]
#     print(f'Gym Name: {cur_dict.get("searchResultBusiness").get("name")}, \
#     Gym URL: yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}')



###Finding Bike Shops Near You###
##https://www.bikeflights.com/bicycleshops

# url = "https://www.bikeflights.com/api/BikeShops/getShopsNear?latitude=41.8003921&longitude=-87.603826&range=25&units=m"

# response = requests.get(url)
# response_data = response.json()


# print("Buying a bycle is best done in person. Here are five bike shops within 25 miles of you:")
# print('------------')

# for i in range(0,5):
#     cur_dict = response_data[i].get("ShipLocation")
#     print(f'Shop Name: {cur_dict.get("label")}')
#     print(f'Shop Address: {cur_dict.get("address1")}, {cur_dict.get("city")} {cur_dict.get("state")}')
#     print(f'Shop Website: {cur_dict.get("website")}')
#     print('------------')

url = "https://www.yelp.com/search/snippet?find_desc=running%20shoes&find_loc=60615&request_origin=user"

response = requests.get(url)
response_data = response.json()
searchPageProps = response_data['searchPageProps']
consumerHeaderProps = searchPageProps['mainContentComponentsListProps']

for i in range(3,8):
    cur_dict = consumerHeaderProps[i]
    print(f'Store Name: {cur_dict.get("searchResultBusiness").get("name")}, \
    Store URL: yelp.com/{cur_dict.get("searchResultBusiness").get("businessUrl")}')

