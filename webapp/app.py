#!/usr/bin/env python3
'''
    app.py
    Lucie Wolf and Yuelin Kuang
    9 Nov 2022

    Web application project for CS257.
'''

import argparse
import flask
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/games')
def show_games():
    return flask.render_template('games_main.html')

@app.route('/stats')
def show_stats():
    return flask.render_template('stats_main.html')

@app.route('/help')
def show_help():
    f = open('doc/api-design.txt')
    text = f.read()
    print(text)
    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application demonstrating templates.')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
