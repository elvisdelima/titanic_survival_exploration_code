import csv
import pandas as pd

in_file = 'titanic_data.csv'
data = pd.read_csv(in_file)

def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """
    
    predictions = []
    for _, passenger in data.iterrows():
        predictions.append(
        	1 if is_a_female_with_up_to_2_siblings_and_spouses_not_from_lower_class(passenger) 
        	or is_a_female_not_from_lower_class(passenger)
        	or is_male_up_to_10_years_old(passenger) 
        	else 0)
        
    # Return our predictions
    return pd.Series(predictions)

def is_a_female_with_up_to_2_siblings_and_spouses_not_from_lower_class(passenger):
	return passenger['Sex'] == 'female' and passenger['SibSp'] <= 2 and passenger['Pclass'] != 3

def is_a_male_from_upper_class_and_paid_more_than_20_in_fees(passenger):
	return passenger['Sex'] == 'female' and passenger['Fare'] > 20

def is_male_up_to_10_years_old(passenger):	
	return passenger['Sex'] == 'male' and passenger['Age'] <= 10


# Make the predictions
predictions = predictions_1(data)
print predictions




