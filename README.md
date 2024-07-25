# SSHStorm

SSHStorm is a Python script that performs a brute-force attack on SSH login credentials using a list of common passwords. It attempts to authenticate against a specified SSH server and reports any successful password discoveries.

### Features
- Test SSH login attempts using a list of commonly used passwords.
- Simple and intuitive command-line interface.
- Provides immediate feedback on password validity for each attempt.

### Technologies Used
- Python 3
- `paramiko` library for SSH connections

### Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/0xknoty/SSHStorm.git
    cd SSHStorm
    ```

2. Run the script:
    ```bash
    python SSHStorm.py
    ```

3. Configuration:
    - Edit the `host`, `username`, and `password_file` variables in the script to match your target settings.
    - Place your list of common passwords in `ssh-common-passwords.txt`.

4. Execution:
    - The script will sequentially attempt each password from the list and display whether the password is valid or not.

### How It Works
- The script reads passwords from a specified file and tries each one against the SSH server.
- For each password, it uses the `paramiko` library to attempt an SSH connection.
- If a valid password is found, it prints the successful password and stops further attempts.
- Invalid passwords are reported, and the script continues with the next password.

### Disclaimer
The author of this script is not responsible for any misuse or damages caused by using this script. Use it at your own risk.
Happy hacking responsibly!
