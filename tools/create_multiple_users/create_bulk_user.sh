#!/bin/bash
# create header for csv output
echo "Name,FB02UID,Username,Password,Matrikel,Raum,Platz,Date" >> username_passwd.csv
while IFS=, read -r col1 col2 col3 col4 col5 col6
do
  STUDENT_NAME="$col1"
  STUDENT_ID="$col2"
  MATRIKEL="$col3"
  RAUM="$col4"
  PLATZ="$col5"
  DATE="$col6"
 
  # Use the following if the username is written as <[username2s]>
  # The following will remove the bracket
  #STUDENT_ID=${STUDENT_ID#*[}
  #STUDENT_ID=${STUDENT_ID%]*}
  #STUDENT_ID=${STUDENT_ID} 
  
  # Use the following to remove 2s
  #STUDENT_USERNAME=$(echo "wus-$STUDENT_ID" | cut -f1 -d"2"):}
  
  STUDENT_USERNAME=$(echo "wus-$STUDENT_ID")
  
  # Use the following to remove 1 chars from back
  #STUDENT_USERNAME=${STUDENT_USERNAME::-1}
  
  # Create user without password
  adduser $STUDENT_USERNAME --gecos "$STUDENT_USERNAME, RoomNumber, WorkPhone, HomePhone" --disabled-password
  
  # Generate random password
  RAND_PASSWD=$(shuf -i 10000-100000 -n 1)
  echo "$STUDENT_USERNAME:$RAND_PASSWD" | chpasswd
  echo $STUDENT_USERNAME
  echo $RAND_PASSWD

  # You can skip this permission setup
  # by changing default mode in /etc/adduser.conf
  # DIR_MODE = 0750 
  
  # Restric user to their own home dir only
  #setfacl --modify user:$STUDENT_USERNAME:0 /home/$STUDENT_USERNAME
  #echo "Student $STUDENT_USERNAME is given special permission"
  #getfacl /home/$STUDENT_USERNAME

  # Save username and password to csv
  echo "$STUDENT_NAME, $STUDENT_ID,$STUDENT_USERNAME, $RAND_PASSWD, $MATRIKEL, $RAUM, $PLATZ, $DATE" >> username_passwd.csv
done < exam_complete_list.csv
