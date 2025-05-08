thetext = "   The little titan launched a Python app to explore the universe. The Python code was powerful.   "

print("Original length:", len(thetext))

thetext = thetext.strip()

print("Trimmed length:", len(thetext))

count_the = thetext.lower().count("the")
print("Count of 'the':", count_the)

if 'little' in thetext:
    print("'little' was found")
else:
    print("'little' was not found")

if 'titan' in thetext:
    print("'titan' was found")
else:
    print("'titan' was not found")

pos_appl = thetext.find("appl")
print("Position of 'appl':", pos_appl)

thetext2 = thetext

thetext2 = thetext2.replace("Python", "PYTHON")

print("Modified thetext2:", thetext2)
