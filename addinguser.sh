#!/bin/bash

echo "Add  a  user and add user to group" | figlet
# runs the program
control(){
    getName
    getGroup
    echo "Name: $user"
     echo "User Group: $group"
     makeprofile
    
}

# choose new user to add
getName() {
    echo "What is the user name?"
    read user
    
}

# assign user to a group
getGroup() {

    while [ "$group" != "linda" ] && [ "$group" != "student" ] && [ "$group" != "naruto" ] && [ "$group" != "people" ] 
    do
    echo "What group would you like to assign the user to?[linda, student, naruto or people]"
    read group
done

}

# adds user and adds user to chosen group
makeprofile(){
   # sudo adduser $user
   sudo useradd $user
    sudo usermod -G $group $user
}

control

echo
echo
echo " ************************************************************ "
echo "User $user created and added to group $group"
echo " "
echo "examine members of group $group: "
getent group $group
echo " ************************************************************ "
