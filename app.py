from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Intern App</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            h1 {
                color: white;
                font-size: 48px;
                text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
                padding: 20px 40px;
                border: 2px solid white;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <h1>Hello from DevOps Intern 🚀</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
