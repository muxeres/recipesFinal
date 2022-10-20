from recipes_app import app
from recipes_app.controllers import login_registration_controller,recipe_controller

if __name__ == "__main__":
    app.run(debug=True)