# select name, age from user_info where age>22
#
# select * where job=IT
#['name', 'age']
# select * where phone like 133

query_clause = 'select name,age from table'
a = query_clause.split('from')[0][1:].split()
print(a)
filter_cols = [i.strip() for i in a]
print(filter_cols)
