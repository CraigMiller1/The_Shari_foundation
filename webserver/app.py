from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index.html')
def landing():
    return render_template('index.html')

@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    
    # Handle the email, e.g., send a notification email
    # Add your email sending logic here
    
    # Redirect to a thank you page or the home page
    return redirect(url_for('landing'))

if __name__ == '__main__':
    app.run(debug=True)

def write_to_file(data):
    with open('database.txt', mode='a') as database2:
        email = data["email"]
        password = data["password"]
        passwordconfirm = data["passwordconfirm"]
        file = database2.write(f'\n{email},{password},{passwordconfirm}')
def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        password = data["password"]
        passwordconfirm = data["passwordconfirm"]
        csv_writer = database.write(database, delimiter=',', quotecharacter='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,password,passwordconfirm])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. try again.'