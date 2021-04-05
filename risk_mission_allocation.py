

import yagmail
import random
from os import environ

def set_new_world_order():
    
    RISK_APP_PASSWORD = environ['RISK_APP_PASSWORD']
    
    RISK_SENDER = environ['RISK_SENDER']
    
    RISK_EMAILS_TO = environ['RISK_EMAILS_TO']
    
    emails = RISK_EMAILS_TO.split(', ')
    
    subject = 'Check out your destiny !!!'
    
    colours = ['green', 'blue', 'indigo', 'yellow', 'orange']
    colours = random.sample(colours, len(colours))
    
    missions = ['Destroy green or else 24 territories',
               'Destroy yellow or else 24 territories',
               'Destroy indigo or else 24 territories',
               'Destroy blue or else 24 territories',
               'Destroy orange or else 24 territories',
               'Occupy 24 territories',
               'Occupy 18 territories with at least 2 troops in each',
               'Occupy Asia and Africa',
               'Occupy North America and Africa',
               'Occupy North America and Australia',
               'Occupy Asia and South America',
               'Occupy Europe and Australia']
    missions = random.sample(missions, len(missions))
    
    kadro = input('klasik kadro? [y/n]:').lower()
    if kadro != 'y':
        new_kadro = input('Enter username parts of the gmail addresses of the players separated with a comma, e.g. aliveli, mehmet for aliveli@gmail.com, mehmet@gmail.com:')
        new_kadro = new_kadro.replace(" ", "").split(',')
        emails = ['{}@gmail.com'.format(name) for name in new_kadro]
    
    n = len(emails)
    emails = random.sample(emails, n)
    ls_final = [random.sample(colours, n), random.sample(missions, n)]
    
    for i in range(len(emails)):
        content = ['Your colour: ', ls_final[0][i], 'Your mission: ', ls_final[1][i]]
        to = emails[i]

        with yagmail.SMTP(RISK_SENDER, RISK_APP_PASSWORD) as yag:
            yag.send(to, subject, content)
            print('Sent email to {} successfully'.format(emails[i]))


set_new_world_order()







