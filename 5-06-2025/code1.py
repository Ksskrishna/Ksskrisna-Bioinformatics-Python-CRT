#using extend
prog_lang = ["C","C++","python","java"]
print(prog_lang)
front_end = ["HTML","HTML","CSS","JS","React","React.js","angular.js"]
prog_lang.extend(front_end)
print(prog_lang)
databases = ["SQL","NoSQL","Monogodb","Django"]
prog_lang.extend(databases)
print(prog_lang)
print(prog_lang.count('HTML'))