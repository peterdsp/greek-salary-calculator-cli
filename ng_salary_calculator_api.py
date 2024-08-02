from flask import Flask, request, jsonify
from net_salary_calculator import calculate_net_salary

app = Flask(__name__)

@app.route('/calculate_net_salary', methods=['POST'])
def calculate_net_salary_endpoint():
    data = request.json
    gross_monthly_salary = data.get('gross_monthly_salary')
    num_children = data.get('num_children')

    if gross_monthly_salary is None or num_children is None:
        return jsonify({"error": "Please provide gross_monthly_salary and num_children"}), 400

    try:
        gross_monthly_salary = float(gross_monthly_salary)
        num_children = int(num_children)
    except ValueError:
        return jsonify({"error": "Invalid input types"}), 400

    net_monthly_salary, net_annual_salary, annual_gross_salary = calculate_net_salary(gross_monthly_salary, num_children)
    return jsonify({
        "gross_monthly_salary": gross_monthly_salary,
        "gross_annual_salary": annual_gross_salary,
        "net_monthly_salary": net_monthly_salary,
        "net_annual_salary": net_annual_salary
    })

if __name__ == '__main__':
    app.run(debug=True)