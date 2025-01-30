import os
import requests
from tqdm import tqdm

def download_file(url, destination=None):
    """
    Download a file from a given URL and save it locally.
    
    Args:
        url (str): The URL of the file to download.
        destination (str): The path where the file will be saved (optional).
    """
    # If destination is not provided, save the file in the current directory with the same name as in the URL
    if not destination:
        local_filename = url.split('/')[-1]
    else:
        local_filename = destination
    
    # Send a GET request to the URL
    with requests.get(url, stream=True) as response:
        total_size = int(response.headers.get('content-length', 0))  # Get total file size
        block_size = 1024  # 1 KB block size
        
        # Download the file with a progress bar using tqdm
        with open(local_filename, 'wb') as file, tqdm(
            desc=local_filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
        ) as bar:
            for data in response.iter_content(block_size):
                bar.update(len(data))  # Update progress bar
                file.write(data)  # Write data to file
    
    print(f'\nDownload completed: {local_filename}')
    return local_filename


def main():
    # Get URL input from the user
    url = input("Enter the download link: ").strip()
    
    # Ask user for an optional custom file name
    custom_name = input("Enter custom file name (or leave empty to use the default): ").strip()
    
    if not url:
        print("Error: No URL provided.")
        return
    
    # Start downloading the file
    if custom_name:
        download_file(url, custom_name)
    else:
        download_file(url)

if __name__ == '__main__':
    main()
