# 0x00. AirBnB clone - The console  
This is exactly as it sounds, an airBnB clone.
![](images/console.png)

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

**Starting the interpreter:**  
We will use a Python script (named console.py) to start the console:
```
./console.py
(hbnb)
```

**Using it to Create Instances:**    
The command interpreter would have its own specific commands. Here's a potential example structure:
+ `create <ModelClass>`: Creates a new object
```
Example:

(hbnb) create BaseModel
b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0
(hbnb) 
```
**Using it to Show Instances of s Specific Class:**
+ `show <ModelClass> <id>`: Shows details of a specific object
```
Example:

(hbnb) show BaseModel b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0
[BaseModel] (b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0) {'id': 'b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0','created_at':
datetime.datetime(2024, 3, 11, 3, 18, 11, 877749), 'updated_at': datetime.datetime(2024, 3, 11, 3, 18, 11, 877765)}
(hbnb) 
```
**Using it to Update Instances:**
+ `update <ModelClass> <id> <attribute> <new_value>`: Updates an existing object
```
Example:

(hbnb) update BaseModel b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0 first_name james
(hbnb) show BaseModel b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0
[BaseModel] (b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0) {'id': 'b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0', 'created_at':
datetime.datetime(2024, 3, 11, 3, 18, 11, 877749), 'updated_at': datetime.datetime(2024, 3, 11, 3, 20, 22, 51888),
'first_name': 'james'}
(hbnb)
```
**Using it to Update Instances:**
+ `destroy <ModelClass> <id>`: Deletes an existing object
```
Example:

(hbnb)
(hbnb) destroy BaseModel 950409fc-e4cc-45bc-bdbd-405ba89d800d
(hbnb) show BaseModel 950409fc-e4cc-45bc-bdbd-405ba89d800d
** no instance found **
(hbnb) 
```

**Using it to List All Instances:**
+ `all <ModelClass>`: Lists all objects of a type (e.g., all users)
```
Example:

(hbnb) all BaseModel
[BaseModel] (b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0) {'id': 'b17d9911-ae6f-4dbf-8dc1-8c1faf6047b0', 'created_at':
datetime.datetime(2024, 3, 11, 3, 18, 11, 877749), 'updated_at': datetime.datetime(2024, 3, 11, 3, 20, 22, 51888),
'first_name': '"james"'}
(hbnb) 

```
**Closing the Command Interpreter:**
+ `quit`: Quits the command interpreter.
```
Example:

(hbnb) quit
(envbnb) cjweb@ubuntu:~/Desktop/Software Engineering/AlxAfricaSE/AirBnB_clone$ 
```

