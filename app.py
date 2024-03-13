from flask import Flask, render_template, request, redirect, flash
from database import Database
import time


app = Flask(__name__)


@app.route('/')
def home():
    ########
    # todo #
    ########

    return "Hello World!"


@app.route('/task/create', methods=['post'])
def create_task():
    ########
    # todo #
    ########

    return {"message": "fail"}


@app.route('/task/update/status/<task_id>')
def check_task(task_id):
    ########
    # todo #
    ########

    return {"message": "fail"}


@app.route('/task/update/content/<task_id>', methods=['post'])
def update_task(task_id):
    ########
    # todo #
    ########

    return {"message": "fail"}


@app.route('/task/delete/<task_id>')
def delete_task(task_id):
    ########
    # todo #
    ########

    return {"message": "fail"}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
