#!/usr/bin/env python



################## 
#IMPORTS
#################

import os
import shutil



#################
#MAIN SCREEN
################


print("""

                          '  + +    `,      #         '     @  #         ;    ,    ;                
                          # + #     #      :`        `:    ##  @`    :   #     ,    .               
                          . :..    '      `:         #    ..+  '#    #   .`    #    #               
                         ; # #     '      @        `@     + .  : '   ``   #    #    #               
                         # ::     :      '        `@`    # :  `` :`   #   +    ,    ,               
                         ## # ,   @      ;       .;;    +  #  ,   @   ;   ``    ,   `.              
                         ;::  :   ;     #       ,:#    +`  +  #   `,   ,   +    +    '              
                         @ @ .`  .     ..      :.@    +`  `.  +    #   @   @    @    @              
                        ,:., '   +     @      ;.'    #    '  .`     ,  ;   :    :    '              
                        @ @  @   #    .`     ;.,.   @     +  @      @   .  `.   `.   ,              
                        ,`#  +   +    #     ;``:  `+     `` `,      .`  +   :    +    .             
                       + #:  ,   ,   .`    ;. +  ::      #  #        #  #   #    #    '             
                       + +  `   ``   @    :. #  #`       :  ,        '  ;   #    '    @             
                      .`'+  ;   ,   `.   ,, #  @        ;  @          . ``  +    ``   #             
                      # +@  #   ;  .#   .: # :;         + ..          #  :  :     ;   '             
                      '` ;  #   '   +@;.; ;`#`         ,  #           ; ,+  `     #   .             
                     ``# ,  #   #  :   +#+:+           # '          :##: #   .    +    .            
                     ; @`.  '   #  @  # .@;@.         ,``:      `'#:   # '   ;    .    '            
                     #`@`.  :   #  : # `@   `++       @ @     ,@.   ,;`+ ,   +     ,   #            
                     #:@``  ,   # .`#@@@@@@@'` ,#,   .`'    :+ `#@@@@@#@@#`  #     +   @            
                     ;#@``  .   ' ' @@@:+ ,+@@#      #`:      ;@@;.  @ .@@@  #     #   '            
                     .#@`.  .   ; @+@@  :  : `@@    ; +       @;  :  :  @;@  @     '   ,            
                    .`'#`.  .   , #@ :,  . :  ;     '@         @  ; :   + @  +     .`  `.           
                    : :@`.  .    `',     # .  ,    #+          `: ` #.;#. #  '      ,   :           
                    '`.@ ,  .    ;+   ,##++@#+;   .+`         `,:,,.`   `.+  :      #   +           
                    +` # :  ,    @@               @.                     ;': ,      #   @           
                    #, # ;  #    ##   _O_        +;                      +;' .      +   +           
                    @; + +  @    +'    |        `+                       @:# .      ,   ;           
                    @' + #  #    .``            ;                        +,@ ..     ``  .           
                    @' ' @  #    ` +                   .                 :;@ .:      :   .          
                    @' : @  @;   ``#                   ,                  #@ .+      +   '          
                    @; . #  #@    #:                  ``                  #@ .@      @   #          
                    #:  .,  #:    :.;                 ,                  .`# ,+      +   #          
                    '.  ' , + :   @ @                 ,                  +,+ ;:      :   '          
                    ,`. @ # : #   #'@`                :                  @`' #``     .`  .          
                     :' + # ```.  #  :                .                 `: : # ,      ,  `.         
                     #@ : .  ; #  :  @                 `                #' ` + #      '   :         
                     .:`   + # @. `` .`                                 '@. `` #      @   +         
                      ##   ; ' +#  '  #                                ; #' '  +      #   @         
                      ,@    +`.: + #  #,                               + ;# @  ,      ;   +         
                       @`   ; #` .,.` #'           `:'    ':`         #  ,@`,   .     `   :         
                       ,#    #'   ;`# # #                            ,. ` +'    '      ,  ``        
                      , #`   ..;  :': #  #                          .:  : .@    @      +   :        
                      #  #    #@  @ +++   '.                       ::   #.,,    '      @   #        
                      +  '    @@. # '+'    +'                     +#    #'#.`   ,`     +   #        
                     `.       '.@ ' @ '    # @                   @ #    #@.`.    ,     ,   '        
                     '        . # , # '    #  #`               .'  +    '@  ,    #     `.  .        
                     #       ,   `  # '    #   :;             +.   ;    ,'  ;    #      '   ,       
                     ,       +   ;  + +    #     @          `#     ,   ..   #    ;      @   '       
                    ;        #   #  + #    @      ',       +,      .   ;`   @     `     +   @       
                    @     [Vamp Toolkit]   #       `#    .#        .   #  [Ausar Bluhd]  +  ;    
                    ,       `    ;  ; #    +         +, #.         `   @    '     @      ,  ,`      
                   ;        +   .`  ; #   ,@          `'          ``   ;    ,     :      #   ,      
                   #        @   '   ' #  ;.'                      `+. `.    ``    `.     @   +      
                   .        :   @   + # '` @  .,:'+++######+':,.  .#,;,      :     +     ;   #      
                  '        ,    ;   # #+`  #,`        .##,;     `,@@ `@      +     +     ``  '      
                  #        #   `.   @ #`   '         '@`@+,@`     #@   #     #     .`     ;  `      
                 .`        +   ;    ''     ,         +`@@#,,#     @+    #    @      +     @   ;     
                 @        `.   #    :.     .        #;@ #.`@+'    @;    `;   ;      #     +   # """)


##################
# DEFINITIONS
###################
def workstation():
 #shutil.copy2('lilo.automode_workstation', 'cool')
  copyfile(lilo.automode_workstation, dst)
  menu()
##################
#FUNCTIONS
##################
def menu():
  print("""
                   [1. Deploy Workstation] [2. Deploy Server] [3. Deploy Router ] 

                    [4. Deploy Auditing Machine]
                   """)
  cec = raw_input("What are we Deploying? =///> ")
  selection("cec")
def selection(choolie):
  if choolie=="1":
      workstation()
      menu()
  elif choolie=="2":
    print ("Option 2")
    #file1 = open("ifconfig.txt","w")
    menu()
  elif choolie=="3":
    print("Num3")
    menu()
  elif choolie=="4":
    print("s")
    menu()
  elif choolie=="5":
    print("sd")
    menu()
  elif choolie=="6":
    print("sdgf")
    menu()
  elif choolie=="7":
    print("sdfg")
    menu()
  else:
    print ("Quitting")

###################
#Calls
###################


menu()