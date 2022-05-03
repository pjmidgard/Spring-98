from time import time
import os
import binascii
import math
import os.path

lenf=0
name=""
add_bits=""
Make_togher=""

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":
                        Deep3=8

                        i=1

                    if namez=="e":
                        i=2
                 
                    Number_add_plus_one=""
                    Prime_Not=""
                    Times_6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    compress_or_not_compress=1
                    Circle_times3=0

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    	
                    nac=len(nameas)
                    
                   
                    s=""

                    Equal_info_between_of_the_cirlce_of_the_file=""
                    Equal_info_between_of_the_cirlce_of_the_file_2=""

                    Prime_Not=""
                    Times_6=""

                    Translate_info_Decimal=""

                    D=0

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7==0:
                        	 raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                                   
                        Equal_info_between_of_the_cirlce_of_the_file_23=""
 
                        sda18=""
                        Equal_info_between_of_the_cirlce_of_the_file_29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    

                                    if Circle_times3==1:
                                        Equal_info_between_of_the_cirlce_of_the_file_2=sda
                            
                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_2, 2)
                                
                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                             
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    
                                    data=width_bits3
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1

                                    Equal_info_between_of_the_cirlce_of_the_file_2=sda

                                    lenf3=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                lenf2=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**40)-1:
                                        raise SystemExit

                                #########################################################################################################################################################
                                
                                
                                if i==1:

                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file_2)

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                 
                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    
                                    
                                    #Extract
                            
                                    s=""

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                  
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                   
                                    g=0

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2

                                    
                                    if   Circle_times2==0 and SpinS==0:
                                    	Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file
                                    	SpinS=1

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)                      
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                                
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                
                                    add_bits=""

                                    Times_6=""

                                    #Compression

                                    sda10=""
                                    Translate_info_Decimal=""
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                 
                                    

                                    if Circle_times2>=(2**8)-2:
                                            compress_or_not_compress=2

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                            
                                    
                                    Find_center_info=Equal_info_between_of_the_cirlce_of_the_file

                                    block=0
                                    Find_Save=1
                                    Find_Save4=0
                                    Find_Save5=0
                                    block2=0

                                    while block<lenf6:

                                           Find_center_info1=Find_center_info[block:block+6]
                                           Find_center_info2=Find_center_info[block:block+5]
                                           Find_center_info3=Find_center_info[block2:block2+6]

                                           if Find_center_info3=="111111" and Find_Save5==0:
                                                Find_center_info=Find_center_info[:block2]+"000000"+Find_center_info[block2+6:]
                                                
                                               

                                                   
                                           elif Find_center_info1=="000000" and Find_Save4==0 and Find_Save5==0 and Find_Save==5:
                                                    Find_Save_binary=bin(Find_Save)[2:]
                                                    lenf=len(Find_Save_binary)

                                                    add_bits8=""
                                                    count_bits=5-lenf%5
                                                    z=0
                                                    if count_bits!=0:
                                                        if count_bits!=5:
                                                                while z<count_bits:
                                                                        add_bits8="0"+add_bits8
                                                                        z=z+1

                                                    Find_center_info3=add_bits8+Find_Save_binary
                                                    check_numner_equal=add_bits8+Find_Save_binary
                                                    
                                                    Find_Save4=1
                                                    if check_numner_equal!=Find_center_info2:
                                                            
                                                            #print(check_numner_equal)
                                                            Find_center_info=Find_center_info[:block]+Find_center_info3+Find_center_info[block+6:]
                                                            
                                                    elif check_numner_equal==Find_center_info2:
                                                            Find_center_info=Find_center_info[:block2]+"111111"+Find_center_info[block2:]
                                                            Find_center_info=Find_center_info[:block]+Find_center_info[block+6:]
                                                        
                                                            
                                                            
                                                    
                                           Find_Save=Find_Save+1
                                           if Find_Save==30:
                                                   Find_Save=1
                                                   block2=block
                                                   Find_Save4=0
                                                   
                                           block=block+6
                                     
                                           
                                    Equal_info_between_of_the_cirlce_of_the_file_17=Find_center_info
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)

                                    if lenf6==lenfS:
                                        Deep3=lenfS

                                    
                                   
                                    Circle_times2=Circle_times2+1
                                    
                                    if   lenfS<=Deep3:
                                    	   
                                            Times_comperession=bin(Circle_times2)[2:]
                                            lenf=len(Times_comperession)

                                            add_bits7=""
                                            count_bits=8-lenf%8
                                            z=0
                                            if count_bits!=0:
                                                if count_bits!=8:
                                                        while z<count_bits:
                                                         	add_bits7="0"+add_bits7
                                                         	z=z+1    
                                    

                                    if   lenfS<=Deep3:
                                                Equal_info_between_of_the_cirlce_of_the_file_17="1"+Equal_info_between_of_the_cirlce_of_the_file_17
                                                lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                add_bits=""
                                                count_bits=8-lenf%8
                                                if count_bits==8:
                                                	count_bits=0
                                                count_bits2=count_bits
                                                z=0
                                                if count_bits!=0:
                                                        if count_bits!=8:
                                                                while z<count_bits:
                                                                        add_bits="0"+add_bits
                                                                        z=z+1

                                   

                                    if   lenfS<=Deep3:
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bits7+Times_comperession+add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                    if   lenfS<=Deep3:
                                                
                                    		L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    		n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                    		width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    		width_bits=(width_bits//8)*2
                                    		width_bits=str(width_bits)
                                    		width_bits="%0"+width_bits+"x"
                                    		width_bits3=binascii.unhexlify(width_bits % n)
                                    		width_bits2=len(width_bits3)
                                    		add_bitszzza=""
                                    		add_bitszs=""
                                    		Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                    		
                                    		with open(nameas, "wb") as f2:
                                    			f2.write(width_bits3)
                                    	
                                    		x2 = time()
                                    		x3=x2-x
                                    		xs=float(x3)
                                    		return print(x3)
                                    		
                                if i==2:

                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                              
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    sda10=""
                                    Translate_info_Decimal=""
                                  
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                
                                    Number_of_the_file=0
                                    Prime_Not=0
                                 
                                    if C==1:
                                        T=2

                                        if Equal_info_between_of_the_cirlce_of_the_file[0:1]=="1":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[1:]
                                        
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:2]=="01":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[2:]
                                                
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:3]=="001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[3:]


                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:4]=="0001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[4:]

                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:5]=="00001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[5:]

                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:6]=="000001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[6:]
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:7]=="0000001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[7:]
    
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:8]=="00000001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
        
    
                                        if C==1 and T!=0:
                                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file
                                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                                    Find_center_info=Equal_info_between_of_the_cirlce_of_the_file
                                                    

                                                    block=0
                                                    Find_Save=1
                                                    Find_Save4=0
                                                    Find_Save5=0
                                                    block2=0

                                                    while block<lenf6:

                                                           Find_center_info1=Find_center_info[block:block+6]
                                                           Find_center_info2=Find_center_info[block:block+5]
                                                           Find_center_info3=Find_center_info[block2:block2+6]

                                                           if Find_center_info3=="000000" and Find_Save5==0:
                                                                Find_center_info=Find_center_info[:block2]+"111111"+Find_center_info[block2+6:]
                                                                
                                                               
                                                          
                                                                  
                                                                   
                                                           if Find_Save4==0 and Find_Save5==0:
                                                                    Find_Save_binary=bin(Find_Save)[2:]
                                                                    lenf=len(Find_Save_binary)

                                                                    add_bits8=""
                                                                    count_bits=5-lenf%5
                                                                    z=0
                                                                    if count_bits!=0:
                                                                        if count_bits!=5:
                                                                                while z<count_bits:
                                                                                        add_bits8="0"+add_bits8
                                                                                        z=z+1

                                                                    Find_center_info3=add_bits8+Find_Save_binary
                                                                    check_numner_equal=add_bits8+Find_Save_binary
                                                                    
                                                                    Find_Save4=1
                                                                    if check_numner_equal==Find_center_info2:
                                                                            Find_center_info=Find_center_info[:block]+"000000"+Find_center_info[block+6:]
                                                                          
                                                                    elif check_numner_equal=="111111":
                                                                            Find_center_info=Find_center_info[:block2]+Find_center_info[block2+6:]
                                                                            Find_center_info=Find_center_info[:block2]+Find_center_info[block2+6:]
                                                                            Find_Save5=1
                                                                            

                                                                         
                                                           
                                                                            
                                                                            
                                                                            
                                                                    
                                                           Find_Save=Find_Save+1
                                                           if Find_Save==30:
                                                                   Find_Save=1
                                                                   block2=block
                                                                   Find_Save4=0  
                                                           block=block+6
                                                                   
                                                           
                                                                  
                                                           
                                                     
                                                           
                                                    Equal_info_between_of_the_cirlce_of_the_file_17=Find_center_info
                                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                
                                                
                                       
                                    Times_6=Number_add_plus_one
                                    Number_add_plus_one=""
                                      
                                    #####################################################################################################################################################
                                   
                                    Prime_Not=""
                                    
                                    
                                    
                                     
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                   

                                    if i==2:
                                        Make_togher=""
                                        Make_togher=Times_6
                                        Number_add_plus_one=""
                                        add_bits=""
                                        if C==1 and T!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==T:
                                        	   
                                            
                                        
                                            if C==1 and T!=0:
 
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_17[1:]
                                            	lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	#print(lenf14)
                                            	
                                            		
                                            	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                         
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)

                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(width_bits3)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
