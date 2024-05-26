import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 683820405 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.03
    return proportions_ztest(np.array([x_success, y_success]), np.array([x_cnt, y_cnt]), alternative='greater')[1] < alpha
