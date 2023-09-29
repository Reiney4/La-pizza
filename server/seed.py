#!/usr/bin/env python3

# Import necessary modules
from random import choice as rc, sample
from faker import Faker
from models import db, Restaurant, Pizza, RestaurantPizza
from app import app
import random


# Define a list of pizza names
pizza_names = [
    "Margherita Pizza",
    "Pepperoni Pizza",
    "Hawaiian Pizza",
    "Mushroom and Garlic Pizza",
    "Veggie Supreme Pizza",
    "Meat Lovers Pizza",
    "BBQ Chicken Pizza",
    "White Pizza",
    "Buffalo Chicken Pizza",
    "Four Cheese Pizza",
    "Pesto Pizza",
    "Taco Pizza",
    "Mediterranean Pizza",
    "Supreme Pizza",
    "Breakfast Pizza",
    "Clam Pizza",
    "BBQ Pulled Pork Pizza",
    "Philly Cheesesteak Pizza",
    "BLT Pizza",
    "Shrimp Scampi Pizza",
]

# Define a list of pizza ingredients
ingredients = [
    "Tomato sauce",
    "Mozzarella cheese",
    "Ham",
    "Pineapple chunks",
    "Fresh basil",
    "Olive oil",
    "Sautéed mushrooms",
    "Roasted garlic",
    "Onions",
    "Black olives",
    "Sausage",
    "Bacon",
    "Ham",
]

# Create a Faker instance to generate fake data
fake = Faker()


# Clear existing data from the database
with app.app_context():
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()
    db.session.commit()

# Create fake restaurants
with app.app_context():
    restaurants = [
        Restaurant(
            name=fake.company(),
            address=fake.address(),
        )
        for _ in range(10)
    ]
    db.session.add_all(restaurants)
    db.session.commit()

# Initialize an empty list

pizzas = []
for i in range(100):
        p = Pizza(
            #get a random ingredient from the ingredient list to be used as the name of the pizza
            name =rc(ingredients),
            #create a random list of 3 ingredients joined to a single string
            ingredients =','.join(sample(ingredients,3)),            
        )
        pizzas.append(p)
        
db.session.add_all(pizzas)
db.session.commit()
       

# Create restaurant-pizza relationships
restaurant_pizzas = []
for i in range(10) : 
        rp =  RestaurantPizza(
              #generate a unique company name using faker 
            name=fake.unique.company(), 
            #generate a random price
            price=random.randint(1, 30),   
            pizza_id=rc(pizzas).id, 
            #select a random restaurant object from the restaurants list 
            restaurant_id=rc(restaurants).id)   
        restaurant_pizzas.append(rp)
     
db.session.add_all(restaurant_pizzas)
db.session.commit()
