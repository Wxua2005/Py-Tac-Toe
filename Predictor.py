import pandas as pd
from joblib import dump , load
import numpy as np
import warnings

warnings.filterwarnings("ignore",category=DeprecationWarning)

thumbs_up = 0
palm = 0
thumbs_down = 0

model = load('model2.joblib')

k = np.loadtxt('test.csv',delimiter=',')

k = pd.DataFrame(data=k,columns=model.feature_names_in_)

l = model.predict(k)
for i in l:
    if i == 0:
        palm += 1
    elif i == 1:
        thumbs_up += 1
    elif i == 3:
        thumbs_down += 1

print(f'Thumbs Up : {thumbs_up}\n Thumbs Down : {thumbs_down}\n Palm : {palm}')
