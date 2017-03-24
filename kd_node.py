class KD_node:
    def __init__(self,point=None,split=None,lc=None,rc=None,father=None,deep=0):
        """
        point: data ponit
        split: split area
        lc,rc: left child , right child
        father: father node
        deep: deep
        """
        self.point=point
        self.split=split
        self.left=lc
        self.right=rc
        self.father=father
        self.deep=deep

    def toString(self):
        # print 'point : ' + str(self.point) + '; split : ' + str(self.split) + '; left :'+ self.left.toString()+'; right :' +self.right.toString()
        ln = False
        rn = False
        if self.left == None:
            ln = True
        if self.right == None:
            rn = True
        s = 'point : ' + str(self.point) + '; split : ' + str(self.split)+';deep : '+str(self.deep)
        if not ln:
            s += '; left:{'+ self.left.toString()+'}'
        else:
            s +='; left:{None} '
        if not rn:
            s += '; right:{'+ self.right.toString()+'}'
        else:
            s +='; right:{None} '
        return s
