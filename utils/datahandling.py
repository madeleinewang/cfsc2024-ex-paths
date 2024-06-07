'''
datahandling

A module of utilities for handling data files used in the cfsc2024-ex-paths 
exercise of the 2024 Computational Fluency Short Course in Brown 
University's Carney Institute for Brain Science.
'''

import pandas as pd


def load_all_subjects(data_dir):
  '''
  This is a placeholder function. It should return a single DataFrame that
  concatenates all the subject data together.
  TODO: Add docstring
  TODO: Add functionality
  '''
  pass

def load_subject(file_path):
  '''
  Load data for a single subject.

  Is meant just to illustrate the idea of using a "helper" module with a
  notebook that does the main analysis. In this case, we avoid having
  our code crash if a file load fails, by wrapping it in a `try-except`
  block that "catches" the error, prints a message, but otherwise does
  nothing. In a real setting we would probably write better error handling.
  
  Parameters
  ----------
  file_path str
    A valid path to the data file

  Returns
  -------
  pandas.DataFrame
    A DataFrame as returned from read_csv. Returns None if load failed.
  '''

  try:
    return pd.read_csv(file_path)
  except:
    print(f'Unable to load data in \n  {file_path}')
    return None
