#  CAPSTONE PROJECT
   
## Project overview
This is the Capstone project required for fulfillment of the Nanodegree Machine Learning Engineer with Microsoft Azure from Udacity. In this project, we use a dataset external to Azure ML ecosystem.

This project will demonstrate my ability to use an external dataset in Azure workspace, train a model using the different tools available in the AzureML framework as well as my ability to deploy the model as a web service. In this project, we need to create a machine learning model : one using Automated ML and other customized model whose hyperparameters are tuned using HyperDrive. Than we need to compare the performance of both the models and deploy the best between two. 

### Project Set Up
Steps needs to be followed during this project - 

•	**Step 1 :** Set up your workspace: Create a new workspace, if you haven’t already.

•	**Step 2 :** Set up your Azure Development Environment: Create a compute instance VM to run jupyter notebooks.

•	**Step 3 :** Download starter files: These files have some boilerplate code and TODOs that will help you start working on your project. You can find them in this link: https://github.com/udacity/nd00333-capstone/tree/master/starter_file

•	**Step 4 :** Choose a dataset:  Working with Kaggle heart failure dataset, it can be found in the link: https://www.kaggle.com/andrewmvd/heart-failure-clinical-data/download

•	**Step 5 :** Train a model using Automated ML: The automl.ipynb file contains a starter code to help you train a model using Automated ML. 

•	**Step 6 :** Train a model with HyperDrive: The hyperparameter_tuning.ipynb file contains some starter codes to help you train a model and perform hyperparameter tuning using HyperDrive.

•	**Step 7 :** Model Deployment: After you have trained your models. You will have to deploy your best model as a webservice and test the model endpoint.

## Dataset

### Overview

This is an analyzed dataset containing the medical records of 299 heart failure patients collected at the Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015. The patients consisted of 105 women and 194 men, and their ages range between 40 and 95 years old.

Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worlwide. Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure. Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies. People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

This heart failure dataset was gotten from kaggle's repository.

### Task

With the kaggle heart failure dataset I'll be using the knowledge I have obtained from the Machine Learning Engineer with Microsoft Azure Nanodegree Program to create a machine learning model that can assess the likelihood of a death by heart failure event. This can be used to help hospitals in assessing the severity of patients with cardiovascular disease. In this project, I will create two models: one using Automated ML and one customized model whose hyperparameters are tuned using HyperDrive.

#### Features of the dataset

The dataset contains 13 features, which report clinical, body, and lifestyle information (Table 1), that we briefly describe here. Some features are binary: anaemia, high blood pressure, diabetes, sex, and smoking. The hospital physician considered a patient having anaemia if haematocrit levels were lower than 36%.

Regarding the features, the creatinine phosphokinase (CPK) states the level of the CPK enzyme in blood. When a muscle tissue gets damaged, CPK flows into the blood. Therefore, high levels of CPK in the blood of a patient might indicate a heart failure or injury. The ejection fraction states the percentage of how much blood the left ventricle pumps out with each contraction. The serum creatinine is a waste product generated by creatine, when a muscle breaks down. Especially, doctors focus on serum creatinine in blood to check kidney function. If a patient has high levels of serum creatinine, it may indicate renal dysfunction. Sodium is a mineral that serves for the correct functioning of muscles and nerves. The serum sodium test is a routine blood exam that indicates if a patient has normal levels of sodium in the blood. An abnormally low level of sodium in the blood might be caused by heart failure. The death event feature, that we use as the target in our binary classification study, states if the patient died or survived before the end of the follow-up period, that was 130 days on average. The original dataset article unfortunately does not indicate if any patient had primary kidney disease, and provides no additional information about what type of follow-up was carried out. Regarding the dataset imbalance, the survived patients (death event = 0) are 203, while the dead patients (death event = 1) are 96. In statistical terms, there are 32.11% positives and 67.89% negatives.

### Access

During this project course, i downloaded the dataset from Kaggle as csv file. Than i uploaded it on my github profile and accessed it using Tabular dataset as given below :
```
from azureml.core.dataset import Dataset
path = "https://raw.githubusercontent.com/Arushikha0408/nd00333-capstone/master/heart_failure_clinical_records_dataset.csv"
dataset = Dataset.Tabular.from_delimited_files(path)
```

## Automated ML

