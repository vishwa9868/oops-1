import logging
from math import e 
logging.basicConfig(filename = 'loginfo.log' , level = logging.INFO , format = '%(asctime) %(levelname)s %(name)s %(message)s')




class string_task :
    
# Extract string
    
    def string_exctract (self , ext_string) :
        logging.info("we are about to extract string from index one to index 100 with a jump of 2")
        self.ext_string = ext_string
        try:
            if len(ext_string)==0:
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str= ext_string[::2]
                logging.info("Extracted string is %s:", str)
                return str
        except Exception as e:
          logging.exception(e)
          
          
          
#Reverse string
    def reverse_string (self ,revrs_str):
        logging.info("we are about extract reverse string")
        self.revrs_str = rev_string
        
    try:
        if str(::-1):
            raise TypeError("tuple object are immutable")
            logging.error("tuple datatype immutable")
        else:
            str = revrs_str[::-1]
            logging.info("reversed string is %s", str)
            return str
    except Exception as e:
        logging.exception(e)
        
        
# split string
    def string_split(self,splt_str):
        logging.info("we are about split string")
        self.splt_str=splt_str
        
    try:
        if len(str)==0:
            raise ValueError("empty string")
            logging.error("empty string")
        else:
            str= sring.upper()
            str1 = atr.split()
            logging.info("split stringis %s:" str)
            return str
    except Exception as e:
        logging.exception(e)
        
# lower string
    def string_lower(self, lstring):
        logging.info("we are about to lower string")
        self.lstring = lstring
        try:
            if len(lstring)==0:
                raise valueError("empty string")
                logging.error("empty string")
            else:
                str = lstring.lower()
                logging.info("lower string is %s:",str)
                return str
        except Exception as e:
            logging.exception(e)
        
        
# capitalize string
    def cap_str(self,capstr):
        logging.info("we are about capitalize string")
        self.capstr=capstr
        
        try:
            if len(capstr)==0:
                raise ValueError("empty string")
                logging.error("empty string")
                
            else:
                str = capstr.title()
                logging.info("Title string is %s", str)
                return str
        except Exception as e:
            logging.exception(e)    