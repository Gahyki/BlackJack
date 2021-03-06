import csv
import math

f = open('blkjckhands.csv')
csv_f = csv.reader(f)
next(csv_f)

#Declare all variables for each different dealer upcard sum (2-10)
t1obeywin = 0
t1obeytotal = 0
t1disobeywin = 0
t1disobeytotal = 0

t2obeywin = 0
t2obeytotal = 0
t2disobeywin = 0
t2disobeytotal = 0

t3obeywin = 0
t3obeytotal = 0
t3disobeywin = 0
t3disobeytotal = 0

t4obeywin = 0
t4obeytotal = 0
t4disobeywin = 0
t4disobeytotal = 0

t5obeywin = 0
t5obeytotal = 0
t5disobeywin = 0
t5disobeytotal = 0

t6obeywin = 0
t6obeytotal = 0
t6disobeywin = 0
t6disobeytotal = 0

t7obeywin = 0
t7obeytotal = 0
t7disobeywin = 0
t7disobeytotal = 0

t8obeywin = 0
t8obeytotal = 0
t8disobeywin = 0
t8disobeytotal = 0

t9obeywin = 0
t9obeytotal = 0
t9disobeywin = 0
t9disobeytotal = 0

t10obeywin = 0
t10obeytotal = 0
t10disobeywin = 0
t10disobeytotal = 0

