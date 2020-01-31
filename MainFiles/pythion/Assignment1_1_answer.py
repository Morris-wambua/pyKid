for i in range(1,26):
    print('{0:5d}{1:5d}{2:6d}{3:6d}{4:6d}{5:6d}{6:6d}{7:6d}'.format(i,i*i,i+25,(i+25)*(i+25),i+50,(i+50)*(i+50),i+75,(i+75)*(i+75)))

# the characters in the curly brackets {} are placeholders for the data.
# the character before the colon indicates which of the data pieces should go where.
# the character after contains formatting information.
# in this case the number is the width of the filed and the d means decimal integer
# there are several other ways to achieve the same or similar result