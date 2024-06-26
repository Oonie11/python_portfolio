from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('./database.csv',mode= 'a', newline='') as database2:
        email,subject,message = data['email'],data['subject'],data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
        except:
            return 'did not saved to data base.'
        return redirect('/thankyou.html')
    else:
        return "something went wrong try again."

if __name__ == '__main__':
    app.run(debug=True)
