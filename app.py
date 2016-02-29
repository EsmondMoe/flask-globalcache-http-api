import macros
from flask import Flask, jsonify, make_response
import ssl
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

macro = macros.Macros()


@auth.get_password
def get_password(username):
    if username == 'user':
        return 'password'
    return None


@app.route('/', methods=['GET'])
@auth.login_required
def root():
    return make_response(jsonify({'status': 'ok'}), 200)


@app.route('/tvtoggle', methods=['GET'])
@auth.login_required
def tvtoggle():
    macro.tv_toggle()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/cableboxtoggle', methods=['GET'])
@auth.login_required
def cableboxtoggle():
    macro.cable_box_toggle()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/allon', methods=['GET'])
@auth.login_required
def allon():
    macro.all_on()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/alloff', methods=['GET'])
@auth.login_required
def alloff():
    macro.all_off()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/moviemode', methods=['GET'])
@auth.login_required
def moviemode():
    macro.movie_mode()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/tvmode', methods=['GET'])
@auth.login_required
def tvmode():
    macro.tv_mode()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/fox', methods=['GET'])
@auth.login_required
def fox():
    macro.fox()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/hgtv', methods=['GET'])
@auth.login_required
def hgtv():
    macro.hgtv()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/discovery', methods=['GET'])
@auth.login_required
def discovery():
    macro.discovery()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/history', methods=['GET'])
@auth.login_required
def history():
    macro.history()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/amc', methods=['GET'])
@auth.login_required
def amc():
    macro.amc()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/travel', methods=['GET'])
@auth.login_required
def travel():
    macro.travel()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/weather', methods=['GET'])
@auth.login_required
def weather():
    macro.weather()
    return make_response(jsonify({'status': 'accepted'}), 202)


@app.route('/sonosmode', methods=['GET'])
@auth.login_required
def sonosmode():
    macro.sonos_mode()
    return make_response(jsonify({'status': 'accepted'}), 202)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'unauthorized access'}), 401)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.load_cert_chain('keys/key.crt', 'keys/key.key')
    app.run(host='127.0.0.1', port=443, ssl_context=context, threaded=True, debug=True)
