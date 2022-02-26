from cgitb import lookup
from logging import logMultiprocessing
from loguru import logger       
import httpx


r = httpx.get('http://ec2-18-222-97-186.us-east-2.compute.amazonaws.com:8000')
logger.info(r)
logger.info(r.status_code)
logger.info(r.headers)
logger.info(r.text)