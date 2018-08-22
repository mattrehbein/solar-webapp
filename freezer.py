from flask_frozen import Freezer
from app import app, Solar

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def show():
    for garden in Solar.query.all():
        yield { 'index': garden.index }

if __name__ == '__main__':
    freezer.freeze()