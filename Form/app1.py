#Import libraries
from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')


@app.route('/submit', methods=["POST"])
def submit():
    #get details from form
    name = request.form.get('name')
    age = request.form.get("age")
    gender = request.form.get("gender")
    email = request.form.get ("email")

    #define the csv filepath
    csv_file ='submissions'
    # Check if file path exists
    if not os.path.exists(csv_file):
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'Gender', 'Email'])
            writer.writerow(['name', 'age', 'gender', 'email'])

#return the results
    return render_template('result.html', name= name, age=age, gender=gender, email=email)

          
if __name__ == '__main__':
    app.run(debug=True)




