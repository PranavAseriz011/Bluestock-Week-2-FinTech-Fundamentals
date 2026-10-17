import requests
import pandas as pd

# Step 1: Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Step 2: Send GET request
    response = requests.get(url, timeout=15)

    # Step 3: Check for HTTP errors
    response.raise_for_status()

    # Step 4: Convert JSON response into Python data
    data = response.json()

    # Step 5: Convert JSON records into a DataFrame
    df = pd.DataFrame(data)

    # Step 6: Save the data as CSV
    df.to_csv("api_data.csv", index=False)

    print("API request successful!")
    print("Total records:", len(df))
    print("Columns:", list(df.columns))
    print("CSV file created: api_data.csv")

except requests.RequestException as error:
    print("API request failed:", error)


# Experiment: Send a POST request
post_url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "My First API Experiment",
    "body": "Learning REST APIs for Bluestock FinTech",
    "userId": 1
}

post_response = requests.post(post_url, json=new_post, timeout=15)

print("\nPOST Request Status:", post_response.status_code)
print("Response JSON:", post_response.json())