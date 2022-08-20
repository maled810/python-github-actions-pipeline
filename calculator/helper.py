import logging
import sys


logger = logging.getLogger()
logger.setLevel(logging.ERROR)

out_handler = logging.StreamHandler(sys.stdout)

log_fmt = logging.Formatter("Logged: %(levelname)s %(asctime)s: in %(funcName)s on line %(lineno)d %(message)s --" 
                            " Full Path: %(pathname)s")
out_handler.setFormatter(log_fmt)

logger.addHandler(out_handler)
