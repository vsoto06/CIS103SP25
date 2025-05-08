def main():
    thetext = """
        Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.
        """
    print(thetext)

    # ---------------------------------
    #     put assignment statements here
  
    print(thetext)

    
    original_length = len(thetext)
    print("Original length:", original_length)

    
    trimmed_text = thetext.strip()

    
    trimmed_length = len(trimmed_text)
    print("Trimmed length:", trimmed_length)

    
    count_the = trimmed_text.lower().count("the")
    print("Count of 'the':", count_the)

    
    if 'little' in trimmed_text.lower():
        print("'little' was found")
    else:
        print("'little' was not found")

   
    if 'titan' in trimmed_text.lower():
        print("'titan' was found")
    else:
        print("'titan' was not found")

   
    pos_appl = trimmed_text.find("appl")
    print("Position of 'appl':", pos_appl)

   
    thetext2 = thetext

    
    thetext2 = thetext2.replace("Python", "PYTHON")

    
    print("Modified thetext2:", thetext2)

if __name__ == "__main__":
    main()
