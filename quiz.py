from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


questions = [
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
    {"question": "What does GPU stand for?", "answer": "graphical processing unit"},
    {"question": "What does RAM stand for?", "answer": "random access memory"},
    {"question": "What does ROM stand for?", "answer": "read only memory"},
    {"question": "Mouse is an input device or output device?", "answer": "input device"},
]

@app.route('/')
def quiz():
    return render_template('quiz.html')


@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_index = data['question_index']
    user_answer = data['answer'].lower()

    correct_answer = questions[question_index]['answer'].lower()
    result = user_answer == correct_answer

    return jsonify({"result": result})


@app.route('/get_question/<int:question_index>', methods=['GET'])
def get_question(question_index):
    if question_index < len(questions):
        return jsonify(questions[question_index])
    else:
        return jsonify({"error": "No more questions"}), 404

if __name__ == '__main__':
    app.run(debug=True)
