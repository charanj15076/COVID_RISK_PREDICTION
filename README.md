# Covid Classification

## What this repo contains?

This repository has the code to test a simple ML model deployed in GCP AI Platform
Directory Covid contains Streamlit webapp 
and rest of the files are the code for Data Analysis, Data Cleaning and Data prediction which are to be executed in GCP cluster.


## Package Requirements
* A Google Cloud account and a Google Cloud Project 
Python 3.6+
google_api_python_client==2.32.0
numpy==1.19.5
pandas==1.2.5
protobuf==3.19.1
pytest==6.2.5
requests==2.25.1
streamlit==0.76.0

### 1. Storing the model in a GCP Bucket
The saved `model.pkl` has to be stored in a Google Storage Bucket. First, create a bucket.

The rest of the inputs can be kept as default. 

And then upload the `model.pkl` to the bucket.

### 2. Hosting the model on AI Platform
Using the AI Platform, we need to create a model


Next, create a version of the model.


Choose the bucket location which has the `model.pkl` file.


The model will take some time to be hosted.


### 3. Creating a Service Account

Finally, head to `IAM -> Service Accounts` and add a Service Account which basically allows to use the model hosted on AI Platform externally.


Next, select `AI Platform Developer` as the role and click `Done`.


Now, in the `Service Accounts` console, we see that there are no keys. Yet.

We go to `Manage Keys`


Creating the key downloads a JSON file which basically has the key our code will be using.


The following configurations should be updated in the `app.py` file.


## Testing the hosted model

After making the appropriate changes to the configuration, running

```
streamlit run app.py
```

allows you to get the predictions from the GCP hosted model as well.

# COVID_RISK_PREDICTION
