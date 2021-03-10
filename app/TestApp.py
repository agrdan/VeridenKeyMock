from flask import request, jsonify, Blueprint, render_template, flash, redirect, url_for, session, json, Response, send_from_directory, send_file, make_response

test = Blueprint('test', __name__)



class Test:

    @staticmethod
    @test.route("/test", methods=['GET'])
    def test():
        resp = {
            'hello': 'world!'
        }
        return jsonify(resp)