from flask import Flask, request, Response
from socket import *
import os

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming():
	logger.debug("received request. post data: {0}".format(request.get_data()))
	# handle the request here
	return Response(status=200)


@app.route('/home')
def home():
	return 'Test'

context = ('server.crt', 'server.key')

if __name__== '__main__':
	app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
