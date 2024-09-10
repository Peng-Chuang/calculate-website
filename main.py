from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form['item']
        quantity = int(request.form['quantity'])
        price = calculate_price(item, quantity)
        return render_template('index.html', price=price, item=item, quantity=quantity)
    return render_template('index.html')

def calculate_price(item, quantity):
    prices = {'apple': 1, 'banana': 0.5, 'orange': 0.8}
    return prices.get(item, 0) * quantity

if __name__ == '__main__':
    app.run(debug=True)
