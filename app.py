from flask import Flask, request, render_template

app = Flask(__name__)

def check_password_strength(password):
    import re

    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    if length_criteria and upper_case_criteria and lower_case_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and ((upper_case_criteria and lower_case_criteria) or (digit_criteria and special_char_criteria)):
        return "Moderate"
    else:
        return "Weak"

@app.route('/', methods=['GET', 'POST'])
def index():
    password_strength = None
    password_input = None
    if request.method == 'POST':
        password = request.form['password']
        password_strength = check_password_strength(password)
        password_input = password
    
    return render_template('index.html', password_strength=password_strength, password_input=password_input)

if __name__ == '__main__':
    app.run(debug=True)
