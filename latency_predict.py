"""

"""
import sys
from joblib import load
import numpy as np

if __name__ == '__main__':
	# Read Data
	logit = load("latency_logit.joblib")
	for line in sys.stdin:
		X_in = np.array([float(i) for i in line.split(",")])
		print(int(logit.predict(X_in.reshape(1,-1)) * 1))