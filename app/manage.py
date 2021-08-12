from project import app
import os

if __name__ == "__main__":
    if os.getenv("FLASK_ENV") == "development":
        app.run(
            debug=True,
            host='10.10.0.10',
            port=3031
        )
    else:
        app.run()