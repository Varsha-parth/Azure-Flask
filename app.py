from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h2> HR Dashboard Report </h2>
<iframe title="HR_Dashboard" width="1140" height="541.25" src="https://msit.powerbi.com/reportEmbed?reportId=c057d48e-6895-4684-87c5-19bf61f8f0fc&autoAuth=true&ctid=72f988bf-86f1-41af-91ab-2d7cd011db47&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9kZi1tc2l0LXNjdXMtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D" frameborder="0" allowFullScreen="true"></iframe>
"""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)