for row in csv_f:

    #Convert winloss column to string
    winloss = ''.join(row[15])

    #Convert player cards to string
    playercard1 = ''.join(row[2])
    playercard2 = ''.join(row[3])
    playercard3 = ''.join(row[4])
    playercard4 = ''.join(row[5])
    playercard5 = ''.join(row[6])
    initialplayersum = int(playercard1) + int(playercard2)
    playerarray = [int(playercard1), int(playercard2), int(playercard3), int(playercard4), int(playercard5), initialplayersum]

    #Convert dealer cards to string
    dealercard1 = ''.join(row[8])
    dealercard2 = ''.join(row[9])
    dealercard3 = ''.join(row[10])
    dealercard4 = ''.join(row[11])
    dealercard5 = ''.join(row[12])
    initialdealersum = int(dealercard1) + int(dealercard2)
    dealerarray = [int(dealercard1), int(dealercard2), int(dealercard3), int(dealercard4), int(dealercard5)]

    #Ensure player only hit a single time for this data.
    counter = 0
    if playerarray[2] != 0:
        counter = counter + 1
    if playerarray[3] != 0:
        counter = counter + 1
    if playerarray[4] != 0:
        counter = counter + 1
    if counter != 1:
        continue

    #If dealersum is 2
    if initialdealersum == 2:

        #If 14<=playersum<=21
        if initialplayersum <=21 and initialplayersum >=14:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t1obeytotal = t1obeytotal + 1

                #If player won
                if winloss == "Win":
                    t1obeywin = t1obeywin + 1

            #If player hit
            else:
                t1disobeytotal = t1disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t1disobeywin = t1disobeywin + 1

        #If 12<=playersum<=13
        elif initialplayersum <=13 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t1obeytotal = t1obeytotal + 1

                #If player won
                if winloss == "Win":
                    t1obeywin = t1obeywin + 1

            #If player stayed
            elif playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t1disobeytotal = t1disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t1disobeywin = t1disobeywin + 1   

    #If dealersum is 3
    if initialdealersum == 3:

        #If 16<=playersum<=21
        if initialplayersum <=21 and initialplayersum >=14:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t2obeytotal = t2obeytotal + 1

                #If player won
                if winloss == "Win":
                    t2obeywin = t2obeywin + 1

            #If player hit
            else:
                t2disobeytotal = t2disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t2disobeywin = t2disobeywin + 1

        #If 12<=playersum<=13
        if initialplayersum <=13 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t2obeytotal = t2obeytotal + 1

                #If player won
                if winloss == "Win":
                    t2obeywin = t2obeywin + 1

                #If player stayed
                else:
                    t2disobeytotal = t2disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t2disobeywin = t2disobeywin + 1    

    #If dealersum is 4
    if initialdealersum == 4:

        #If 14<=playersum<=21
        if initialplayersum<=21 and initialplayersum>=14:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t3obeytotal = t3obeytotal + 1

                #If player won
                if winloss == "Win":
                    t3obeywin = t3obeywin + 1

            #If player hit
            else:
                t3disobeytotal = t3disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t3disobeywin = t3disobeywin + 1

        #If 12<=playersum<=13
        if initialplayersum <=13 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t3obeytotal = t3obeytotal + 1

                #If player won
                if winloss == "Win":
                    t3obeywin = t3obeywin + 1

                #If player hit
                else:
                    t3disobeytotal = t3disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t3disobeywin = t3disobeywin + 1   

    #If dealersum is 5
    if initialdealersum == 5:

        #If 14<=playersum<=21
        if initialplayersum<=21 and initialplayersum>=14:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t4obeytotal = t4obeytotal + 1

                #If player won
                if winloss == "Win":
                    t4obeywin = t4obeywin + 1

            #If player hit
            else:
                t4disobeytotal = t4disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t4disobeywin = t4disobeywin + 1

        #If 12<=playersum<=13
        if initialplayersum <=13 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t4obeytotal = t4obeytotal + 1

                #If player won
                if winloss == "Win":
                    t4obeywin = t4obeywin + 1

                #If player stayed
                else:
                    t4disobeytotal = t4disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t4disobeywin = t4disobeywin + 1   

    #If dealersum is 6
    if initialdealersum == 6:

        #If 14<=playersum<=21
        if initialplayersum<=21 and initialplayersum>=15:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t5obeytotal = t5obeytotal + 1

                #If player won
                if winloss == "Win":
                    t5obeywin = t5obeywin + 1

            #If player hit
            else:
                t5disobeytotal = t5disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t5disobeywin = t5disobeywin + 1

        #If 12<=playersum<=14
        if initialplayersum <=14 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t5obeytotal = t5obeytotal + 1

                #If player won
                if winloss == "Win":
                    t5obeywin = t5obeywin + 1

                #If player stayed
                else:
                    t5disobeytotal = t5disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t5disobeywin = t5disobeywin + 1   

    #If dealersum is 7
    if initialdealersum == 7:

        #If 14<=playersum<=21
        if initialplayersum<=21 and initialplayersum>=15:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t6obeytotal = t6obeytotal + 1

                #If player won
                if winloss == "Win":
                    t6obeywin = t6obeywin + 1

            #If player hit
            else:
                t6disobeytotal = t6disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t6disobeywin = t6disobeywin + 1

        #If 12<=playersum<=14
        if initialplayersum <=14 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t6obeytotal = t6obeytotal + 1

                #If player won
                if winloss == "Win":
                    t6obeywin = t6obeywin + 1

                #If player stayed
                else:
                    t6disobeytotal = t6disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t6disobeywin = t6disobeywin + 1   

    #If dealersum is 8
    if initialdealersum == 8:

        #If 16<=playersum<=21
        if initialplayersum<=21 and initialplayersum>=16:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t7obeytotal = t7obeytotal + 1

                #If player won
                if winloss == "Win":
                    t7obeywin = t7obeywin + 1

            #If player hit
            else:
                t7disobeytotal = t7disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t7disobeywin = t7disobeywin + 1

        #If 12<=playersum<=15
        if initialplayersum <=15 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t7obeytotal = t7obeytotal + 1

                #If player won
                if winloss == "Win":
                    t7obeywin = t7obeywin + 1

                #If player stayed
                else:
                    t7disobeytotal = t7disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t7disobeywin = t7disobeywin + 1   

    #If dealersum is 9
    if initialdealersum == 9:

        #If 16<=playersum<=21
        if initialplayersum<=21 and initialplayersum>=16:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t8obeytotal = t8obeytotal + 1

                #If player won
                if winloss == "Win":
                    t8obeywin = t8obeywin + 1

            #If player hit
            else:
                t8disobeytotal = t8disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t8disobeywin = t8disobeywin + 1

        #If 12<=playersum<=15
        if initialplayersum <=15 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t8obeytotal = t8obeytotal + 1

                #If player won
                if winloss == "Win":
                    t8obeywin = t8obeywin + 1

                #If player stayed
                else:
                    t8disobeytotal = t8disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t8disobeywin = t8disobeywin + 1   

    #If dealersum is 10
    if initialdealersum == 10:

        #If 17<=playersum<=21
        if initialplayersum<=21 and initialplayersum>=17:

            #If player stayed
            if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                t9obeytotal = t9obeytotal + 1

                #If player won
                if winloss == "Win":
                    t9obeywin = t9obeywin + 1

            #If player hit
            else:
                t9disobeytotal = t9disobeytotal + 1

                #If player won
                if winloss == "Win":
                    t9disobeywin = t9disobeywin + 1

        #If 12<=playersum<=16
        if initialplayersum <=17 and initialplayersum >=12:
            
            #If player hit
            if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                t9obeytotal = t9obeytotal + 1

                #If player won
                if winloss == "Win":
                    t9obeywin = t9obeywin + 1

                #If player stayed
                else:
                    t9disobeytotal = t9disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t9disobeywin = t9disobeywin + 1   

    #If dealersum is 11
        if initialdealersum == 10:

            #If 17<=playersum<=21
            if initialplayersum<=21 and initialplayersum>=17:

                #If player stayed
                if playercard3 == 0 and playercard4 == 0 and playercard5 == 0:
                    t10obeytotal = t10obeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t10obeywin = t10obeywin + 1

                #If player hit
                else:
                    t10disobeytotal = t10disobeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t10disobeywin = t10disobeywin + 1

            #If 12<=playersum<=16
            if initialplayersum <=17 and initialplayersum >=12:
                
                #If player hit
                if playercard3 != 0 or playercard4 != 0 or playercard5 != 0:
                    t10obeytotal = t10obeytotal + 1

                    #If player won
                    if winloss == "Win":
                        t10obeywin = t10obeywin + 1

                    #If player stayed
                    else:
                        t10disobeytotal = t10disobeytotal + 1

                        #If player won
                        if winloss == "Win":
                            t10disobeywin = t10disobeywin + 1 

