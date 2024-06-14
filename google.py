import googletrans 
from  googletrans import Translator 
#print(googletrans.LANGUAGES)
transl = Translator()
output = transl.translate("em dep qua" , src = "vi", dest = "en"); 
print(output.text)

