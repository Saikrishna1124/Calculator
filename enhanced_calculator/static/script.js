function calculate(operation) {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;

    let numbers = [];
    if (num1) numbers.push(num1);
    if (num2) numbers.push(num2);

    fetch('/calculate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({operation: operation, numbers: numbers})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('display').value = data.result;
    })
    .catch(error => {
        document.getElementById('display').value = "Error";
    });
}
