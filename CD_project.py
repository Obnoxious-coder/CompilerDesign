#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


keywords={"विराम":{"Token":"T_BREAK","Val":None},"संख्या":{"Token":"T_FLOAT","Val":None},"विकल्प":{"Token":"T_CASE","Val":None} ,"अक्षर":{"Token":"T_CHAR","Val":None},"अगर":{"Token":"T_IF","Val":None},"अन्य":{"Token":"T_ELSE","Val":None},"पूर्णांक":{"Token":"T_INT","Val":None},"ऑटो":{"Token":"T_AUTO","Val":None},"स्थिर":{"Token":"T_CONST","Val":None},"छोटा":{"Token":"T_SHORT","Val":None},"ढांचा":{"Token":"T_STRUCT","Val":None},"अचिन्हित":{"Token":"T_UNSIGNED","Val":None},"जारी":{"Token":"T_CONTINUE","Val":None},"दीर्घ":{"Token":"T_LONG","Val":None},"चिन्हिता":{"Token":"T_SIGNED","Val":None},"स्विचा":{"Token":"T_SWITCH","Val":None},"रिक्त":{"Token":"T_VOID","Val":None},"डिफ़ाल्टा":{"Token":"T_DEFAULT","Val":None},"रजिस्टर":{"Token":"T_REG","Val":None},"साइजोफ":{"Token":"T_SIZE_OF","Val":None},"डप्रकारव्याख्या":{"Token":"T_TYPE_OF","Val":None},"परिवर्तनशील":{"Token":"T_VOLATILE","Val":None},"डू":{"Token":"T_DO","Val":None},"वापसी":{"Token":"T_RETURN","Val":None},"स्थिर":{"Token":"T_STATIC","Val":None},"संघ":{"Token":"T_UNION","Val":None},"जबकि":{"Token":"T_WHILE","Val":None}}
arithmetic_op={"+":{"Token":"T_PLUS","Val":None},"-":{"Token":"T_SUB","Val":None},"*":{"Token":"T_MUL","Val":None},"/":{"Token":"T_DIV","Val":None},"&":{"Token":"T_AND","Val":None},"|":{"Token":"T_OR","Val":None},"^":{"Token":"T_XOR","Val":None}}
relational_op={"<":{"Token":"T_LESS","Val":None},">":{"Token":"T_MORE","Val":None},"=":{"Token":"T_EQ","Val":None},"<=":{"Token":"T_LESS_EQ","Val":None},">=":{"Token":"T_MORE_EQ","Val":None},"==":{"Token":"T_EQ_EQ","Val":None}}
special_sym={";":{"Token":";","Val":None},",":{"Token":",","Val":None},"(":{"Token":"(","Val":None},")":{"Token":")","Val":None},"{":{"Token":"{","Val":None},"}":{"Token":"}","Val":None},"[":{"Token":"[","Val":None},"]":{"Token":"]","Val":None}}
var={}


# In[3]:


def is_var(word):
    x=re.search("^[$]",word)
    if x==None:
        return False
    else:
        return True
def is_const(word):
    x=re.search("[0-9]+",word)
    y=re.search("[0-9]+[.][0-9]+",word)
    if x==None and y==None:
        return False
    else:
        return True


# In[4]:


def Parse_(t_text):
    parsing_list=[]
    for t_word in t_text:
        if t_word in keywords.keys():
            parsing_list.append(keywords[t_word])
        elif t_word in arithmetic_op.keys():
            parsing_list.append(arithmetic_op[t_word])
        elif t_word in relational_op.keys():
            parsing_list.append(relational_op[t_word])
        elif t_word in special_sym.keys():
            parsing_list.append(special_sym[t_word])
        elif t_word in var.keys():
            parsing_list.append(var[t_word])
        else:
            if(is_var(t_word)):
                var_name="T_VAR"+t_word
                var[t_word]={"Token":var_name,"Val":None}
                parsing_list.append(var[t_word])
            elif(is_const(t_word)):
                var_name="T_Const"+t_word
                var[t_word]={"Token":var_name,"Val":int(t_word)}
                parsing_list.append(var[t_word])
            else:
                parsing_list.append("error")
    return parsing_list


# In[5]:


def Tokenize_(text):
    for r in range(len(text)):
        if(text[r]==";"):
            text=text[0:r]+" "+text[r:]
        elif text[r]==",":
            text=text[0:r]+" "+text[r]+" "+text[r+1:]
        
    return text.split()


# In[6]:


def read_from_file(f_loc):
    f=open(f_loc,"r",encoding="utf8")
    text=f.read()
    return text


# In[ ]:


if __name__=="__main__":
    choice=input("ENTER C FOR CONSOLE ELSE F FOR FILE")
    if choice=='c' or choice=='C' :
        while True:
            text=input('Hindi_compiler>>>')
            t_text=Tokenize_(text)
            print(Parse_(t_text))
    else:
        f_name=input("Enter File name")
        f_loc=".\Files\\"+f_name
        text=read_from_file(f_loc)
        t_text=Tokenize_(text)
        print(Parse_(t_text))
        
        


# In[ ]:





# In[ ]:




