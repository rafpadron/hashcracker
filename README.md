# Hash Cracker

This project is a simple hash cracker that attempts to find the original password from a given hash using a dictionary attack. The dictionary file used is `rockyou.txt`.

## Features

- Supports multiple hash algorithms (e.g., SHA-256, MD5).
- Allows the user to input the hash to crack.
- Allows the user to input a salt (if used).
- Measures the time taken to find the password.
- Saves the found password to a results file.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/hashcracker.git
    cd hashcracker
    ```

2. **Ensure you have the `rockyou.txt` dictionary file in the same directory as [main.py](http://_vscodecontentref_/0). You can download it from various sources online.**

3. **Run the script:**

    ```sh
    python3 main.py
    ```

4. **Follow the prompts:**

    - Enter the hash to crack.
    - Enter the salt (if used).
    - Enter the hash algorithm (e.g., `sha256`, `md5`).

5. **Example of hashing a password for testing:**

    The script includes an example of how to hash a password for testing purposes. This example is executed before the main function:

    ```python
    password_to_test = "password123"
    salt_to_test = "randomsalt"
    algorithm_to_test = "md5"
    hashed_password = hash_password(password_to_test, salt_to_test, algorithm_to_test)
    print(f"The hash of the password '{password_to_test}' with salt '{salt_to_test}' using {algorithm_to_test} is: {hashed_password}")
    ```

    You can use the printed hash as input when prompted to enter the hash to crack.

## Example

```sh
$ python3 main.py
Enter the hash to crack: 482c811da5d5b4bc6d497ffa98491e38
Enter the salt: randomsalt
Enter the hash algorithm (e.g., sha256, md5): md5
Trying: password123 -> 482c811da5d5b4bc6d497ffa98491e38
Password found: password123
Time taken: 0.002 seconds
```

Educational Use Only
This project is intended for educational purposes only. It is designed to help users understand how hash functions and dictionary attacks work.

Precautions
Do not use this tool for illegal activities. Unauthorized access to data is illegal and unethical.
Use responsibly. Ensure you have permission to test the security of any system or data.
Understand the risks. Cracking passwords can expose sensitive information. Always handle such information with care.
Notes
Ensure that the rockyou.txt file is present in the same directory as main.py.
The script will ignore any lines in the dictionary file that cannot be decoded as UTF-8.
