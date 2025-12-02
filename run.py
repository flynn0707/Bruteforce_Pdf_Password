import pikepdf
import sys

def recover_pdf_password(pdf_filename, wordlist_filename):
    print(f"Starting recovery for: {pdf_filename}")
    print(f"Using wordlist: {wordlist_filename}")
    
    try:
        # Open the wordlist file
        with open(wordlist_filename, 'r') as f:
            lines = f.readlines()
            total_passwords = len(lines)
            print(f"Loaded {total_passwords} passwords to test...")

            for index, line in enumerate(lines):
                # Clean the password (remove newlines/spaces)
                password = line.strip()
                
                try:
                    # Attempt to open the PDF with the current password
                    with pikepdf.open(pdf_filename, password=password) as pdf:
                        print("\n" + "="*40)
                        print(f" SUCCESS! Password found: {password}")
                        print("="*40)
                        return password
                        
                except pikepdf.PasswordError:
                    # Password was wrong, continue to the next one
                    continue
                except Exception as e:
                    print(f"\nAn unexpected error occurred: {e}")
                    return None

                # Optional: Show progress every 1000 attempts
                if index % 1000 == 0:
                    sys.stdout.write(f"\rTesting... {index}/{total_passwords} ({((index/total_passwords)*100):.1f}%)")
                    sys.stdout.flush()

        print("\n\nPassword not found in the provided wordlist.")
        return None

    except FileNotFoundError:
        print("\nError: Could not find the PDF or the Wordlist file.")
        print("Make sure the filenames are correct and in the same folder.")

if __name__ == "__main__":
    # CHANGE THESE FILENAMES TO MATCH YOUR FILES
    target_pdf = "a.pdf" 
    wordlist = "1.txt" 
    
    recover_pdf_password(target_pdf, wordlist)