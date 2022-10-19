from sklearn.cluster import KMeans
import random
import pickle
from src.get_data import data_processing

model_path = "kmean_model.pkl"
zip_code_cluster_path = "zip_code_cluster.csv"

def cluster_model():
   
    zip_code_data ,zip_code_label = data_processing()
    
    kmeanModel =  KMeans(init="random",n_clusters=7,n_init=10,max_iter=300,random_state=42)
    kmeanModel.fit(zip_code_data)
    
	zip_code_label['cluster'] = kmeanModel.labels_
    pickle.dump(model, open(model_path, 'wb'))
	zip_code_label.to_csv (zip_code_cluster_path, index = None, header=True)
	
	return model_path ,zip_code_cluster_path


if __name__ == '__main__':

    model_path ,zip_code_cluster_path = cluster_model()