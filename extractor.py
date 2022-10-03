import re
 
try:
    file =  open("[UPLOAD YOUR RAW SQL FILE PATH]", "r",encoding='utf8')
    for line in file:
        lines = line.strip()
        emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", lines)
      
        savs =  open("CREATEFILE_FOR_SAVING EXTRACTED EMAILS ","a",encoding='utf8')
        
        fil = savs.write("\n".join(emails))
        print(fil)
        savs.write("\n")
        savs.close()
    
except FileNotFoundError as e:
    print(e)
