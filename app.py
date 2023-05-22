from os import path
from pathlib import Path

from flask import Flask, render_template
from flask_frozen import Freezer


template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
#app.config['FREEZER_BASE_URL'] = environ.get('CI_PAGES_URL')
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)

#@freezer.register_generator
#def catch_all():
#    for page in Path('wiki/pages').iterdir():
#        if str(page).endswith('.html'):
#            yield {'path': f'{page.stem}.html'}

@app.cli.command()
def freeze():
    freezer.freeze()

@app.cli.command()
def serve():
    freezer.run()

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/<page>')
def pages(page):
    try:
        #each_page = str(Path('pages'))
        #return render_template(("pages/" + (page.lower() + '.html')).lower())
        return render_template("pages/" + (page + '.html'))
    except:
        return "Error"

#@app.route('/', defaults={'path': 'index.html'})
#@app.route('/<path:path>')
#def catch_all(path):
#    if path.endswith('.html'):
#        path = f'pages/{path.lower()}'
#    else:
#        path = f'pages/{path.lower()}.html'
#    try:
#        return render_template(path)
#    except:
#        return abort(404)

# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    app.run(port=8080)
