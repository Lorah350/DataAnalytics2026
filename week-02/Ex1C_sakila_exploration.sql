/*
a) The actor table includes actor_id, first_name,last_name, and last update.
b) The film table includes film_id, title, description, release_year, language_id, rental_details, legnth, rating, and last_update.alter
c) The film_actor both actor_id and film_id.
d) The rental table includes rental_id, rental_date, inventory_id, customer_id, return_date, and staff_id. It is harder to read because it uses ID numbers instead of names.
e) The inventory table includes inventory_id, film_id, store_id, and last_update.
f) You need the rental table (to find rentals by date), the inventory table (to connect rentals to film_id), and the film table (to get the film titles). These tables are linked through inventory_id and film_id.

SELECT rental_id, rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;
*/
