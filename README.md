resolver
========
Simple python script which sends http get for each adress which resolved by nslookup and counts time

Test:

di@p:~$ python resolver.py www.python.org www.google.com

for www.python.org : 
{'82.94.164.162': [1.1645090579986572, 'dinsdale.python.org']}

for www.google.com : 
{'173.194.71.99': [0.7697839736938477, 'lb-in-f99.1e100.net'], '173.194.71.147': [0.31087398529052734, 'lb-in-f147.1e100.net'], '173.194.71.103': [0.30500292778015137, 'lb-in-f103.1e100.net'], '173.194.71.106': [0.30433106422424316, 'lb-in-f106.1e100.net'], '173.194.71.104': [0.28401684761047363, 'lb-in-f104.1e100.net'], '173.194.71.105': [0.2862532138824463, 'lb-in-f105.1e100.net']}

{ip: [time for http get, host name]}
