def datetime():
    import datetime
    result=datetime.datetime.now()
    return str(result)


viewer=input("Enter who is watching the list is it the contender or the master\n")
viewer= viewer.capitalize()
if viewer == "Master":
    diet_or_exercise=int(input("Enter 1 for exercise and 2 for diet\n"))
    if diet_or_exercise== 1:

        viewer_choice=int(input("Hello sir, whose data is going to be inputed today, type 1 for Hamad,2 for rohan, 3 for wasil\n"))
        if viewer_choice==1:
           times1=int(input("How many exercise are there to be done today\n"))
           for i in range(0,times1,1):
             with open("Hamad_exercise.txt",'a') as h:
               input_text1= input("Enter the exercises to be performed\n")
               h.write("["+datetime()+"]"+" - ")
               h.write(input_text1+"\n")
               

        elif viewer_choice==2:
           times2=int(input("How many exercise are there to be done today\n"))
           for i in range(0,times2,1):
             with open("Rohan_exercise.txt",'a') as r:
               input_text2=input("Enter the exercises to be performed\n")
               r.write("["+datetime()+"]"+" - ")
               r.write(input_text2+"\n")
          
        else:
          times3=int(input("How many exercise are there to be done today\n"))
          for i in range(0,times3,1):
             with open("Wasil_exercise.txt",'a') as w :
               input_text3= input("Enter the exercises to be performed\n")
               w.write("["+datetime()+"]")
               w.write(input_text3+"\n")
    
    else:
       
       master_choice=int(input("Enter 1 for Hamad, 2 for Rohan, 3 for Wasil\n"))
       if master_choice==1:
          for i in range(0,3,1):
            with open("Hamad_diet.txt",'a') as h:
              dtext1=input("Enter the time of the meal and the meal\n")
              h.write("["+datetime()+"]"+" - ")
              h.write(dtext1+"\n")
              

       elif master_choice==2:
          for i in range(0,3,1):
             with open("Rohan_diet.txt",'a') as r:
               dtext2=input("Enter the time of the meal and the meal\n")
               r.write("["+datetime()+"]"+" - ")
               r.write(dtext2+"\n")
               

       else:  
          for i in range (0,3,1):
             with open("Wasil_diet.txt",'a') as w:
               dtext3=input("Enter the meal name and the meal\n")
               w.write("["+datetime()+"]"+" - ")
               w.write(dtext3+"\n")
               
else:
  type=int(input("Do u want to retrieve the exercise part or the diet part, press 1 for exercise, 2 for diet\n"))
  if type==1:
      person=int(input("Which persons informations u want to retrieve type 1 for hamad, 2 for rohan, 3 for wasil\n"))
      if person==1:
         with open("Hamad_exercise.txt",'r') as h:
            for line in h:
               print(line)

      elif person==2:
         with open("Rohan_exercise.txt",'r') as r:
            for line in r:
               print(line)         

      else:
         with open("Wasil_exercise.txt",'r') as w:
            for line in w:
               print(line) 
 
  else:
     theguy=int(input("Which persons informations u want to retrieve type 1 for hamad, 2 for rohan, 3 for wasil\n"))
     if theguy==1:
        with open("Hamad_diet.txt",'r') as h:
           for line in h:
              print(line)

     elif theguy==2:
        with open("Rohan_diet.txt",'r') as r:
           for line in r:
              print(line)


     else:
        with open("Wasil_diet.txt",'r') as w:
           for line in w:
              print(line)
      
       
