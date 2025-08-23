from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(_hospitalmagement_)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'hospital_management'

mysql = MySQL(app)

@app.route('/doctors', methods=['GET', 'POST'])
def manage_doctors():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM doctors")
        doctors = cur.fetchall()
        cur.close()
        return jsonify(doctors)
    
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        specialty = data.get('specialty')
        phone = data.get('phone')
        email = data.get('email')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO doctors(name, specialty, phone, email) VALUES (%s, %s, %s, %s)",
                    (name, specialty, phone, email))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Doctor added"}), 201

@app.route('/patients', methods=['GET', 'POST'])
def manage_patients():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM patients")
        patients = cur.fetchall()
        cur.close()
        return jsonify(patients)
    
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        dob = data.get('dob')
        gender = data.get('gender')
        phone = data.get('phone')
        address = data.get('address')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO patients(name, dob, gender, phone, address) VALUES (%s, %s, %s, %s, %s)",
                    (name, dob, gender, phone, address))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Patient added"}), 201

@app.route('/appointments', methods=['GET', 'POST'])
def manage_appointments():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM appointments")
        appointments = cur.fetchall()
        cur.close()
        return jsonify(appointments)
    
    if request.method == 'POST':
        data = request.json
        patient_id = data.get('patient_id')
        doctor_id = data.get('doctor_id')
        appointment_date = data.get('appointment_date')
        status = data.get('status', 'Scheduled')
        notes = data.get('notes')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO appointments(patient_id, doctor_id, appointment_date, status, notes) VALUES (%s, %s, %s, %s, %s)",
                    (patient_id, doctor_id, appointment_date, status, notes))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Appointment created"}), 201

if _name_ == '_main_':
    app.run(debug=True)