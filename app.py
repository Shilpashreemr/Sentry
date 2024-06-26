import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# Initialize Sentry
sentry_sdk.init(
    dsn="https://34158ae445e79da449d800140861fe94@o4507497998647296.ingest.us.sentry.io/4507498007560192",
    integrations=[FlaskIntegration()]
)

# Example Flask application
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    
    division_by_zero = 1 / 0  
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=False)
