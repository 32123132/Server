from flask import Flask, request, jsonify

app = Flask(__name__)

# Временная "база данных" для демонстрации
registered_users = [
    "ruslantumbum"
]


@app.route('/check_username', methods=['POST'])
def check_username():
    # Получаем данные из запроса
    data = request.get_json()

    # Проверяем наличие имени пользователя в запросе
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username'].strip()

    # Валидация формата имени пользователя
    if len(username) < 4:
        return jsonify({
            "valid": False,
            "reason": "Username must be at least 4 characters long"
        }), 200

    if not username.isalnum():
        return jsonify({
            "valid": False,
            "reason": "Username can only contain letters and numbers"
        }), 200

    # Проверка на занятость имени
    if username.lower() in [u.lower() for u in registered_users]:
        return jsonify({
            "valid": True,
            "reason": "Username is correct"
        }), 200

    return jsonify({
        "valid": False,
        "reason": "Username doesn't buy script)"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)