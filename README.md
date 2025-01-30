# File Downloader
Overview
-A simple Python script to download files from a given URL while displaying a progress bar using tqdm.

## Features
-Downloads any file from a specified URL
-Displays a real-time progress bar
-Allows user to specify a custom filename

## Requirements
- `requests`
- `tqdm`

## Installation && Usage
1. Install requirements using pip

```bash
pip install requests tqdm
```
2. Run the script using:
```bash
python linux_downloader.py
```

## Example Output
-Enter the download link: https://example.com/file.zip
-Enter custom file name (or leave empty to use the default): myfile.zip
-myfile.zip: 5.00MB [00:10, 500KB/s]
-Download completed: myfile.zip

## Contibutions
Contributions are welcome! Feel free to fork this repository and submit a pull request.

