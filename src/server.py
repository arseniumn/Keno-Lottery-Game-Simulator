# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:53:38 2020

@author: arseniumn
"""
import random
from ticket import Ticket
               #1       2       3       4       5       6       7       8       9      10        11        12
paytable = [
             [  0,      0,      0,      0,      0,      0,      0,      0,      0,      2,        2,        4], #0 out of
             
             [2.5,      1,      0,      0,      0,      0,      0,      0,      0,      0,        0,        0], #1 out of
            
             [  0,      5,    2.5,      1,      0,      0,      0,      0,      0,      0,        0,        0], #2 out of
              
             [  0,      0,     25,      4,      2,      1,      1,      0,      0,      0,        0,        0], #3 out of
             
             [  0,      0,      0,    100,     20,      7,      3,      2,      1,      0,        0,        0], #4 out of
             
             [  0,      0,      0,      0,    450,     50,      20,    10,      5,      2,        1,        0], #5 out of
             
             [  0,      0,      0,      0,      0,   1600,     100,    50,     25,     20,       10,        5], #6 out of
             
             [  0,      0,      0,      0,      0,      0,    5000,  1000,    200,     80,       50,       25], #7 out of
             
             [  0,      0,      0,      0,      0,      0,      0,   15000,  4000,    500,      250,      150], #8 out of
             
             [  0,      0,      0,      0,      0,      0,      0,       0,  40000,  10000,    1500,     1000], #9 out of
             
             [  0,      0,      0,      0,      0,      0,      0,       0,      0,  100000,   15000,    2500], #10 out of
             
             [  0,      0,      0,      0,      0,      0,      0,       0,      0,       0,  500000,   25000], #11 out of
             
             [  0,      0,      0,      0,      0,      0,      0,       0,      0,       0,     0,   1000000]] #12 out of

data = {}
class Server:
    def __init__(self):
          self.numbers = set()
          self.data  = dict()          
          for i in range (len(paytable)):
              for j in range (len(paytable[i])):
                  key = str(paytable[i][j])
                  self.data.update({key : 0})
             
    def generateNumbers(self):
        t=0
        self.numbers.clear()
        while(t<20):
            aNumber = random.randint(1,80)
            while(aNumber in self.numbers):
                aNumber = random.randint(1,80)
            self.numbers.add(aNumber)
            t += 1
            
    # It is used for one draw to show it in console
    def getNumbers(self):
        return self.numbers
    
    def scanTicket(self, ticket):
        matched = 0      
        #Check how many of the numbers of ticket have been matched with server's
        temp = list(ticket.getTicketNumbers())
        for i in range (len(temp)):
            if(temp[i] in self.numbers):
                matched += 1
                
        # Get the payment for specific number of matched numbers
        payment = paytable[matched][ticket.getDifferentNumbers()-1]
        
        # Update value of dictionary
        newValue = self.data.get(str(payment)) + 1
        self.data.update({str(payment) : newValue})
        
        #print("Matched : ",matched)
        #print("Win : ",paytable[matched][ticket.getDifferentNumbers()-1])
        return payment

    def getDataSet(self):
        return self.data
    