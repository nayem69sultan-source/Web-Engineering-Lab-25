from flask import Flask, render_template, request

app = Flask(__name__)

patients = [
    {"name": "Rahim Ahmed", "age": 30, "contact": "01912-345678"},
    {"name": "Sultana Begum", "age": 25, "contact": "01876-543210"},
]

appointments = [
    {"date": "2024-10-31", "time": "10:00 AM", "patient_name": "Rupa Das", "doctor": "Dr. Kamal Hossain"},
]

doctors = [
    {"name": "Dr. Kamal Hossain", "specialty": "Cardiology", "contact": "01711-987654"},
    {"name": "Dr. Faria Rahman", "specialty": "Pediatrics", "contact": "01711-123456"},
]

prescriptions = [
    {"patient_name": "Rahim Ahmed", "medicine": "Aspirin", "dosage": "100mg"},
    {"patient_name": "Sultana Begum", "medicine": "Paracetamol", "dosage": "500mg"},
]

invoices = [
    {"invoice_number": "INV001", "patient_name": "Rupa Das", "date": "2024-10-30", "amount": "৳2000", "status": "Paid"},
    {"invoice_number": "INV002", "patient_name": "Rahim Ahmed", "date": "2024-10-29", "amount": "৳1500", "status": "Pending"},
]

reports = [
    {"report_type": "Monthly Patients", "date": "2024-10-01", "generated_by": "Admin"},
    {"report_type": "Weekly Prescriptions", "date": "2024-10-28", "generated_by": "Admin"},
]

@app.route('/')
def index():
    return render_template(
        'index.html',
        patients=patients,
        appointments=appointments,
        doctors=doctors,
        prescriptions=prescriptions,
        invoices=invoices,
        reports=reports
    )

# Example route to handle adding a new patient (you can extend this)
@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form.get('name')
    age = request.form.get('age')
    contact = request.form.get('contact')
    patients.append({"name": name, "age": age, "contact": contact})
    return render_template(
        'index.html',
        patients=patients,
        appointments=appointments,
        doctors=doctors,
        prescriptions=prescriptions,
        invoices=invoices,
        reports=reports
    )

if __name__ == '__main__':
    app.run(debug=True)
