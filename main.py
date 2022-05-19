from flask import Flask, redirect, render_template, flash, session
app = Flask('app')

app.config['SECRET_KEY'] = 'qEChL7R3SpF72cEA'

@app.route('/')
def index():
  return render_template('index.html')
  

@app.route('/flashing')
def flashing():
    flash('Sucesso', 'success')    
    return render_template('flashing.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)