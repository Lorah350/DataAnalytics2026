# Requirements and Conceptual Model
Sonia, Lorah & Smaya 

b) Brainstorm some basic requirements for this project. Who is the “end user” and
what will the end user need to be able to do? What different categories of data
might be important to track?

 Lana is the end user, being the owner of the business. The data that needs to be tracked is:
 -Customers : info on customer 
 -Dogs : info on dog 
 -Appointments : appointment info 
 -Payments : payment information 

c)For each broad category of data that you come up with, what specific pieces of
information would be useful to track? For each category, create a list of bullets
with what information that category includes.

Customer:
-Customer ID
-Full name
-Phone number
-Email
-Address

Dog: 
-Dog ID
-Dog name 
-Dog Breed 
-Age
-Weight 
-Special Intruction
-Customer ID

Appointments: 
-Appointment ID
-Date 
-Time 
-Duration 
-Dog ID
-Customer ID 

Payments:
-Payment ID
-Payment Date
-Amount 
-Payment Status
-Customer ID

# Logical Model

a) What should be the main entities in your database (which will translate into tables)?
Aim for at least three, but not more than five, to keep things from getting overly
complicated.

Our Entities would be customer, dog, appointment and payment 

b) What attributes (column names) belong to each of those entities? It may be helpful
to consider an example of a single record belonging to that entity – what are the
pieces of information that the record should include?

All of the IDs within our entities, Dates, Times, Names and Info stated in 1.C. 

c) What entities will have relationships to each other? That is, what information will
need to be reassembled together when data is retrieved from the database?

They will all have a relationship with Customer ID. They are related to the Customer and Dog. 

d) Can you identify any possible many-to-many relationships between your tables
that will need to a resolving table?

A customer might have many dogs, sales, and appointments. Resolving table would be ReacurringCustomer. 

  
