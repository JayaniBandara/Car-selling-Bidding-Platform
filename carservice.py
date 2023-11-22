from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for services offered
services_offered = ["Oil Change", "Brake Inspection and Repair", "Engine Diagnostics", "Tire Rotation and Replacement"]

@app.route('/')
def home():
    return render_template('index.html', services=services_offered)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        # Handle the form submission for appointment scheduling
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        selected_service = request.form['service']
        preferred_date = request.form['date']

        # You can process the form data here (e.g., send an email, save to a database)

        return render_template('appointment_confirmation.html', name=name, service=selected_service, date=preferred_date)

    return render_template('appointment.html', services=services_offered)

if __name__ == '__main__':
    app.run(debug=True)
