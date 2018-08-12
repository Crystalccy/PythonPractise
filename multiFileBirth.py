import pandas as pd

years = range(1880,2011)
pieces = []
columns = ['name','sex','births']

for year in years:
     path = "pydata-book-2nd-edition/datasets/babynames/yob%d.txt" %year
     frame = pd.read_csv(path, names = columns)
     
     frame['year'] = year
     pieces.append(frame)

names = pd.concat(pieces, ignore_index = True)

total_births = names.pivot_table('births',index='year',columns='sex',aggfunc=sum) 
 

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

sub_set = total_births[['John','Harry','Mary','Marilyn']]
sub_set.plot(subplots=True,figsize = (12,10),grid = False, title="Number of Birth Per Year")

table = top1000.pivot_table('prop',index = 'year',columns = 'sex', aggfunc = sum)
table.plot(title = 'sum of table1000.prop by year and sex', yticks = np.linspace(0,1.2,13),xticks=range(1880,2020,10))

df = boys[boys.year == 2010]
prop_cumsum = df.sort_index(by= 'prop', ascending = False).prop.cumsum()

prop_cumsum.searchsorted(0.5)

df = boys[boys.year == 1900]
in1900 = df.sort_index(by = 'prop', ascending = False).prop.cumsum()
in1900.searchsorted(0.5)+1

def get_quantitl_count(group,q=0.5):
    group = group.sort_index(by = 'prop',ascending = False)
    return group.prop.cumsum().searchsorted(0.5)[0]+1
    
diversity = top1000.groupby(['year','sex']).apply(get_quantitl_count)
diversity = diversity.unstack('sex')

diversity.dtypes

prop_cumsum.searchsorted(0.5)

prop_cumsum.searchsorted(0.5)[0]


type(prop_cumsum.searchsorted(0.5))

type(prop_cumsum.searchsorted(0.5)[0])