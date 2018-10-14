import pandas as pd
import re
import csv
import os
from numpy.linalg import inv
import numpy as np

fbs_url="https://www.cbssports.com/college-football/scoreboard/FBS/"
b1g_url="https://www.cbssports.com/college-football/scoreboard/BIG10/"
top25_url="https://www.cbssports.com/college-football/scoreboard/top25/"

#for a specific week:
#"http://www.cbssports.com/college-football/scoreboard/FBS/" + str(year) + "/regular/" + str(week)

