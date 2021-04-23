import jieba
import json
import requests
import abc
#处理用户数据
class Data_base:
    def __init__(self,ask_type):
        if ask_type=='账户查询':
            self.my_url=r'https://lingxinyun.cn/sp/getId'
            self.user_account=''
        else:
            self.my_url=r'https://lingxinyun.cn/sp/getSandPlay'
            self.user_account={'id':ask_type}
        #print(self.my_url)
        self.response=requests.get(url=self.my_url,params=self.user_account)
        self.text=self.response.text
        self.json_data=json.loads(self.text)
    #@abc.abstractclassmethod
    def get_handled_data(self):
        
        #print(self.json_data)
        return self.json_data
    

data_from_web=Data_base('账户查询')
A=data_from_web.get_handled_data()
print(A)
class Get_gamedata(Data_base):
    def get_handled_data(self):
        make_moudle=[]
        delete_moudle=[]
        for i in range(len(self.json_data)):
            if self.json_data[i][0:2]=='创建':
                make_moudle.append(self.json_data[i][5:len(self.json_data[i])-1])
            if self.json_data[i][0:2]=='删除':
                delete_moudle.append(self.json_data[i][5:len(self.json_data[i])-1])
        print(make_moudle)
        print(delete_moudle)
'''
data_from_web=Get_gamedata('2800')
A=data_from_web.get_handled_data()
'''