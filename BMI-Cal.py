

def bmi_caculator(gender, height_m, weight_kg):
    bmi = round(weight_kg / (height_m ** 2), 2)

    if bmi <= 18.4:
        print(gender,' BMI is', bmi, 'which means you are Underweight.Health Risk-Malnutrition risk')
        return bmi

    elif bmi > 18.5 and bmi < 24.9:
        print(gender,' BMI is', bmi, 'which means you are Normal Weight.Health Risk-Low risk')
        return bmi

    elif bmi > 25 and bmi < 29.9:
        print(gender, ' BMI is', bmi, 'which means you are OverWeight.Health Risk-Enhanced risk')
        return bmi

    elif bmi > 30 and bmi < 34.9:
        print(gender, ' BMI is', bmi, 'which means you are Moderately obese.Health Risk-Medium risk')
        return bmi

    elif bmi > 35 and bmi < 39.9:
        print(gender, ' BMI is', bmi, 'which means you are Severely obese.Health High risk')
        return bmi

    elif bmi > 40:
        print(gender, ' BMI is', bmi, 'which means you are Very severely obese.Health Very high risk')
        return bmi



import json

with open('C:\\Users\\GAnya\\PycharmProjects\\BMI_Calculator\\jsondata.json') as f:
   json_data=json.load(f)
   count = 0
   for i in json_data:
       print(i)
       Gender=i['Gender']
       Height=(i['HeightCm'])/100
       Weight=i['WeightKg']
       Bmi = round(Weight / (Height ** 2), 2)

       if Bmi>29.9:
           count+=1
       bmi_caculator(Gender,Height,Weight)

   print('Total OverWeight People :', count)