The following code shows a basic example of creating an AutoMLConfig object and submitting an experiment for classification. I chose the automl settings below because I wanted to specify the experiment type as classification. The classification experiment will be carried out using AUC weighted as the primary metric, I find this metric useful for predicting binary classification models. The experiment timeout minutes is set to 30 minutes to control the use of resources and 5 cross-validation folds with the maximum number of iterations that would be executed simultaneously set to 4 to maximize usage. All of these settings defines the machine learning task.

The configuration object below contains and persists the parameters for configuring the experiment run, as well as the training data to be used at run time.
```
automl_settings = {
    "experiment_timeout_minutes": 30,
    "max_concurrent_iterations": 5,
    "primary_metric" : 'AUC_weighted',
    "n_cross_validations": 5
}
automl_config = AutoMLConfig(compute_target=cpu_cluster,
                             task = "classification",
                             training_data=dataset,
                             label_column_name="DEATH_EVENT", 
                             enable_early_stopping= True,
                             featurization= 'auto',
                             enable_voting_ensemble= True,
                             **automl_settings
                            )
```
**AutoML experiment RunDetails** - The following image shows run details of AutoML experiment
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/run1.PNG)

**AutoML Run with Metric: AUC_Weighted** - This shows for different AutoML run. On average it is - 0.9191440337763013.
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/auc_weighted.PNG)

**Various Models of AutoML Run** - This image shows various algorithm along with their AUC_Weighted value.  
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/model.PNG)

### Results

This automl experiment generated an AUC_weighted score of 0.9191440337763013 for the AutoML model.

The parameters that VotingEnsemble used are:

'RandomForest', 'XGBoostClassifier', 'GradientBoosting', 'RandomForest', 'RandomForest', 'RandomForest'

It also had weights of: 

'ensemble_weights': 0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666
 
To improve the automl model, I can try applying other metrics, for example, the average precision score metrics that gives the weighted mean of precision with weights equal to class probability. It is a useful metric to compare how well models are ordering the predictions, without considering any specific decision threshold.

**VotingEnsemble Run Details** - This image shows details like status, accuracy, AUC Macro, AUC Micro, Duration etc. of VotingEnsemble algorithm.
![alt_test](https://github.com/Arushikha0408/nd00333-capstone/blob/master/voting1.PNG)

**VotingEnsemble Metric Details** - This image shows details like accuracy, AUC Macro, AUC Micro and AUC_Weighted values of VotingEnsemble algorithm
![alt_test](https://github.com/Arushikha0408/nd00333-capstone/blob/master/voting2.PNG)

**Jupyter notebook snippet for code for best run** - This shows code and output related to best run for AutoML experiment.
![alt_test](https://github.com/Arushikha0408/nd00333-capstone/blob/master/best_run.PNG)

## Hyperparameter Tuning

I chose a custom-coded model — a standard Scikit-learn Logistic Regression for this experiment. Logistic Regression is a classification algorithm that is used to predict the probability of a categorical dependent variable. In the case of this capstone experiment, I chose the model because the decision boundary of logistic regression model is a linear binary classifier that seperate the two classes I want to predict using a hyperdrive service.

The parameters I used for the hyperparameter search are:

Regularization Strength (C) with range 0.1 to 1.0 -- Inverse of regularization strength. Smaller values cause stronger regularization

Max Iterations (max_iter) with values 25, 50, 100, 150 and 200 -- Maximum number of iterations to converge.

**Jupyter notebook snippet for Hyperparameter Tuning - hyperdrive_config code** - This shows code configurations for hyperparameter tuning.
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/hyper_para.PNG)

**Jupyter notebook snippet for Hyperparamter Tuning - RunDeatils part (a)** - This shows the output obtained for RunDetails of hyperparameter drive.
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/hyper_rundetails1.PNG)

**Jupyter notebook snippet for Hyperparamter Tuning - RunDeatils part (b)** - 
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/hyper_rundetails2.PNG)

### Results

The best hyperparameters for the hyperdrive model is:

• 'Regularization Strength: ': 0.05232056042459456
• 'Max iterations: ': 25
• This hyperparameters generated an accuracy of  0.7666666666666667 for the hyperdrive model.

The model could have improved further using Bayesian optimization algorithm but that allows for the use of a different kind of statistical techniques for improvement of hyperparamter. It picks samples based on how previous samples performed, so that new samples improve the primary metric and its search is potentially efficient.

