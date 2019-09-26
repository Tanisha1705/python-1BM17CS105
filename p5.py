class Calldetails:

    def __init__(self,from_call,to_call,duration,typecall):
        self.from_call=from_call
        self.to_call=to_call
        self.duration=duration
        self.typecall=typecall

    def getter(self):
     return(self.from_call,self.to_call,self.duration,self.typecall)

class util:
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_call_string):
        for x in list_call_string:
            a=x.split(",")
            call=Calldetails(a[0],a[1],a[2],a[3])
            self.list_of_call_objects.append(call)
    def output(self):
        c1,c2,c3=0,0,0
        for x in self.list_of_call_objects:
              if(x.getter()[3]=="STD"):
                c1+=1
              elif (x.getter()[3]=="LOCAL"):
                  c2+=1
              else:
                  c3+=1
              print(x.getter())
        
        print("STD = ",c1)
        print("LOCAL = ",c2)
        print("ISD = ",c3)
        
            
call1="999000001,9852298329256,23,STD"
call2="999238923872,3425456,54,LOCAL"
call3="25342627,3625213436262,6,ISD"

list_call_string=[call1,call2,call3]
u=util()
u.parse_customer(list_call_string)
u.output()
        
            
