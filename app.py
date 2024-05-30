#Import libraries
from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('footballacademy.html')


@app.route('/submit', methods=["POST"])
def submit():
    #get details from form
    name = request.form.get('name')
    age = request.form.get("age")
    gender = request.form.get("email address")
    email = request.form.get ("amount")

    #define the csv filepath
    csv_file ='donation records'
    # Check if file path exists
    if not os.path.exists(csv_file):
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'Email address', 'Amount'])
    writer.writer(['name', 'age', 'email address', 'amount'])

#return the results
    return render_template('thank_you.html', name= name, age=age, emailaddress=emailaddress, amount= amount)

          
if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 5000, debug=True, threaded= True)