**Jupyter notebook snippet for Hyperparamter Tuning - Best Run code snippet** - This image shows code for best run and its output.
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/hyper_bestrun.PNG)

**Hyperparamter Tuning - hyper_drive model run detals under Experiments Part (A)** - This image shows run details of hyper driver under Experiments 
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/hyper_bestmodel.PNG)

**Hyperparamter Tuning - hyper_drive model run detals under Experiments Part (B)** -
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/hyper_bestmodel1.PNG)


## Model Deployment

After training a model using Automated ML, the next thing is to deploy the best model as a webservice and test the model endpoint.

To deploy the automl model, first thing is to register the model and then create an environment. We have a 'score.py' script that is provided for the inference configuration. In the inference configuration, I enabled application insights, that is, logging. So now I can deploy the automl model using Azure Container Instance as a WebService with parameters: workspace, aci service name, model, inference config and deployment configuration.

**Jupyter notebook snippet of AutoML** - This image shows code snippet for deploying a model in AutoML.
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/deploy.PNG)

**Deploying best model for AutoML - Running status** - This shows Running status of deployed AutoML model
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/deploy1.PNG)

**Deploying best model for AutoML - Completed status** - This shows Completed status of deployed AutoML model
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/deploy2.PNG)
 
After deployment was successful, a rest endpoint was generated, to query the endpoint with a sample input, I created an endpoint.py file that contained two sets of data for scoring, I copied the rest endpoint and added it to the 'endpoint.py' file as a scoring uri.

scoring URI - http://1f47e230-341d-459b-9740-11b253d5d018.southcentralus.azurecontainer.io/score

Sample input/payload:
```
{
  "data": [
    {
      "age": 36,
      "anaemia": 0,
      "creatinine_phosphokinase": 200,
      "diabetes": 0,
      "ejection_fraction": 30,
      "high_blood_pressure": 0,
      "platelets": 120000,
      "serum_creatinine": 1.1,
      "serum_sodium": 135,
      "sex": 1,
      "smoking": 0,
      "time": 7
    },
    {
      "age": 39,
      "anaemia": 0,
      "creatinine_phosphokinase": 300,
      "diabetes": 0,
      "ejection_fraction": 50,
      "high_blood_pressure": 0,
      "platelets": 200000,
      "serum_creatinine": 0.9,
      "serum_sodium": 250,
      "sex": 0,
      "smoking": 0,
      "time": 1
    }
  ]
}
``` 

**Jupyter Notebook snippet - Queying Endpoint.py generated after Deployment** - This image shows querying endpoint.py and creating json for service.
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/deploy3.PNG)

**Jupyter Notebook snippet - Serive State** - This image shows service state as Healthy for model. 
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/service_state.PNG)

**Logs for Service** - This image shows logs for running service.
![alt_text](https://github.com/Arushikha0408/nd00333-capstone/blob/master/deploy4.PNG)

## Future Improvement
There are many ways to improve AutoML and HyperDrive runs in this project.
To improve the AutoML, we could choose the best 3 to 5 algorithms that performed well in this classification task and create another AutoML run forbidding any other algorithm type. We could also take a look at the data that has been wrongly classified by the best model and try to identify a pattern that points to transformations that we can perform in the dataset. That can be done by creating a pipeline with a first step to transform the data and a second one to execute the AutoML.
Moving on to the HyperDrive algorithm, we could have used regularization strength as a reference (it was randomly picked) and created a second HyperDrive run using a different sampling method using values closer to it. Another strategy would be to test different classifier algorithms in our training script and change their hyperparameters too. We could do that to a finite set of algorithms and hyperparameters and select the best one among all runs. Many other classification algorithms could be tested, like Decision Tree, Random Forest, Support Vector Classification, and so on. Each of these algorithms has different hyperparameters that can be choose using either Random Sampling or other sampling methods. Deep Learning algorithms could also be applied to solve this problem.

Going even further, models performance was measured using the metric `Accuracy` for simplicity, and this could be changed to a more robust metric like `AUC_weighted` for example.

## Screen Recording

 The link to screen recording is - https://drive.google.com/file/d/1WGNc-ev3_HVQbSfH-d0KBDCRvmkQg8vz/view?usp=sharing
 
