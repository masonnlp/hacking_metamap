# hacking_metamap
This is a "hacking project" -- what that means is that the code is dirty (at least to start with) with the object to explore something.

The something in this case is to explore the use of meta_map tool by NIH: https://metamap.nlm.nih.gov/.

Metamap is a sophisticated tool that takes some body of text and annotates the text using UMLS Metathesaurus terms.

We can use Metamap in two modes:

1. By downloading and installing to code and running it locally. This requires a bit of work -- it uses Java so we have to support the Java eco-system
2. The second is to use the web-service NIH provides

We are going to opt for option-2. Where our Python code invokes a remote web-service running on NIH's servers and returns the result.

So for this project write a function:

```
def meta_map(text):
    # here write your code
    # the code should submit text to the Metamap service
    # capture the return
    # you should return the output as a python dicrionary
 ```

It seems NIH has a lightweight python client to invoke their webservice here https://metamap.nlm.nih.gov/MetaMapLiteReST.shtml 

So the outline of the task is:

1. Look at https://metamap.nlm.nih.gov/MetaMapLiteReST.shtml
2. Register for an accoutn with NIH that allows you to invoke their web service
3. Write the meta_map function as speced above to make the call on https://metamap.nlm.nih.gov/MetaMapLiteReST.shtml
4. Present your results and explain the workings of your code, the input and output
