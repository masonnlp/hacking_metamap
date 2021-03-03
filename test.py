'''This program calls and runs the public metamap web service to extract the concepts from the tweets.csv file.'''

from pymetamap import MetaMap # Python Wrapper

mm = MetaMap.get_instance('/home/archel2000/Downloads/public_mm/bin/metamap20') # Python Wrapper

with open('tweets.csv') as file: # Opens tweets.csv and sets it as a variable.
    data = file.readline() # Reads individual lines of the csv file.
    sents = [data]
    concepts, error = mm.extract_concepts(sents, [1, 2]) # Sends the data to the webserver and returns and stores concepts
    for concept in concepts: # For loops prints the concepts.
        print(concept)

'''
Results: 

### MetaMap ERROR: The sldiID option requires input lines of the form ID|Text
ConceptMMI(index='1', mm='MMI', score='7.40', preferred_name='Count', cui='C0750480', semtypes='[qnco]', trigger='["Count"-tx-1-"count"-noun-0]', location='TX', pos_info='[48/5],[63/5]', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='7.40', preferred_name='Count Dosing Unit', cui='C1705566', semtypes='[qnco]', trigger='["COUNT"-tx-1-"count"-noun-0]', location='TX', pos_info='[48/5],[63/5]', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Author', cui='C3812881', semtypes='[prog]', trigger='["Author"-tx-1-"author"-noun-0]', location='TX', pos_info='17/6', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Communicable Diseases', cui='C0009450', semtypes='[dsyn]', trigger='["ID"-tx-1-"id"-noun-0]', location='TX', pos_info='2/2', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='GDC Index Date Terminology', cui='C5202800', semtypes='[inpr]', trigger='["ID"-tx-1-"id"-noun-0]', location='TX', pos_info='2/2', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Identifier', cui='C0600091', semtypes='[inpr]', trigger='["ID"-tx-1-"id"-noun-0]', location='TX', pos_info='2/2', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Immune diffusion', cui='C1441613', semtypes='[lbpr]', trigger='["ID"-tx-1-"id"-noun-0]', location='TX', pos_info='2/2', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Source', cui='C0449416', semtypes='[fndg]', trigger='["Source"-tx-1-"source"-noun-0]', location='TX', pos_info='10/6', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Source (property) (qualifier value)', cui='C4521696', semtypes='[ftcn]', trigger='["Source"-tx-1-"source"-noun-0]', location='TX', pos_info='10/6', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Term Source', cui='C1705919', semtypes='[inpr]', trigger='["Source"-tx-1-"source"-noun-0]', location='TX', pos_info='10/6', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Text', cui='C1527021', semtypes='[inpr]', trigger='["Text"-tx-1-"text"-noun-0]', location='TX', pos_info='5/4', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Text (foundation metadata concept)', cui='C3541382', semtypes='[inpr]', trigger='["Text"-tx-1-"text"-noun-0]', location='TX', pos_info='5/4', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Text - MDFAttributeType', cui='C1554111', semtypes='[inpr]', trigger='["Text"-tx-1-"text"-noun-0]', location='TX', pos_info='5/4', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Text Line', cui='C1705606', semtypes='[inpr]', trigger='["Text"-tx-1-"text"-noun-0]', location='TX', pos_info='5/4', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='5.18', preferred_name='Text Messages', cui='C3178910', semtypes='[inpr]', trigger='["Text"-tx-1-"text"-noun-0]', location='TX', pos_info='5/4', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='3.68', preferred_name='Status', cui='C0449438', semtypes='[qlco]', trigger='["Status"-tx-1-"status"-noun-0]', location='TX', pos_info='33/6', tree_codes='')
ConceptMMI(index='1', mm='MMI', score='3.50', preferred_name='Quotation', cui='C2981735', semtypes='[mnob]', trigger='["Quote"-tx-1-"quote"-noun-0]', location='TX', pos_info='27/5', tree_codes='')
'''