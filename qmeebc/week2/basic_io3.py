my_dictionary = {"a key": 10, "another key": 11}

import pickle

f = open('testp.p','wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

f = open('testp.p','rb')
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)