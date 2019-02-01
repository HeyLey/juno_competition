import sys, os

import numpy as np
import pandas as pd



input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
reference_dir = os.path.join(input_dir, 'ref')

reference_file = os.path.join(reference_dir, 'true_info_ph1.csv')
prediction_file = os.path.join(submit_dir, 'preds.csv')

if not os.path.isdir(submit_dir):
    print("{} doesn't exist".format(submit_dir))
elif not os.path.isdir(reference_dir):
    print("{} doesn't exist".format(reference_dir))
else:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reference  = pd.read_csv(reference_file)
    prediction = pd.read_csv(prediction_file)

    reference  = reference.sort_values('evtID')
    prediction = prediction.sort_values('evtID')

    #if not np.array_equal(reference['evtID'], prediction['evtID']):
     #   continue
     
    E_diff  = np.mean((reference['E'] - prediction['E']) ** 2)
    R_diff = np.mean((reference['R'] - prediction['R']) ** 2)
    score = R_diff * 0.001 + E_diff * 10
   
    output_filename = os.path.join(output_dir, 'scores.txt')

    with open(output_filename, 'w') as output_file:
        output_file.write("MSE: {}".format(score))
        output_file.write("\n")
        output_file.write("MSE E: {}".format(E_diff))
        output_file.write("\n")
        output_file.write("MSE R: {}".format(R_diff))


