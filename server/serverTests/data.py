import pickle
from datetime import datetime
from joblib import dump, load
import os

class PFit():
    def __init__(self, *args, **kwargs):
        self.args=args
        self.kwargs=kwargs


class ExpSet():

    def __init__(self,pathDump:str=os.getcwd()):
        self.pFits=[]
        self.pathDump=pathDump
        #if os.path.isfile() :

    def addPFit(self,pFit:PFit):
        self.pFits.append(pFit)
        self.dump()

    @staticmethod
    def load(path=os.getcwd()):
        if os.path.isfile(path+"/ExpSet"):
            f=open(path+"/ExpSet",'rb')
            myExp= pickle.load(f)
            myExp.pathDump=path
            return myExp
        print("No ExpSet @ "+path)
        return ExpSet(pathDump=path)

    def dump(self):
        f = open(self.pathDump+'/ExpSet', 'wb')
        pickle.dump(self, f)
        f.close()
