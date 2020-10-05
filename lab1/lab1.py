import pandas as pd
import numpy as np
import matplotlib.pyplot



def main():
    df = pd.read_csv("data/heart_failure_clinical_records_dataset.csv")
    df = df.drop(columns=['anaemia','diabetes','high_blood_pressure','sex','smoking','time','DEATH_EVENT'])

    print(df)





if __name__ == '__main__':
    main()
