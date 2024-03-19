#User-Agent Definition:
    
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
#URL Definition:
url = 'https://jooble.org/SearchResult?p=4&rgns=Indiana&ukw=data%20science'
#Parsing HTML Content:
r = requests.get(url, headers=agent)

#Parsing HTML Content:
soup = BeautifulSoup(r.text, "html")


u= soup.find_all('div', class_="infinite-scroll-component__outerdiv")
pro=[]
for  item in u:
    for link in item.find_all('a',href=True):
        pro.append(link['href'])
        
        
        
        
import requests
from bs4 import BeautifulSoup
import time

# Define user agent
agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    #"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}

# List to store data
data_list = []

# Loop through each link
for link in pro:
    try:
        start_time = time.time()  # Record start time

        # Send GET request
        response = requests.get(link, headers=agent, verify=False)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract job details
        job_title = soup.find('h1', class_="x5dWY- h2").text.strip()
        company_name = soup.find('p', class_="z6WlhX").text.strip()
        location = soup.find('div', class_='caption TvUaeW').text.strip()
        posting_date = soup.find('div', class_='qWhsVN sziB5b').text.strip()
        job_type = soup.find('div', class_='"blapLw q40Pqk fhg31q NTN-BG"').text.strip()
        job_description = soup.find('p', simplifier="block").text.strip()
        required_qualifications = soup.find('ul').find('li').text.strip()

        # Record end time and calculate request time
        end_time = time.time()
        request_time = end_time - start_time

        # Create dictionary to store data
        job_data = {
            'Job_Title': job_title,
            'Company_Name': company_name,
            'Location': location,
            'Posting_Date': posting_date,
            'Job_Type': job_type,
            'Job_Description': job_description,
            'Required_Qualifications': required_qualifications,
            'Request_Time': request_time  # Include request time in job data
        }

        # Append data to list
        data_list.append(job_data)

        # Add a delay of 1 second between requests
        time.sleep(1)

    except Exception as e:
        print(f"An error occurred for {link}: {e}")

# Print or further process data_list as needed
print(data_list)
