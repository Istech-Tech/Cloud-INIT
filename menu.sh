#!/bin/bash

selection=
until [ "$selection" = "0" ]; do
    echo ""
    echo "PROGRAM MENU"
    echo "1 - Backup Home Directory"
    echo "2 - Show Active Users"
    echo "3 - Bash Shell"
    echo "0 - Logout"
    echo ""
    echo -n "Enter selection: "
    read selection
    echo ""
    case $selection in
        1 ) df ;;
        2 ) free ;;
        3 ) bash ;;
        0 ) exit ;;
        * ) echo "Please enter 1, 2, 3, 4, or 0"
    esac
done
