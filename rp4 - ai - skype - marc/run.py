#!flask/bin/python
from app import app
HOST='0.0.0.0'

app.run(debug=True,host=HOST)

