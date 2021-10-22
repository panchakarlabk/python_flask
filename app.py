from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

flaskAppInstance = Flask(__name__)

if __name__ == '__manin__':
    logger.debug("Starting the appliction ")
    from api import *
    flaskAppInstance.run(host="0.0.0.0", port=5000, debug=True, use_reloder=True)
