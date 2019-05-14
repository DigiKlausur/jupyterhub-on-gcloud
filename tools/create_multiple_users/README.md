How to create bulk linux users with random password </br>
* Create a list of all students
** The columns of the list should contain the following
*** Name
*** F02UID (i.e. mwasil2s)
*** Matrikel nummer
*** Room number
*** Platz
*** Date
* Run create_bulk_user.sh with sudo
** sudo bash create_bulk_user.sh
** Once the user creation is done, it will generate a new list of users with password
* Once we have the list of users with their password, we can generate a pdf of each user information. This will be the id of the student and will be handed by Prüfung Aufsicht (Invigilator)
** TODO: ipynb or python file to generate pdf
* Removing bulk user
** Create a dellist containing usernames to delete
** run remove_bulk_users.bash with sudo
*** sudo bash remove_bulk_users.bash
