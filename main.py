from flask import Flask
app = Flask('app')

@app.route('/')
def welcome():
  return 'Welcome page - Sync Contacts button'


@app.route('/dashboard')
def dashboard():
  return 'Main Dashboard'

app.run(host='0.0.0.0', port=8080, debug=True)