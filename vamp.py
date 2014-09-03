#!/usr/bin/env python
### IMPORTS
from subprocess import call
import os

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
                    @     [Vamp Toolkyt]   #       `#    .#        .   #  [Ausar BLuhd]  +  ;    
                    ,       `    ;  ; #    +         +, #.         `   @    '     @      ,  ,`      
                   ;        +   .`  ; #   ,@          `'          ``   ;    ,     :      #   ,      
                   #        @   '   ' #  ;.'                      `+. `.    ``    `.     @   +      
                   .        :   @   + # '` @  .,:'+++######+':,.  .#,;,      :     +     ;   #      
                  '        ,    ;   # #+`  #,`        .##,;     `,@@ `@      +     +     ``  '      
                  #        #   `.   @ #`   '         '@`@+,@`     #@   #     #     .`     ;  `      
                 .`        +   ;    ''     ,         +`@@#,,#     @+    #    @      +     @   ;     
                 @        `.   #    :.     .        #;@ #.`@+'    @;    `;   ;      #     +   # """)
print("""
          [0. Exit] [1. Moniter Mode] [2. Tx Power] [3. Wireless Scanning] [4. Cracking Handshakes]""")


number = raw_input("what is your number? =///> ")
def menu(UserSupplyedNumber):
  if UserSupplyedNumber=="1":
    #file1 = os.open("ifconfgi.txt","w")
    print ("""
                                 What Network Card Do you want to use
      """)
    #vamp = os.open("vamp.txt)
    print("vamp")
    #call(["ifconfig", "-a","ifconfig.txt"])
    #Sprint(file1)
    #file1 = open("ifconfig.txt","w")

  elif UserSupplyedNumber=="2":
    print ("txt power")
    #file1 = open("ifconfig.txt","w")
  elif UserSupplyedNumber==3:
    Print()
  elif UserSupplyedNumber==4:
    Print()
  elif UserSupplyedNumber==5:
    Print()
  elif UserSupplyedNumber==6:
    Print()
  elif UserSupplyedNumber==7:
    Print()
  else :
    UserSupplyedNumber>0;
    print ("the number is greater then 9")
menu(number)