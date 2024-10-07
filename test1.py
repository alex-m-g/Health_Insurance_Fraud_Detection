import os
import pandas as pd

def data_wrangle(folder):
    files = []
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        files.append(file_path)

    df_test = pd.read_csv(files[0])
    df_test_beneficiary_data = pd.read_csv(files[1])
    df_train_inpatient_data = pd.read_csv(files[2])
    df_train_outpatient_data = pd.read_csv(files[3])
    df_train = pd.read_csv(files[4])
    df_train_beneficiary_data = pd.read_csv(files[5])
    df_train_inpatient_data = pd.read_csv(files[6])
    df_train_outpatient_data = pd.read_csv(files[7])

    print("Successful variable assignment")

    
    # replace 2 to 0 for the chronic conditions to indicate False.
    df_train_beneficiary_data = df_train_beneficiary_data.replace({'ChronicCond_Alzheimer': 2, 'ChronicCond_Heartfailure': 2, 'ChronicCond_KidneyDisease': 2,
                               'ChronicCond_Cancer': 2, 'ChronicCond_ObstrPulmonary': 2, 'ChronicCond_Depression': 2, 
                               'ChronicCond_Diabetes': 2, 'ChronicCond_IschemicHeart': 2, 'ChronicCond_Osteoporasis': 2, 
                               'ChronicCond_rheumatoidarthritis': 2, 'ChronicCond_stroke': 2 }, 0)
    
    print("Successful df_train_benificiary_data reassignment Part 1")

    # For RenalDiseaseIndicator replacing 'Y' with 1
    df_train_beneficiary_data = df_train_beneficiary_data.replace({'RenalDiseaseIndicator': 'Y'}, 1)
    
    print("Successful df_train_benificiary_data reassignment Part 2")

    # convert all these columns datatypes to numeric
    # Select all columns that start with 'ChronicCond_' or 'RenalDiseaseIndicator' and apply conversion
    df_train_beneficiary_data[df_train_beneficiary_data.filter(like='ChronicCond_').columns.tolist() + ['RenalDiseaseIndicator']] = df_train_beneficiary_data[df_train_beneficiary_data.filter(like='ChronicCond_').columns.tolist() + ['RenalDiseaseIndicator']].apply(pd.to_numeric)
    print("Successful conversion of df_train_benificiary_data to numeric")

def main():
    folder = "archive"
    data_wrangle(folder)

if __name__ == "__main__":
    main()
