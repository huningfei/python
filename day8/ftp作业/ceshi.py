import configparser
config = configparser.ConfigParser()
config.read('userinfo')
#print(config['hnf']['passwd'])
user = config.sections()
print(user)
for i in user:
    print(i)
    print(config[i]['passwd'])