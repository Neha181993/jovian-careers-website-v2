from re import template
from flask import Flask, render_template, jsonify
from database import load_job_from_db

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$100,000'
}]


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM jobs")
        jobs = []
        for row in result:
            jobs.append(row)
        return jobs



@app.route("/")
def hello():
    JOBS1= load_jobs_from_db()## This needs to be added below as of now it is not working coz we don't have db
    return render_template('home.html',
                           jobs=JOBS,
                           company_name="Jovian Careers")


@app.route("/api/jobs")
def list_jobs():
    JOBS1= load_jobs_from_db()## This needs to be added below as of now it is not working coz we don't have db
    return jsonify(JOBS)

## To print specific ID 
@app.route("/api/jobs/<id>")
def show_job():
    JOBS=load_job_from_db(id)
    ## This needs to be added below as of now it is not working coz we don't have db
    return jsonify(JOBS)


@app.route("/api/jobs/<id>")
def show_job_temlpate():
    JOBS=load_job_from_db(id)
    ##This needs to be added below as of now it is not working coz we don't have db
    if not JOBS:
        return "Not Found", 404
    return render_template('jobpage.html',job=JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
