from flask import Flask, render_template, request
from gradio_client import Client

app = Flask(__name__)

client = Client("Qwen/Qwen2-72B-Instruct")

@app.route('/', methods=['GET', 'POST'])
def index():
    jd_result = None
    if request.method == 'POST':
        Title = request.form['Title']
        work_mode = request.form['work_mode']
        location = request.form['location']
        Specific = request.form.get('Specific', '')
       

        query = (f"Designation: {Title}\n"
                 f"Work Mode: {work_mode}\nLocation: {location}\n"
                 f"Tech Stacks/Tools: {Specific}\n")

        result = client.predict(
            query=query,
            history=[],
            system="YOU ARE A PERFECT JD GENERATOR.",
            api_name="/model_chat"
        )
        jd_result = result[1][0][1] if result and result[1] else None

    return render_template('index.html', jd_result=jd_result)

if __name__ == '__main__':
    app.run(debug=True)