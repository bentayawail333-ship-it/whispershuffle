# whispershuffle
terminal encryption tool that works on the bit level with images data bending mode --work in progress--


* the encryption tool implements on the American civil war called rail cipher by adding 2 other
parameters on top of rails which r offset and direction : 
- * rails : how may arrays to input bits into by applying a zigzag pattern 
- * offset : defines the rails jumped before starting the input of bits into the rails 
- * direction: can force the direction up or leave it as intended if offset's modulo by the cycle (=2*(r-1)) isnt 0 -aka in a middle rail-

* this initial version of this tool contains 3 modes classic shatter and glitch each handle a different type of input
* - classic : can encrypt n decrypt input strings 
* - shatter : handles txt files 
* - glitch : takes as arguments a picture (.jpg/.jpeg/.png) 


you can always use -h or --help either inside modes or in the tool in general to display the help menu should be plenty self-explanatory 
