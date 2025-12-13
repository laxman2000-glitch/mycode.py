class filehandling:
    def __init__(self,code):
        self.code = code 
        
    def basic (self,name):
        with open(self.code,"a+") as f:
            
            f.write(name+"\n")
            f.write("bye\n")
    
    
    def alogoritum(self):
        with open(self.code,"r") as f:
            for i in f:
                if "bye" in i :
                    print("appened sucessfully")
                    return

            print ("append not sucessfull retry again")
                        
write_name= str(input("what do you want to right"))
sas = FileHandling("code.txt")
sas.basic(write_name)
sas.alogoritum()
    
    

