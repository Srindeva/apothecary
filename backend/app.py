from flask import Flask, jsonify
from dataclasses import dataclass
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_BASE = "https://hackutd2025.eog.systems"
# # request = requests.get(f"{base}/api/Data", params={"start_date": 0, "end_date": 2000000000}, timeout=10)
# # requestraise_for_status()
# # print(request.headers.get("Content-Type"))
# # print(request.json())

# response_couriers = requests.get(f"{BASE_URL}/api/Information/couriers", timeout=10)
# response_couriers.raise_for_status()
# couriers_data = response_couriers.json()

# print(couriers_data[0])

@app.route("/cauldrons")
def get_cauldrons():
    try:
        response = requests.get(f"{API_BASE}/api/Information/cauldrons", timeout=10)
        response.raise_for_status()
        data = response.json()  
        cauldrons = [
            {
                "max_volume": c.get("max_volume"),
                "id": c.get("id"),
                "name": c.get("name"),
                "latitude": c.get("latitude"),
                "longitude": c.get("longitude"),
            }
            for c in data
        ]
        return jsonify(cauldrons)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/market")
def get_market():
    try:
        response = requests.get(f"{API_BASE}/api/Information/market", timeout=10)
        response.raise_for_status()
        market = response.json()  
        return market
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @app.route("/couriers")
# def get_couriers():
#     try:
#         response = requests.get(f"{BASE_URL}/api/Information/couriers", timeout=10)
#         response.raise_for_status()
#         data = response.json()  
#         couriers = [
#             {
#                 "id": c.get("courier_id"),
#                 "name": c.get("name"),
#                 "max_carrying_capacity": c.get("max_carrying_capacity")
#             }
#             for c in data
#         ]
#         return jsonify(couriers)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True)

# @dataclass
# class Ticket:
#     ticket_id: str
#     cauldron_id: str
#     amount_collected: float
#     courier_id: str
#     date: str

# @dataclass
# class Courier:
#     courier_id: str
#     name: str
#     max_carrying_capacity: float    

# def fetch_tickets():
#     response = requests.get(f"{API_BASE}/api/Tickets")
#     response.raise_for_status()
#     data = response.json()
#     # This is an object with `.transport_tickets` as its array of tickets
#     tickets_raw = data.get("transport_tickets", [])
#     tickets = []
#     for t in tickets_raw:
#         ticket = Ticket(
#             ticket_id=t.get("ticket_id"),
#             cauldron_id=t.get("cauldron_id"),
#             amount_collected=t.get("amount_collected"),
#             courier_id=t.get("courier_id"),
#             date=t.get("date")
#         )
#         tickets.append(ticket)
#     return tickets

# # Example usage
# for ticket in fetch_tickets():
#     print(f"Ticket {ticket.ticket_id}: {ticket.amount_collected} from cauldron {ticket.cauldron_id} by courier {ticket.courier_id} on {ticket.date}")