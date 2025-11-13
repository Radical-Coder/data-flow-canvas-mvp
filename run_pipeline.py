import json
import requests


def double_numbers(numbers):
    return [x * 2 for x in numbers]


def call_api():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response.raise_for_status()
    return response.json()


def main():
    with open('sample_data.json') as f:
        data = json.load(f)
    doubled = double_numbers(data)
    api_data = call_api()
    combined = {
        "doubled_numbers": doubled,
        "api_response": api_data
    }
    print(combined)


if __name__ == '__main__':
    main()
