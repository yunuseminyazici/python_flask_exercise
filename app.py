from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mapping_suggestion', methods=['GET', 'POST'])
def mapping_suggestion():
    suggestion = [{'name':'datapoint1', 'node':'https://www.examle.com/datapoint1'},{'name':'datapoint2', 'node':'https://www.examle.com/datapoint2'}]
    return render_template('mapping_suggestion.html', suggestion=suggestion)    

@app.route('/mappings', methods=['GET', 'POST'])
def mappings():
    name = request.form.getlist('name')
    node = request.form.getlist('node')
    selected_mappings = list(zip(name, node))
    response_data = [{'name': name, 'node': node} for name, node in selected_mappings]
    #json_response = json.dumps(response_data)
    colours = ['red', 'blue', 'green']
    return render_template('mapping.html', suggestion=response_data, colours=colours)

@app.route('/mapping_suggestion_accept', methods=['POST'])
def mapping_suggestion_accept():
    suggestion = request.form
    mapping={}
    for item in suggestion:
        mapping[item]=suggestion[item]
    return render_template('mapping_suggestion_accept.html', mapping=mapping)

if __name__ == '__main__':
    app.run(debug=True)
