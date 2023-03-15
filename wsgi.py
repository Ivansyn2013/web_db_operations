from app import  app
from config.config import DeveloperPostgresConfig

if __name__ == '__main__':

    app.run(host='0.0.0.0',
            port=5003,
            debug=DeveloperPostgresConfig.FLASK_DEBUG)