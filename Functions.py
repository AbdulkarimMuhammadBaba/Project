#8.1
def display_message():
    return "I am learning how to define and call a function in python"
    
#8.2
def favourite_book(title):
    return f"one of my favourite book is {title}"
    
#8.3
def make_Tshirt(size,text):
    msg=f"The size of the shirt is {size} and the word \'{text}\' is printed on it"
    return msg
    
mts=make_Tshirt("small","Nike")
print(mts)
mtts=make_Tshirt(size="small",text="Nike")
print (mtts)

#8.4
def make_Tshirt(text,size="large"):
    msg=f"The size of the shirt is {size} and the word \'{text}\' is printed on it \nI love python"
    return msg
mts=make_Tshirt("Nike")
print(mts)
mtts=make_Tshirt(size="small",text="Nike")
print (mtts)
#8.5
def describe_city(city,country="Nigeria"):
    return f"{city} is in {country}"
print (describe_city("Kano"))
print(describe_city("Abuja"))
print (describe_city("Paris"))
#8.6
def city_country(city,country):
    return f"{city}, {country}"
print (city_country("Accra","Ghana"))
print(city_country("Abuja", "Nigeria"))
print (city_country("Paris","France"))
#8.7
def make_album(artist, album):
    dict={artist : album}
    return dict
print (make_album("Psquare","Do Me"))
print (make_album("Akon","Mama Africa"))
print (make_album("Maheer zhain","Huwa Ahmdun Wa Muhammad"))
##
def make_album(artist, album,name=''):
    if name:
        dict={artist : album, "number of songs":name}
        return dict
    else:
        return {artist : album}
print (make_album("Psquare","Do Me",20))
print (make_album("Akon","Mama Africa"))
print (make_album("Maheer zhain","Huwa Ahmdun Wa Muhammad"))
#8.8
while True:
    artist=input ("artist name: ")
    title=input ("album title: ")
    if artist!="q":
        print(make_album(artist, title))
    elif  artist=="q":
        break
#8.9
lst=["his book", "hello, musa","stand up"]
def show_message():
    for i in lst:
        print(i)
show_message()
#8.10
def send_message():
    new_lst=[]
    for i in lst:
        new_lst.append(i)
        print ("new list: ",new_lst)
        print ("original list: ",lst)
send_message()
#8.12
def sw_toppings(*toppings):
    toppingz=[]
    for i in toppings:
        toppingz.append(i)
    return toppingz
print (sw_toppings("chicken","cheese","mayonnaise","coslow"))
print (sw_toppings("cheese","butter"))
print (sw_toppings("meat","cheese","mayonnaise"))
#8.13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first 
    user_info['last_name'] = last     
    return user_info 
user_profile = build_profile('Abdul', 'Abe',location='Kano',field='structures')
print(user_profile)
#8.14
def car_informations(name,model,**car_info):
    car_info['car_name'] = name
    car_info['car_model'] = model  
    return car_info 
car_infos= car_informations('Honda', 'Accord', doors=2,year=2012, type='sedan')
print(car_infos)
#8.15
import my_module
from my_module import square
from my_module import square as sq
from my_module import *