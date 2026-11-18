import string 
j='greeeksforgreeks_is_best'
res=string.capwords(j.replace('_','')).replace('','')
print(res)
