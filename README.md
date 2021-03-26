# Algothon_TeamTBA

This is the github repo for TeamTBA during the Algothon 

Contains of a barebones classifier that predicts whether the next step log-return is positive $r_{t + 1} > 0$ based on the 500 previous log-returns $r_{t} , \ldots, r_{t - 499}$

+ `train_latency_classifier.py` - trains a Logistic Regression model on provided data `data/LatencyTraining.csv`
+ `latency_logit.joblib` - output of `train_latency_classifier.py`
+ `latency_predict.py` - import the classifier and use it to run predictions from command line

**Usage**

Run `make run`. For each line (observation), 500 numbers delimited by commas is expected; A prediction of 0 or 1 is returned for each line