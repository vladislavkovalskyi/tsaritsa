from tsaritsa import app
from tsaritsa.blueprints import index_blueprint, send_message_blueprint

app.register_blueprint(index_blueprint)
app.register_blueprint(send_message_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
