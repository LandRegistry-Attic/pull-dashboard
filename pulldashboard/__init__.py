import os, logging
from flask import Flask

from config import CONFIG_DICT

app = Flask(__name__)

app.config.update(CONFIG_DICT)

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

app.logger.info("\nConfiguration\n%s\n" % app.config)

# Repositories not to show info for
excludedRepos = [line.rstrip('\n') for line in open(app.config['REPOSITORY_BLACKLIST'])]
