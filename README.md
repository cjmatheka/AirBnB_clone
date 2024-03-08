# 0x00. AirBnB clone - The console  
This is exactly as it sounds, an airBnB clone.

## Project Overview 
A web platform replicating the core features of Airbnb, allowing hosts to list their accommodations and guests to
book short-term stays.

**Core Features:**  
1. Listing Management:
   + Hosts create listings (descriptions, photos, pricing, availability, rules).
   + Guests search with filters (location, dates, guests, amenities, price).
2. Booking System:
   + Hosts maintain availability calendars.
   + Guests send booking requests; hosts approve/decline.
   + Secure payment processing integrated.
3. User Profiles:
   + Profiles for guests and hosts (info, contact details, verification).
4. Reviews & Ratings:
   + Guests and hosts leave reviews to build trust.
5. Messaging:
   + Facilitates communication between hosts and guests throughout the booking process.

## Command Interpreter
**Purpose:**
A custom command-line interface (CLI) that lets you interact with the Airbnb clone's underlying data and functionality 
without needing a graphical web interface. This is particularly useful during development and testing.

**Functionality:**
The typical functions would include:  
+ Creating Objects: Commands to create new users, listings, cities, etc.
+ Managing Objects: Commands to update details, check availability, change pricing, etc.
+ Deleting Objects: Commands to remove users, listings or other data.
+ Displaying Information: Commands to list all users, show available listings, or fetch other relevant data.

**How to Start It:**
We will use a Python script (named console.py) to start the console:
```
./console.py
```

How to Use It:
The command interpreter would have its own specific commands. Here's a potential example structure:
+ create <object_type> <attributes>: Creates a new object
```
(hbnb) create City name="Nairobi"
```
+ update <object_type> <id> <attribute> <new_value>: Updates an existing object
```
(hbnb)
```
+ all <object_type>: Lists all objects of a type (e.g., all users)
```
(hbnb)
```
+ show <object_type> <id>: Shows details of a specific object (e.g., show listing 123)
```
(hbnb)
```
+ exit: Quits the command interpreter.
```
(hbnb)
```
create city name="Nairobi"
create user name="Jane Smith" email="jane@example.com" password="mypassword"
update listing 567 availability "2024-09-21" "2024-09-25"
show booking 34
all reviews

