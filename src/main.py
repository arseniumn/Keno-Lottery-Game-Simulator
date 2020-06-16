# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:48:49 2020

@author: arseniumn
"""
import os
from ticket import Ticket
from server import Server
import pandas as pd
import collections

# Simulation of KENO with 100k tickets
# User can change it
NUMBER_OF_TICKETS = 100000

# Simulation of KENO with 144 DRAWS
# The DRAWS are set to 1 but you can set it to 144
# because each DRAW is applied every 5 minutess
# DRAWS/hour = 60 min / 5 min = 12 DRAWS/HOUR
# DRAWS/12 hour  = 12 x 12 = 144 DRAWS/DAY(half)
NUMBER_OF_DRAWS = 1

# Minimum BET that is declared by the owner of the game
# Don' change it
BET = 1

# Multiplier is 1
# User can change it by removing the comment from Ticket class where
# multiplier is generated randomly
MULTIPLIER = 0.5

def main():
    PayOut = 0
    PayIn = 0
    
    # Initialize Server Object
    s = Server()

    # For each DRAW
    for i in range(NUMBER_OF_DRAWS):    
        
       # Server generates the 20 lucky numbers
        s.generateNumbers()
        #print(s.getNumbers())
        
        # Generate tickets with random numbers per DRAW
        for j in range (NUMBER_OF_TICKETS):
            t = Ticket(j)
            t.generateTicketNumbers()
            
            # The player pays for the ticket
            PayIn += (BET*MULTIPLIER)

            # Ticket scan-evaluation by passing the tickets to Server
            PayOut += (s.scanTicket(t)*MULTIPLIER*BET)
    
    # Return To Player calculation    
    RTP = (PayOut/PayIn) * 100
    print("General Return to Player (RTP) from Keno is : ", round(RTP,3), "%")
    
     # Add probability in auxiliary list
    aux = []
    for val in s.getDataSet().values():
        aux.append(val/NUMBER_OF_TICKETS)
        
    # Create the dataset for dataframe for the Excel
    dataset = { 
                "Payment" : list(s.getDataSet().keys()),
                "Probability" : aux
              }
    df = pd.DataFrame(dataset, columns = ["Payment","Probability"])
    generateExcelFile(df)


def generateExcelFile(df):  
    # Export probabilities to Excel file
    df.to_excel (r'probs.xlsx', index = False, header=True)
    os.system("start EXCEL.EXE probs.xlsx")
    
if __name__ == "__main__":
    main()