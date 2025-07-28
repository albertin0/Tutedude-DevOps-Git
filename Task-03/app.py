from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def form():
    current_day = datetime.now().strftime("%A")
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template('form.html', current_day=current_day, current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)