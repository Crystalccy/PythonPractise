import pandas as pd

years = range(1880,2010)
pieces = []
columns = ['name','sex','births']

for year in years:
     path = "pydata-book-2nd-edition/datasets/babynames/yob%d.txt" % year
     frame = pd.read_csv(path, names = columns)
     
     frame['year'] = year
     pieces.append(frame)

#names = pd.concat(pieces, ignore_index = True)

#total_births = names.pivot_table('births',index='year',columns='sex',aggfunc=sum) 
 

def add_prop(group):
    births = group.births.astype(float)
    
    group['prop'] = births / births.sum()
    return group
    
names = names.groupby(['year','sex']).apply(add_prop)

#judge = np.allclose(names.groupby(['year','sex']).prop.sum(),1)

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]
    
grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)

#print (top1000)

boys = top1000[top1000.sex =='M']
girls = top1000[top1000.sex =='F'] 
total_births = top1000.pivot_table('births',index='year',columns='name',aggfunc=sum) 

sub_set = total_births[['John','Hurry','Mary','Marilyn']]
sub_set.plot(subplots=True,figsize = (12,10),grid = False, title="Number of Birth Per Year")