#Declare Variables to calculate final win total
meanobeywin = 0
meandisobeywin = 0

#Print all results
print('\nFor when the dealer was showing 2')
if t1obeytotal != 0:
    print('obeytotal: ',t1obeytotal)
    print('obeywin: ',t1obeywin)
    print('obeywinrate: ', t1obeywin/t1obeytotal)
    meanobeywin = meanobeywin + (t1obeywin/t1obeytotal)
if t1disobeytotal !=0:
    print('disobeytotal: ',t1disobeytotal)
    print('disobeywin: ',t1disobeywin)
    print('disobeywinrate: ', t1disobeywin/t1disobeytotal)
    meandisobeywin = meandisobeywin + (t1disobeywin/t1disobeytotal)

print('\nFor when the dealer was showing 3')
if t2obeytotal != 0:
    print('obeytotal: ',t2obeytotal)
    print('obeywin: ',t2obeywin)
    print('obeywinrate: ', t2obeywin/t2obeytotal)
    meanobeywin = meanobeywin + (t2obeywin/t2obeytotal)
if t2disobeytotal !=0:
    print('disobeytotal: ',t2disobeytotal)
    print('disobeywin: ',t2disobeywin)
    print('disobeywinrate: ', t2disobeywin/t2disobeytotal)
    meandisobeywin = meandisobeywin + (t2disobeywin/t2disobeytotal)

print('\nFor when the dealer was showing 4')
if t3obeytotal != 0:
    print('obeytotal: ',t3obeytotal)
    print('obeywin: ',t3obeywin)
    print('obeywinrate: ', t3obeywin/t3obeytotal)
    meanobeywin = meanobeywin + (t3obeywin/t3obeytotal)
if t3disobeytotal !=0:
    print('disobeytotal: ',t3disobeytotal)
    print('disobeywin: ',t3disobeywin)
    print('disobeywinrate: ', t3disobeywin/t3disobeytotal)
    meandisobeywin = meandisobeywin + (t3disobeywin/t3disobeytotal)

print('\nFor when the dealer was showing 5')
if t4obeytotal != 0:
    print('obeytotal: ',t4obeytotal)
    print('obeywin: ',t4obeywin)
    print('obeywinrate: ', t4obeywin/t4obeytotal)
    meanobeywin = meanobeywin + (t4obeywin/t4obeytotal)
if t4disobeytotal !=0:
    print('disobeytotal: ',t4disobeytotal)
    print('disobeywin: ',t4disobeywin)
    print('disobeywinrate: ', t4disobeywin/t4disobeytotal)
    meandisobeywin = meandisobeywin + (t4disobeywin/t4disobeytotal)

print('\nFor when the dealer was showing 6')
if t5obeytotal != 0:
    print('obeytotal: ',t5obeytotal)
    print('obeywin: ',t5obeywin)
    print('obeywinrate: ', t5obeywin/t5obeytotal)
    meanobeywin = meanobeywin + (t5obeywin/t5obeytotal)
if t5disobeytotal !=0:
    print('disobeytotal: ',t5disobeytotal)
    print('disobeywin: ',t5disobeywin)
    print('disobeywinrate: ', t5disobeywin/t5disobeytotal)
    meandisobeywin = meandisobeywin + (t5disobeywin/t5disobeytotal)

print('\nFor when the dealer was showing 7')
if t6obeytotal != 0:
    print('obeytotal: ',t6obeytotal)
    print('obeywin: ',t6obeywin)
    print('obeywinrate: ', t6obeywin/t6obeytotal)
    meanobeywin = meanobeywin + (t6obeywin/t6obeytotal)
if t6disobeytotal !=0:
    print('disobeytotal: ',t6disobeytotal)
    print('disobeywin: ',t6disobeywin)
    print('disobeywinrate: ', t6disobeywin/t6disobeytotal)
    meandisobeywin = meandisobeywin + (t6disobeywin/t6disobeytotal)

print('\nFor when the dealer was showing 8')
if t7obeytotal != 0:
    print('obeytotal: ',t7obeytotal)
    print('obeywin: ',t7obeywin)
    print('obeywinrate: ', t7obeywin/t7obeytotal)
    meanobeywin = meanobeywin + (t7obeywin/t7obeytotal)
