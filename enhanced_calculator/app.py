from flask import Flask, render_template, request, jsonify
from calculator import add, subtract, multiply, divide, power, square_root, modulo, factorial

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    numbers = data.get('numbers', [])

    try:
        # Convert all numbers to float
        numbers = [float(num) for num in numbers]

        if operation == 'add':
            result = add(numbers)
        elif operation == 'subtract':
            result = subtract(numbers)
        elif operation == 'multiply':
            result = multiply(numbers)
        elif operation == 'divide':
            result = divide(numbers)
        elif operation == 'power':
            result = power(numbers[0], numbers[1])
        elif operation == 'sqrt':
            result = square_root(numbers[0])
        elif operation == 'modulo':
            result = modulo(numbers[0], numbers[1])
        elif operation == 'factorial':
            result = factorial(numbers[0])
        else:
            result = "Invalid operation"
    except Exception as e:
        result = str(e)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
