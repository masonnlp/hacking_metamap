"""
1. Look at https://metamap.nlm.nih.gov/MetaMapLiteReST.shtml
2. Register for an accoutn with NIH that allows you to invoke 
   their web service
3. Write the meta_map function as speced above to make the 
  call on https://metamap.nlm.nih.gov/MetaMapLiteReST.shtml
4. Present your results and explain the workings of your 
  code, the input and output
5. Write a main function that
  a. takes command line input that specifies 
    one or more input files
  b. saves the responses in output files
  c. To handle command line arguments use
     https://docs.python.org/2/library/argparse.html
6. Write unit tests for your code using pytest
7. Figure out where to put your temp files if any
8. Make sure you use pipenv
9. Make sure your code is pip8 compliant
  HINT use the black tool to autoformat
  https://github.com/psf/black
10. MAke sure to update .gitignore appropriately


"""

example_text = \
"""
Txt001|Written informed consent.
Txt002|Age 18 years or older.
Txt003|informed consent.
Txt004|Male or female.
"""

def meta_map(text):
    pass

meta_map(example_text)

