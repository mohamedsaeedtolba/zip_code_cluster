from flask import Flask, request, Response, jsonify
import pandas as pd
import json
import pickle

model_path = 'trained_model/kmean_model.pickle'
#zip_code_cluster_path = "zip_code_cluster.csv"

def predict_cluster(input_features):
    
    #zip_code_cluster = pd.read_csv(zip_code_cluster_path)
    kmean_model= pickle.load(open(model_path,'rb'))
    prediction_cluster = kmean_model.predict(input_features)
	
    return prediction_cluster
    	


app = Flask(__name__)

@app.route("/get_predicted_cluster", methods=["POST","GET"])
def cluster():
    try:
	
      #data = request.json
      data = request.json
      print(f"data:{data}")
      
      if len(data)>1 :
          input_features = pd.DataFrame.from_dict(data)
      else:
          input_features = pd.DataFrame.from_dict(data,index=[0])
      prediction_cluster= predict_cluster(input_features)
	  
      
      print(f"prediction_cluster:{type(prediction_cluster)}")
	  
      return {'zip_code_cluster': prediction_cluster.tolist()}

    except Exception as e:
        print(f"error:{e}")
        return {"Error":"internal server error"},500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)