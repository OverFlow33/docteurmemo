import logging
from django.conf import settings

logger = logging.getLogger('prediction_logger')

def log_prediction_request(user, url, method, response):    
    logger.info(f'<User: {user.id}> ({method.upper(): <6}) [{response.status_code}] [{url}]  {response.reason}')