if t7disobeytotal !=0:
    print('disobeytotal: ',t7disobeytotal)
    print('disobeywin: ',t7disobeywin)
    print('disobeywinrate: ', t7disobeywin/t7disobeytotal)
    meandisobeywin = meandisobeywin + (t7disobeywin/t7disobeytotal)

print('\nFor when the dealer was showing 9')
if t8obeytotal != 0:
    print('obeytotal: ',t8obeytotal)
    print('obeywin: ',t8obeywin)
    print('obeywinrate: ', t8obeywin/t8obeytotal)
    meanobeywin = meanobeywin + (t8obeywin/t8obeytotal)
if t8disobeytotal !=0:
    print('disobeytotal: ',t8disobeytotal)
    print('disobeywin: ',t8disobeywin)
    print('disobeywinrate: ', t8disobeywin/t8disobeytotal)
    meandisobeywin = meandisobeywin + (t8disobeywin/t8disobeytotal)

print('\nFor when the dealer was showing 10')
if t9obeytotal != 0:
    print('obeytotal: ',t9obeytotal)
    print('obeywin: ',t9obeywin)
    print('obeywinrate: ', t9obeywin/t9obeytotal)
    meanobeywin = meanobeywin + (t9obeywin/t9obeytotal)
if t9disobeytotal !=0:
    print('disobeytotal: ',t9disobeytotal)
    print('disobeywin: ',t9disobeywin)
    print('disobeywinrate: ', t9disobeywin/t9disobeytotal)
    meandisobeywin = meandisobeywin + (t9disobeywin/t9disobeytotal)

print('\nFor when the dealer was showing 11')
if t10obeytotal != 0:
    print('obeytotal: ',t10obeytotal)
    print('obeywin: ',t10obeywin)
    print('obeywinrate: ', t10obeywin/t10obeytotal)
    meanobeywin = meanobeywin + (t10obeywin/t10obeytotal)
if t10disobeytotal !=0:
    print('disobeytotal: ',t10disobeytotal)
    print('disobeywin: ',t10disobeywin)
    print('disobeywinrate: ', t10disobeywin/t10disobeytotal)
    meandisobeywin = meandisobeywin + (t10disobeywin/t10disobeytotal)

#Calculating means
meanobeywin = meanobeywin/10
meandisobeywin = meandisobeywin/10

#Calculating Variances
obeyvar = (
    (math.pow(meanobeywin-(t1obeywin/t1obeytotal),2) + 
    math.pow(meanobeywin-(t2obeywin/t2obeytotal),2) + 
    math.pow(meanobeywin-(t3obeywin/t3obeytotal),2) + 
    math.pow(meanobeywin-(t4obeywin/t4obeytotal),2) + 
    math.pow(meanobeywin-(t5obeywin/t5obeytotal),2) + 
    math.pow(meanobeywin-(t6obeywin/t6obeytotal),2) + 
    math.pow(meanobeywin-(t7obeywin/t7obeytotal),2) + 
    math.pow(meanobeywin-(t8obeywin/t8obeytotal),2) + 
    math.pow(meanobeywin-(t9obeywin/t9obeytotal),2) + 
    math.pow(meanobeywin-(t10obeywin/t10obeytotal),2))
    /10
)
disobeyvar = (
    (math.pow(meandisobeywin-(t1disobeywin/t1disobeytotal),2) + 
    math.pow(meandisobeywin-(t2disobeywin/t2disobeytotal),2) + 
    math.pow(meandisobeywin-(t3disobeywin/t3disobeytotal),2) + 
    math.pow(meandisobeywin-(t4disobeywin/t4disobeytotal),2) + 
    math.pow(meandisobeywin-(t5disobeywin/t5disobeytotal),2) + 
    math.pow(meandisobeywin-(t6disobeywin/t6disobeytotal),2) + 
    math.pow(meandisobeywin-(t7disobeywin/t7disobeytotal),2) + 
    math.pow(meandisobeywin-(t8disobeywin/t8disobeytotal),2) + 
    math.pow(meandisobeywin-(t9disobeywin/t9disobeytotal),2) + 
    math.pow(meandisobeywin-(t10disobeywin/t10disobeytotal),2))
    /10
)

#Calculating Standard Deviations
obeystd = math.sqrt(obeyvar)
disobeystd = math.sqrt(disobeyvar)

print('\nFinal Results: ')
print('meanwinrate(if decision tables OBEYED): ', meanobeywin, " Variance: ", obeyvar," Standard Deviation: ", obeystd)
print('meanwinrate(if decision tables DISOBEYED): ', meandisobeywin, " Variance: ", disobeyvar," Standard Deviation: ", disobeystd)
