# importing the module
import os
  
# sets the text colour to green 
os.system("tput setaf 2")
  
print("Launching Terminal User Interface")
  
# sets the text color to red
os.system("tput setaf 1")
  
print("\t\tWELCOME TO Terminal User Interface\t\t\t")
  
# sets the text color to white
os.system("tput setaf 7")
  
print("\t-------------------------------------------------")
print("Entering local device")
while True:
    print("""
        1.Bash Shell
        2.Config Cert And Hostname
        3.Configure web
        4.Configure docker
        5.Add user
        6.Delete user
        7.Troubleshoot Server
        8.Backup Docker
        10.update ubuntu
        9.Exit""")
  
    ch=int(input("Enter your choice: "))
  
    if(ch == 1):
        os.system("bash")
  
    elif ch == 2:
        os.system("sh /etc/certbot.install-setup.sh")
  
    elif ch == 3:
        os.system("yum install httpd -y")
        os.system("systemctl start httpd")
        os.system("systemctl status httpd")
  
    elif ch == 4:
        os.system("yum install docker-ce -y")
        os.system("systemctl start docker")
        os.system("systemctl status docker")
  
  
    elif ch == 5:
        new_user=input("Enter the name of new user: ")
        os.system("sudo useradd {}".format(new_user))
        os.system("id -u {}".format(new_user) )   
          
    elif ch == 6:
        del_user=input("Enter the name of the user to delete: ")
        os.system("sudo userdel {}".format(del_user))
  
    elif ch == 7:
       os.system("bash /home/tacticalrmm/install/troubleshoot_server.sh")
    elif ch == 8:
       os.system("bash /home/tacticalrmm/install/docker-backup-scripts/backup-all.sh")
    elif ch == 10:
       os.system("sudo sh /etc/update.sh")
    elif ch == 9:
        print("Exiting application")
        exit()
    else:
        print("Invalid entry")
  
    input("Press enter to continue")
    os.system("clear")


