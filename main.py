from flask import Flask, request, jsonify

app = Flask(name)

# Sample Data (Baad me Database se Connect karenge)
users = {
    "6586541322": {"player_name": "§igm฿_ßð¥", "region": "IND", "status": "NOT BANNED"},
    "1234567890": {"player_name": "Hacker123", "region": "US", "status": "BANNED"},
}

@app.route('/check_banned', methods=['GET'])
def check_banned():
    player_id = request.args.get('player_id')
    
    if player_id in users:
        return jsonify({"player_id": player_id, **users[player_id]})
    else:
        return jsonify({"error": "Player not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
