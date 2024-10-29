# db.py

from main import create_app, db

app = create_app()

# Create the application context for database operations
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
