from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://hackutd2025.eog.systems"
# r = requests.get(f"{base}/api/Data", params={"start_date": 0, "end_date": 2000000000}, timeout=10)
# r.raise_for_status()
# print(r.headers.get("Content-Type"))
# print(r.json())

@app.route("/couriers")
def get_couriers():
    try:
        response = requests.get(f"{BASE_URL}/api/Information/couriers", timeout=10)
        response.raise_for_status()
        data = response.json()  # This is a list of CourierDto objects
        # Optional: only return id, name, capacity
        couriers = [
            {
                "id": c.get("courier_id"),
                "name": c.get("name"),
                "max_carrying_capacity": c.get("max_carrying_capacity")
            }
            for c in data
        ]
        return jsonify(couriers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True)