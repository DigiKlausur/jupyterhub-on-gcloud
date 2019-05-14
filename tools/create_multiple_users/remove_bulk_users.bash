for username in $(< dellist.txt)
  do
    echo "$username"
    echo "/home/$username"
    echo "Removing $username"
    userdel $username
    echo "Removing /home/$username"
    rm -rf /home/$username
  done
