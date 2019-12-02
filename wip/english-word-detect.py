



import enchant

d = enchant.Dict("en_US")

if d.check("test") == True:
    print ('ok!')
else:
    print ('NOOOOO!')
