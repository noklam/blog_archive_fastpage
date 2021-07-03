from kedro.pipeline import Pipeline, node

import pandas as pd

def A(df):
    print('Loading the Iris Dataset')
    return 'Step1'

def B(dummy):
    return 'Step2'

def C(dummy):
    return 'Step3'
    
def create_pipeline():
    return Pipeline(node(A, "example_iris_data", "A"),
                    node(B,"A","B"),
                    node(C,"C","C"))