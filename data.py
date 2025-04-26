import sys
import os
import csv

# Replace with the ACTUAL path to the directory containing the package
# Use the path you get from `pip show requests`
package_path = r"C:\Users\picfire\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages"  # Use a raw string OR
#package_path = "C:/Users/picfire/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0/LocalCache/local-packages/Python313/site-packages" # OR use forward slashes

# Add the package path to sys.path
sys.path.append(package_path)

data = []

# Now you can try importing the package
try:
    import requests
    from bs4 import BeautifulSoup
    print("Requests version:", requests.__version__)
    # print("BeautifulSoup version:", BeautifulSoup.__version__)

    # Your scraping code here...
    # Replace with the actual URL
    url = "https://www.musicmetricsvault.com/genres/rb/12"

    # Send an HTTP request to the website
    response = requests.get(url)


    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the elements containing the data you want to extract
        # (Replace with the actual CSS selectors or HTML tags)
        # Example: Extracting all the table rows
        table_rows = soup.find_all("tr")  # Example: Find all table rows

        header_row = [th.text.strip() for th in table_rows[0].find_all("th")] if table_rows else []
        if header_row:
            data.append(header_row)


        # Iterate over the elements and extract the data
        for row in table_rows:
            # Extract the data from each row (replace with your specific logic)
            cells = row.find_all("td")  # Example: Find all table data cells
            row_data = [cell.text.strip() for cell in cells]  # Extract text from each cell
            # extract the name of the artist
            # artist_name = row.find("a", class_="artist-name").text.strip() if row.find("a", class_="artist-name") else "N/A"

            # Process the extracted data (e.g., print, store in a list, etc.)
            if row_data:
                data.append(row_data)
            print(row_data)

            # Write the data to a CSV file
        filename = "spotify_data_R&B.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)

        print(f"Data written to {filename}")


    else:
        print(f"Request failed with status code: {response.status_code}")

except ImportError as e:
    print(f"ImportError: {e}")
    print("Please make sure the package is installed correctly and the path is correct.")