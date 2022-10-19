import json 
import pandas as pd



features_dict = {'population':'B01003_001E','males':'B01001_002E','females':'B01001_026E','never_married': 'B06008_002E','married': 'B06008_003E',
 'divorced': 'B06008_004E',
 'separated': 'B06008_005E',
 'widowed': 'B06008_006E',
 'grad_degree': 'B06009_006E',
 'per_capita_income': 'B19301_001E'}
 

data_path = "zip_code_dataframe.csv"

def get_zip_data():

    all_data = []
	
    for k,v in features_dict.items():
        URL = f"https://api.census.gov/data/2019/acs/acs5?get={v}&for=zip%20code%20tabulation%20area:*"
        r = requests.get(url = URL)
        data = r.json()
        all_data.append(pd.DataFrame(data[1:],columns=[k,'state','zip code tabulation area']).set_index("zip code tabulation area"))

    zip_code_df = pd.concat([all_data[i] for i in range(len(all_data))], axis=1)
	 
	
    return zip_code_df


def data_processing():

    
    zip_code_df = get_zip_data()
    
    zip_code_df.dropna(inplace=True)
	del zip_code_df['state']
	zip_code_df = zip_code_df.reset_index()
	
	zip_code_label = zip_code_df[["zip code tabulation area"]]
	zip_code_df.drop("zip code tabulation area",axis=1,inplace=True)
	zip_code_data = zip_code_df.apply(pd.to_numeric)
	
	return zip_code_data ,zip_code_label




	