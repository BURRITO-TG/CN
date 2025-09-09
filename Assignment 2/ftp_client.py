import ftplib
import os

def ftp_client():
    # Public test FTP server
    FTP_HOST = "ftp.dlptest.com"
    FTP_USER = "dlpuser"
    FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

    # Create a dummy file to upload
    file_to_upload = "test_upload.txt"
    with open(file_to_upload, "w") as f:
        f.write("This is a test file for the FTP assignment.")
    
    downloaded_file = "test_download.txt"

    print("--- Starting FTP Session ---")
    try:
        with ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS) as ftp:
            print(f"Connected to {FTP_HOST}.")

            # 1. Upload a file
            with open(file_to_upload, 'rb') as f:
                ftp.storbinary(f'STOR {file_to_upload}', f)
            print(f"File '{file_to_upload}' uploaded successfully.")

            # 2. List directory contents
            print("\nListing directory contents:")
            files = ftp.nlst()
            for file in files:
                print(f"  - {file}")
            
            # Confirm upload
            if file_to_upload in files:
                print(f"Confirmed '{file_to_upload}' is on the server.")

            # 3. Download the file
            with open(downloaded_file, 'wb') as f:
                ftp.retrbinary(f'RETR {file_to_upload}', f.write)
            print(f"\nFile '{file_to_upload}' downloaded as '{downloaded_file}'.")

            # 4. Verify content
            with open(downloaded_file, 'r') as f:
                content = f.read()
            if "This is a test file" in content:
                print("Downloaded file content verified successfully.")

    except ftplib.all_errors as e:
        print(f"An FTP error occurred: {e}")
    finally:
        # Clean up local files
        # if os.path.exists(file_to_upload):
        #     os.remove(file_to_upload)
        # if os.path.exists(downloaded_file):
        #     os.remove(downloaded_file)
        print("\n--- FTP Session Closed ---")


if __name__ == "__main__":
    ftp_client()