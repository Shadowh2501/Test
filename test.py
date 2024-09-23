from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

# Define the HTML page for the challenge
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CTF Challenge</title>
</head>
<body style="text-align: center; margin-top: 50px;">
    <h1>CTF Challenge</h1>
    <p>{{ message }}</p>
    {% if flag %}
    <p><strong>Flag: {{ flag }}</strong></p>
    {% endif %}
</body>
</html>
'''

@app.route('/')
def index():
    # Check for the cookie 'T1m3-P3r10d' with the value 'infinity'
    cookie_value = request.cookies.get('T1m3-P3r10d')
    if cookie_value == 'infinity':
        message = "Here is your flag!"
        flag = "CTF{Y0u_F0und_Th3_Flag!}"
    else:
        message = "You must wait for a <code>T1m3-P3r10d </code> of infinity to get the flag."
        flag = None

    # Render the page
    return render_template_string(html_template, message=message, flag=flag)

if __name__ == '__main__':
    app.run(debug=True)
    