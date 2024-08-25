from flask import Flask, render_template, request, jsonify,g
from flask_cors import CORS
import sqlite3
import os
import openai  # Import the OpenAI module
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
DATABASE = 'database.db'

# Connect to SQLite Database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/chat', methods=['POST'])
#def chat():
 #   user_message = request.json.get('message')
 #   if user_message:
  #      response = openai.ChatCompletion.create(
 #           model="gpt-3.5-turbo",  # or "gpt-4" if available
  #          messages=[
  #              {"role": "system", "content": "You are a helpful assistant."},
  #              {"role": "user", "content": user_message}
  #          ]
  #      )
   #     bot_reply = response['choices'][0]['message']['content'].strip()
  #      print("Bot reply:", bot_reply)
  #      return jsonify({"reply": bot_reply})
   # return jsonify({"reply": "Sorry, I didn't understand that."})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response['choices'][0]['message']['content'].strip()
        print("Bot reply:", bot_reply)  # This will help debug by showing the bot's reply in the terminal
        return jsonify({"reply": bot_reply})
    return jsonify({"reply": "Sorry, I didn't understand that."})


@app.route('/welcome', methods=['GET'])
def welcome_message():
    return jsonify({"message": "Hi there! I'm here to help you connect with top-rated contractors. How can I assist you today?"})

@app.route('/service_inquiry', methods=['POST'])
def service_inquiry():
    data = request.json
    service_type = data.get('service_type')
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    db = get_db()
    db.execute("INSERT INTO inquiries (service_type, name, email, phone) VALUES (?, ?, ?, ?)",
               (service_type, name, email, phone))
    db.commit()

    # Example: Save to a database here
    
    return jsonify({"message": f"Thank you, {name}. I've recorded your interest in {service_type}. How would you like to proceed?"})

@app.route('/plumbing_services', methods=['GET'])
def get_plumbing_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM plumbing_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/plumbing_services/<int:service_id>', methods=['GET'])
def get_plumbing_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM plumbing_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/electrical_services', methods=['GET'])
def get_electrical_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM electrical_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/electrical_services/<int:service_id>', methods=['GET'])
def get_electrical_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM electrical_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/hvac_services', methods=['GET'])
def get_hvac_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM hvac_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/hvac_services/<int:service_id>', methods=['GET'])
def get_hvac_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM hvac_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/carpentry_services', methods=['GET'])
def get_carpentry_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM carpentry_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/carpentry_services/<int:service_id>', methods=['GET'])
def get_carpentry_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM carpentry_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/painting_drywall_services', methods=['GET'])
def get_painting_drywall_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM painting_drywall_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/painting_drywall_services/<int:service_id>', methods=['GET'])
def get_painting_drywall_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM painting_drywall_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/roofing_services', methods=['GET'])
def get_roofing_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM roofing_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/roofing_services/<int:service_id>', methods=['GET'])
def get_roofing_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM roofing_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/flooring_services', methods=['GET'])
def get_flooring_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM flooring_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/flooring_services/<int:service_id>', methods=['GET'])
def get_flooring_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM flooring_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/masonry_services', methods=['GET'])
def get_masonry_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM masonry_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/masonry_services/<int:service_id>', methods=['GET'])
def get_masonry_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM masonry_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/window_door_services', methods=['GET'])
def get_window_door_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM window_door_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/window_door_services/<int:service_id>', methods=['GET'])
def get_window_door_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM window_door_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/landscaping_services', methods=['GET'])
def get_landscaping_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM landscaping_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/landscaping_services/<int:service_id>', methods=['GET'])
def get_landscaping_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM landscaping_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)

@app.route('/handyman_services', methods=['GET'])
def get_handyman_services():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM handyman_services")
    services = cur.fetchall()
    return jsonify(services)

@app.route('/handyman_services/<int:service_id>', methods=['GET'])
def get_handyman_service_by_id(service_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM handyman_services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    return jsonify(service)


@app.route('/service_options', methods=['GET'])
def service_options():
    options = {
        "form": "Fill in a Form",
        "call": "Call a Contractor",
        "appointment": "Set an Appointment"
    }
    return jsonify(options)

@app.route('/contractors', methods=['GET'])
def get_contractors():
    contractors = [
        {"id": 1, "name": "John's Plumbing", "phone": "555-1234", "service": "Plumbing"},
        {"id": 2, "name": "Electric Pros", "phone": "555-5678", "service": "Electrical"},
        {"id": 3, "name": "HVAC Masters", "phone": "555-8765", "service": "HVAC"},
        {"id": 4, "name": "Carpentry Experts", "phone": "555-4321", "service": "Carpentry"}
    ]
    return jsonify(contractors)

@app.route('/fill_form', methods=['POST'])
def fill_form():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    selected_contractors = data.get('contractors')

    # Process form submission (you could save this to your database)

    return jsonify({"message": "Form submitted successfully", "contractors": selected_contractors})

@app.route('/call_contractor', methods=['POST'])
def call_contractor():
    contractor_id = request.json.get('contractor_id')

    # Here you would typically trigger some action, like initiating a call

    return jsonify({"message": f"Calling contractor with ID {contractor_id}..."})

@app.route('/set_appointment', methods=['POST'])
def set_appointment():
    data = request.json
    contractor_id = data.get('contractor_id')
    appointment_time = data.get('appointment_time')

    # Process appointment scheduling (you could save this to your database)

    return jsonify({"message": f"Appointment set with contractor {contractor_id} at {appointment_time}"})


@app.route('/faq', methods=['POST'])
def handle_faq():
    question = request.json.get('question')
    answer = gpt4_faq_handler(question)
    return jsonify({"answer": answer})

def gpt4_faq_handler(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=150
    )
    answer = response['choices'][0]['message']['content'].strip()
    print("FAQ answer:", answer)
    return answer
   # return response['choices'][0]['message']['content'].strip()


if __name__ == "__main__":
    app.run(debug=True,port=5500)
