from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined Knowledge Base
RESPONSES = {
    "timing": "College timings are 9:00 AM to 4:30 PM, Monday to Friday.",
    "time": "College timings are 9:00 AM to 4:30 PM, Monday to Friday.",
    "attendance": "Students should maintain a minimum of 75% attendance to be eligible for examinations.",
    "course": "Our college offers B.Tech, M.Tech, BCA, MCA, and MBA programs across various specializations.",
    "exam": "Mid-term exams take place in October and March. End-semester exams are in December and May.",
    "library": "The central library is open from 8:00 AM to 8:00 PM on working days. You can borrow up to 3 books using your Student ID.",
    "timetable": "You can access your class schedule on the student portal under 'Academics -> Timetable'.",
    "department": "Major departments include Computer Science, Electronics, Mechanical, Civil, and Information Technology.",
    "contact": "You can contact the administration office at admin@college.edu or call +1 (800) 123-4567.",
    "hello": "Hello! How can I help you today? You can ask about timings, attendance, exams, library, etc.",
    "hi": "Hi there! Feel free to ask me any questions about college operations or courses."
}

def get_bot_response(user_msg):
    clean_msg = user_msg.lower()
    for key, val in RESPONSES.items():
        if key in clean_msg:
            return val
    return "I'm sorry, I don't have information on that. Try asking about timings, attendance, exams, library, courses, or contact info!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
