import requests
import json

def http_client():
    test_url = 'https://jsonplaceholder.typicode.com/posts'
    
    # --- 1. GET Request ---
    print("--- Sending GET Request ---")
    try:
        get_response = requests.get(test_url + '/1')
        get_response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        print(f"Status Code: {get_response.status_code}")
        print("\nResponse Headers:")
        for key, value in get_response.headers.items():
            print(f"  {key}: {value}")
        
        print("\nResponse Body:")
        print(json.dumps(get_response.json(), indent=2))

    except requests.exceptions.RequestException as e:
        print(f"GET Request Failed: {e}")

    # --- 2. POST Request ---
    print("\n--- Sending POST Request ---")
    post_data = {
        'title': 'Computer Networks',
        'body': 'Lab Assignment 2',
        'userId': 1
    }
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    
    try:
        post_response = requests.post(test_url, json=post_data, headers=headers)
        post_response.raise_for_status()

        print(f"Status Code: {post_response.status_code}")
        print("\nResponse Body (from server):")
        print(json.dumps(post_response.json(), indent=2))

    except requests.exceptions.RequestException as e:
        print(f"POST Request Failed: {e}")

if __name__ == "__main__":
    http_client()