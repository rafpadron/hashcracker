import hashlib
import time

def get_hash_from_user():
    # Prompt the user to enter the hash to crack
    return input("Enter the hash to crack: ")

def get_dictionary_file():
    # Return the name of the dictionary file to use
    return "rockyou.txt"

def get_algorithm_from_user():
    # Prompt the user to enter the hash algorithm to use
    return input("Enter the hash algorithm (e.g., sha256, md5): ")

def read_file(file_path):
    # Read the contents of the file and return as a list of lines
    try:
        with open(file_path, "r", errors="ignore") as file:
            return file.readlines()
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"File not found: {file_path}")
        return []

def calculate_hash(string, algorithm='sha256'):
    # Calculate the hash of a given string using the specified algorithm
    hash_func = getattr(hashlib, algorithm)
    return hash_func(string.encode()).hexdigest()

def find_password(hash_file, lines, algorithm='sha256'):
    # Try to find the password that matches the given hash
    for line in lines:
        line = line.strip()
        calculated_hash = calculate_hash(line, algorithm)
        print(f"Trying: {line} -> {calculated_hash}")
        if calculated_hash == hash_file:
            return line
    return None

def save_results(password, file_path="results.txt"):
    # Save the found password to a results file
    with open(file_path, "a") as file:
        file.write(f"Password found: {password}\n")

def hash_password(password, algorithm='sha256'):
    # Hash a given password using the specified algorithm
    return calculate_hash(password, algorithm)

def main():
    # Main function to coordinate the hash cracking process
    hash_file = get_hash_from_user().strip().lower()
    algorithm = get_algorithm_from_user().strip().lower()
    dic_file = get_dictionary_file()
    lines = read_file(dic_file)
    
    if lines:
        start_time = time.time()
        password = find_password(hash_file, lines, algorithm)
        end_time = time.time()
        
        if password:
            print(f"Password found: {password}")
            save_results(password)
        else:
            print("Password not found")
        
        print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    # Example of how to hash a password for testing
    password_to_test = "password123"
    algorithm_to_test = "md5"
    hashed_password = hash_password(password_to_test, algorithm_to_test)
    print(f"The hash of the password '{password_to_test}' using {algorithm_to_test} is: {hashed_password}")
    
    main()