from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mappings', methods=['GET', 'POST'])
def mappings():
    suggestion = ['book1', 'book2', 'book3']
    colours = ['red', 'blue', 'green']
    return render_template('mapping.html', suggestion=suggestion, colours=colours)

@app.route('/mapping_suggestion_accept', methods=['POST'])
def mapping_suggestion_accept():
    suggestion = request.form
    mapping={}
    for item in suggestion:
        mapping[item]=suggestion[item]
    return render_template('mapping_suggestion_accept.html', mapping=mapping)

if __name__ == '__main__':
    app.run(debug=True)
