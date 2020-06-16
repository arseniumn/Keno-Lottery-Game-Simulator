# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:53:38 2020

@author: arseniumn
"""
import random

multipliers = [1,2,3,4,5,6,7,8,9,10]

class Ticket:
      def __init__(self, ID):
          self.ID = ID
          self.numbers_set = set()
          self.diff_numbers = random.randint(1,12)    
          #self.multiplier = multipliers[random.randint(0,len(multipliers)-1)]
          
      def generateTicketNumbers(self):
           t=0
           while(t<self.diff_numbers):
               aNumber = random.randint(1,80)
               while(aNumber in self.numbers_set):
                   aNumber = random.randint(1,80)
               self.numbers_set.add(aNumber)
               t += 1

      def getTicketNumbers(self):
        return self.numbers_set
    
      def getDifferentNumbers(self):
        return self.diff_numbers