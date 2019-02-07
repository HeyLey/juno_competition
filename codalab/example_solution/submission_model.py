import numpy as np
import pandas as pd
import sys


class Model:
    def run(self, pmts_pos, spmt_hits, lpmt_hist, true_info, test_data):
        x = test_data["event"].unique()
        pred = pd.DataFrame({
            "evtID": x,
            "R": np.random.normal(size=len(x)),
            "E": np.random.normal(size=len(x))
        	})
        

        return pred
