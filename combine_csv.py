import pandas as pd

def combine(add_list,output_name):
    combined_df = pd.DataFrame()
    for address in add_list: 
        input_csv = pd.read_csv(address)
        combined_df = pd.concat([combined_df, input_csv]).drop_duplicates().reset_index(drop=True)
    combined_df.to_csv(f'{output_name}.csv', index=False)

combine(['abcr_amine_1.csv','abcr_amine_2.csv','Doug_amine_1.csv','Doug_amine_2.csv','Merck_amine_1.csv','Merck_amine_2.csv','tci_amine_1.csv','tci_amine_2.csv'],'amide')