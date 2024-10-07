import os
import pandas as pd

def data_wrangle(folder):
    files = []
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        files.append(file_path)

    df_test = pd.read_csv(files[0])
    df_test_beneficiary_data = pd.read_csv(files[1])
    df_test_inpatient_data = pd.read_csv(files[2])
    df_test_outpatient_data = pd.read_csv(files[3])
    df_train = pd.read_csv(files[4])
    df_train_beneficiary_data = pd.read_csv(files[5])
    df_train_inpatient_data = pd.read_csv(files[6])
    df_train_outpatient_data = pd.read_csv(files[7])

    print("Successful variable assignment")

    print(f"df_test:\n{df_test.columns}")
    print(f"df_test_beneficiary_data:\n{df_test_beneficiary_data.columns}")
    print(f"df_test_inpatient_data:\n{df_test_inpatient_data.columns}")
    print(f"df_test_outpatient_data:\n{df_test_outpatient_data.columns}")
    print(f"df_train:\n{df_train.columns}")
    print(f"df_train_beneficiary_data:\n{df_train_beneficiary_data.columns}")
    print(f"df_train_inpatient_data:\n{df_train_inpatient_data.columns}")
    print(f"df_train_outpatient_data:\n{df_train_outpatient_data.columns}")

def main():
    folder = "archive"
    data_wrangle(folder)

if __name__ == "__main__":
    main()
