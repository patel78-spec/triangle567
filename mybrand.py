from datetime import datetime

def my_brand(name: str):
    now = datetime.now()
    print('=*=*=*= Dhruv Patel =*=*=*=')
    print('=*=*=*= Course 2023-SSW567-WS =*=*=*=') 
    print('=*=*=*= {} =*=*=*='.format(name))
    print('=*=*=*= Function called on {} =*=*=*='.format(now.strftime("%d/%m/%Y %H:%M:%S")))