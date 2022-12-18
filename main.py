from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
import json
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '1abhigup6@gmail.com'
app.config['MAIL_PASSWORD'] = 'lyfmjwyasriaiwfx'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

print("Connection made")

# Database configuration
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'AxpaluMpIg'
app.config['MYSQL_PASSWORD'] = 'Ie4s0L15iC'
app.config['MYSQL_DB'] = 'AxpaluMpIg'
mysql = MySQL(app)

# Route to default homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to send emails and send data to database
@app.route('/submit', methods=['GET', 'POST'])
def submit_email():
    # Add entry to the db
    email = request.form.get('email')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO loi_email(email) VALUES ('{}')".format(email))
    mysql.connection.commit()
    cur.close()
    msg = Message('New Interest', sender='1abhigup6@gmail.com',
                  recipients=['foxlearner@outlook.in'])
    msg.body = "New email " + email
    mail.send(msg)

    return redirect('/')

# Route for pitch page
@app.route('/pitch')
def pitch():
    return render_template('pitch.html')


if __name__ == '__main__':
    app.run(debug=True)
