'''This program calls and runs the public metamap web service to extract the concepts from the tweets.csv file.'''


from pymetamap import MetaMap # Python Wrapper
import pandas as pd

mm = MetaMap.get_instance('/home/archel2000/Downloads/public_mm/bin/metamap20') # Python Wrapper.

data = pd.read_csv('tweets.csv', sep=',') # Reads the tweets.csv file and seperates the text by commas.

sents = [data] # Sets sents as a tuple for data.

concepts, error = mm.extract_concepts(sents, [1, 2])  # Calls the webserver and returns and stores concepts.

for concept in concepts: # For loop prints concepts
    print(concept)

'''
Results:

/home/archel2000/.local/lib/python3.9/site-packages/pandas/compat/__init__.py:97: UserWarning: Could not import the lzma
 module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
  warnings.warn(msg)
Traceback (most recent call last):
  File "/home/archel2000/git/workspace/MMTesting/test_2.py", line 9, in <module>
    data = pd.read_csv('tweets.csv', sep=',') # Reads the tweets.csv file and seperates the text by commas.
  File "/home/archel2000/.local/lib/python3.9/site-packages/pandas/io/parsers.py", line 610, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/archel2000/.local/lib/python3.9/site-packages/pandas/io/parsers.py", line 468, in _read
    return parser.read(nrows)
  File "/home/archel2000/.local/lib/python3.9/site-packages/pandas/io/parsers.py", line 1057, in read
    index, columns, col_dict = self._engine.read(nrows)
  File "/home/archel2000/.local/lib/python3.9/site-packages/pandas/io/parsers.py", line 2061, in read
    data = self._reader.read(nrows)
  File "pandas/_libs/parsers.pyx", line 756, in pandas._libs.parsers.TextReader.read
  File "pandas/_libs/parsers.pyx", line 771, in pandas._libs.parsers.TextReader._read_low_memory
  File "pandas/_libs/parsers.pyx", line 827, in pandas._libs.parsers.TextReader._read_rows
  File "pandas/_libs/parsers.pyx", line 814, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 1951, in pandas._libs.parsers.raise_parser_error
pandas.errors.ParserError: Error tokenizing data. C error: Expected 9 fields in line 9, saw 11
'''