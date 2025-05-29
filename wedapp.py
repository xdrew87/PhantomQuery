from flask import Flask, request, render_template
from modules.phone_lookup import lookup_number
from modules.email_lookup import lookup_email_breach

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    phone_result = None
    email_result = None

    if request.method == 'POST':
        if 'phone' in request.form and request.form['phone']:
            phone_result = lookup_number(request.form['phone'])
        if 'email' in request.form and request.form['email']:
            email_result = lookup_email_breach(request.form['email'])

    return render_template('index.html', phone_result=phone_result, email_result=email_result)

if __name__ == '__main__':
    app.run(debug=True)
