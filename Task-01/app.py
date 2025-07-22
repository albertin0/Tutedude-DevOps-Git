from flask import Flask, jsonify
import json, requests

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    try:
        api_url = 'https://reqres.in/api/users'  # URL to fetch the JSON data
        # Make a GET request to the API endpoint    
        response = requests.get(api_url)

        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Return the data
        return jsonify(data), 200
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": str(http_err)}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in file"}), 400
    except requests.exceptions.ConnectionError as conn_err:
        # Handle connection errors (e.g., no internet connection)
        return jsonify({"error": f"Connection error occurred: {conn_err}"}), 503
    except requests.exceptions.Timeout as timeout_err:
        # Handle request timeout errors
        return jsonify({"error": f"Timeout error occurred: {timeout_err}"}), 408
    except requests.exceptions.RequestException as req_err:
        # Handle any other general request errors
        return jsonify({"error": f"An unexpected error occurred: {req_err}"}), 500
    except ValueError as json_err:
        # Handle JSON decoding errors if the response is not valid JSON
        return jsonify({"error": f"Error decoding JSON response: {json_err}"}), 500
if __name__ == "__main__":
    app.run(debug=True)
