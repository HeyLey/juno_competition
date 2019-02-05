import sys, os
import glob

import numpy as np
import pandas as pd


ingestion_program = sys.argv[1] # программа обучение
train_data = sys.argv[2] # трейн сет
output_dir = sys.argv[3] # сюда записать ответ
input_dir = sys.argv[4] # тут реф тест файл
#shared_directory = sys.argv[5] #xз
submission_program = sys.argv[5] # чужой код

input_train = os.path.join(train_data, "/*.csv")
input_test = os.path.join(input_dir, "test_lpmt_hits.csv")

test = pd.read_csv(input_test)

sys.path.append(submission_program)

import submission_model

model = submission_model.Model()

pred = model.run(input_train, test)

answer_path = os.path.join(output_dir, "pred.csv")
pred.to_csv(answer_path, index=False)
