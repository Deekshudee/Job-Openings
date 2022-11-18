from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id' : 1,
  'postion': 'data analyst',
  'location':'banglore India',
  'salary': 'Rs. 10,00,000'
},
{
  'id': 2,
  'postion':'data engineer',
  'location':'delhi India',
  'salary': 'Rs. 12,00,000'
},
{
  'id':3,
  'postion':'backend engineer',
  'location':'pune India',
  'salary':'Rs. 15,00,000'
}
]

@app.route("/api/jobs")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

                        

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)

