from flask import Flask, render_template, request, Response, redirect
from analyzer import data, get_sample_and_delete

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html', sheets=data.keys())

@app.route('/question/', methods=['POST'])
def question():
    full_question, count_question = get_sample_and_delete(sheet_name=request.form['sheet'], data_frame_dict=data)
    return render_template('question.html',
                        full_name=full_question.iloc[0, 0],
                        job=full_question.iloc[0, 1],
                        post=full_question.iloc[0, 2],
                        question=full_question.iloc[0, 3],
                        count_question=count_question,
                        sheet=request.form['sheet'])