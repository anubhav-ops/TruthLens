from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/analyze", methods = ["POST"])
def analyze():
	data = request.get_json()
	if not data or "url" not in data: 
		return jsonify({"status":"error", "message":"Missing 'url' in request body"}), 400
	
	url = data["url"]
	return jsonify({"status": "success", "received_url":url})
if __name__ == "__main__":
	app.run(debug=True)