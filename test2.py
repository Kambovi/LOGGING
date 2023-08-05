# make sure of spellings
import logging

logging.basicConfig(filename="test2.log",level=logging.DEBUG, format='%(asctime)s %(message)s %(levelname)s')
logging.debug("log with time stamp")

l=[1,2,3,4,5,0]
for i in l:
    logging.info("we are inside the loop")
    if i =="2":
        logging.info(l)
