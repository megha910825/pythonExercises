### TCS Appraisel Hike Calculator
## If your rating is above 4.5 you get 10% hike, 
## if your rating is between 3 and 4.5 you will get 7% hike
## if your rating is between 2 and 3 you will get 3% hike
## if your rating is below 2 you will get no hike
## Consider scenario 1: CTC 1000000 rating 4.7
## Scenario 2: CTC 1000000 rating 2.5

ctc = 1000000
rating = 2.5
hike = 0
if (rating > 4.5 ):
    hike = 10
elif ( rating > 3 and rating < 4.5):
    hike = 7
elif ( rating >= 2 and rating <= 3):
    hike =  3
else:
    hike = 0 

totalHike = ctc + ctc* hike/100
print(totalHike)