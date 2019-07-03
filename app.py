from flask import Flask, render_template, jsonify
import json
# Assume data comes from somewhere else
data = {
  "data": [
    {
      "id": "1",
      "name": "Tiger Nixon",
      "position": "System Architect",
      "salary": "$320,800",
      "start_date": "2011/04/25",
      "office": "Edinburgh",
      "extn": "5421"
    },
    {
      "id": "2",
      "name": "Garrett Winters",
      "position": "Accountant",
      "salary": "$170,750",
      "start_date": "2011/07/25",
      "office": "Tokyo",
      "extn": "8422"
    }]
}
 
app = Flask(__name__)
 
@app.route('/index')
@app.route('/')
def index():
  # return render_template('index.html',data=data)
  return render_template('index.html',data=json.dumps(data))
 
if __name__ == '__main__':
  app.run(debug=True)