from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home_route():
   return render_template('./index.html') 

@app.route('/<string:page_name>')
def html_page(page_name):
   return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        sender_name = data["sender_name"]
        email = data["email"]
        number = data["number"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{sender_name},{email},{subject},{number},{message}') 

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        sender_name = data["sender_name"]
        email = data["email"]
        number = data["number"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([sender_name,email,number,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong. Try again!'
