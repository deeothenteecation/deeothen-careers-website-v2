from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Laundry Supervisor',
  'location': 'Manila, Philippines',
  'salary': 'Php 60,000'
}, {
  'id': 2,
  'title': 'Meal Researcher/Designer',
  'location': 'Remote',
  'salary': 'Php 40,000'
}, {
  'id': 3,
  'title': 'House Sanitation Manager',
  'location': 'Manila, Philippines',
  'salary': 'Php 100,000'
}, {
  'id': 4,
  'title': 'Massage Specialist',
  'location': 'Manila, Philippines',
  'salary': 'Very Attractive!! (negotiable)'
}]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='DeeothenTC Enterprise')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)