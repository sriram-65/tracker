from flask import Flask
from admin.admin import Ad
from taking.take import Take
from taking.user import Use
app = Flask(__name__)

app.register_blueprint(Ad)
app.register_blueprint(Take)
app.register_blueprint(Use)



app.secret_key = 'MuruganThunai'

if __name__ == "__main__":
    app.run(debug=True)