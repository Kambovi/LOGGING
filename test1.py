import logging
logging.basicConfig(filename="test2.log",level=logging.INFO)
logging.info("this is my fisrt log")
l= [1,2,3,4,5,6,7,8]
for i in l:
    if i=="2":
        logging.INFO(l)