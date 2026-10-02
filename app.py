from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for login sessions
app.secret_key = "smart-q-secret-key"


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- PATIENT REGISTRATION ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        mobile = request.form.get("mobile")
        email = request.form.get("email")
        password = request.form.get("password")
        age = request.form.get("age")
        gender = request.form.get("gender")
        address = request.form.get("address")
        emergency_contact = request.form.get("emergency_contact")

        # Hash password
        password_hash = generate_password_hash(password)

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        try:

            cursor.execute("""
                INSERT INTO patients
                (
                    name,
                    mobile,
                    email,
                    password,
                    age,
                    gender,
                    address,
                    emergency_contact
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name,
                mobile,
                email,
                password_hash,
                age,
                gender,
                address,
                emergency_contact
            ))

            connection.commit()

        except sqlite3.IntegrityError:

            connection.close()

            return "Email or mobile number already exists."

        connection.close()

        return "Patient account created successfully!"

    return render_template("register.html")


# ---------------- PATIENT LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        connection = sqlite3.connect("database.db")

        # Allows us to access columns by name
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM patients WHERE email = ?",
            (email,)
        )

        patient = cursor.fetchone()

        connection.close()

        # Check patient and password
        if patient and check_password_hash(
            patient["password"],
            password
        ):

            # Save patient information in session
            session["patient_id"] = patient["id"]
            session["patient_name"] = patient["name"]

            return redirect(url_for("patient_dashboard"))

        return render_template(
            "login.html",
            error="Invalid email or password."
        )

    return render_template("login.html")


# ---------------- PATIENT DASHBOARD ----------------

@app.route("/patient/dashboard")
def patient_dashboard():
    if "patient_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM tokens
        WHERE patient_id = ?
        ORDER BY id DESC
        LIMIT 1
    """, (session["patient_id"],))

    token = cursor.fetchone()
    connection.close()

   
# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ---------------- RUN APP ----------------

@app.route("/generate-token", methods=["GET", "POST"])
def generate_token():
    if "patient_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        # Create token table if it does not exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tokens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                token_number INTEGER NOT NULL,
                department TEXT NOT NULL,
                doctor TEXT NOT NULL,
                queue_type TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Get the next token number
        cursor.execute("""
            SELECT MAX(token_number)
            FROM tokens
            WHERE DATE(created_at) = DATE('now')
        """)

        result = cursor.fetchone()
        last_token = result[0] if result[0] else 0
        new_token = last_token + 1

        # Temporary demo values
        department = "General Medicine"
        doctor = "Dr. Sharma"
        queue_type = "normal"

        cursor.execute("""
            INSERT INTO tokens
            (patient_id, token_number, department, doctor, queue_type, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            session["patient_id"],
            new_token,
            department,
            doctor,
            queue_type,
            "waiting"
        ))

        connection.commit()
        connection.close()

        render_template(
    "token_success.html",
    token_number=new_token,
    department=department,
    doctor=doctor,
    queue_type=queue_type
)
        return render_template("generate_token.html")


if __name__ == "__main__":
    app.run(debug=True)