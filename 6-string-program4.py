# I have a string variable called s='maine 200 banana khaye'. This of course is 
# a wrong statement, the correct statement is 'maine 10 samosa khaye'. 
# Replace incorrect words in original string with new ones and print the new 
# string. Also try to do this in one line.

s = 'maine 200 banana khaye'
corrected_s = s.replace('200', '10').replace('banana', 'samosa')
print(corrected_s)