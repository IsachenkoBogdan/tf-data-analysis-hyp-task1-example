import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 683820405 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.03

    table = [[x_success, x_cnt - x_success],
             [y_success, y_cnt - y_success]]
    return sps.fisher_exact(table, alternative='greater')[1] < alpha
