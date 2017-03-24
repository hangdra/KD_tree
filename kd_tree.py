import kd_node

# def getPathOfSearch(dp,root):
#     '''get path of node find the leaf node of the kd_tree'''
#     stack = [root]
#     current = root
#     while True:
#         x_level = current.deep%len(current.point)
#         if current.point[x_level]>dp[x_level]:
#             if current.left != None:
#                 stack.append(current.left)
#                 current = current.left
#             else:
#                 break
#         else:
#             if current.right != None:
#                 stack.append(current.right)
#                 current = current.right
#             else:
#                 break
#     return stack

def create_KD_tree(data_list,deep,father_node):
    """ creata kd tree by dataset ,use deep for level use deep(mod dimension)"""
    l = len(data_list)
    if l == 0:
        return
    # dimension of data_node
    dimension = len(data_list[0])
    # didn't use variance to chose 'dimension' separate the area,u can try it
    # variance
    # variance = 0
    x_level = deep%dimension
    data_list.sort(key=lambda x: x[x_level])
    point_root=data_list[l/2]
    root=kd_node.KD_node(point_root,x_level,None,None,father_node,deep)
    root.left=create_KD_tree(data_list[:l/2],deep+1,root)
    root.right=create_KD_tree(data_list[l/2+1:],deep+1,root)
    return root


def search_for_leaf_area_node(dp,root):
    """get the exact leaf node area the dp belone"""
    current = root
    while True:
        x_level = current.deep%len(current.point)
        if current.point[x_level]>dp[x_level]:
            if current.left != None:
                current = current.left
            else:
                break
        else:
            if current.right != None:
                current = current.right
            else:
                break
    return current

def get_node(dp,leaf,fatherNode):
    """ get exact node shorest between 'leaf' and 'fatherNode' """
    deep_node = leaf
    node = leaf
    dis_w = compute_distance(dp,node.point,len(dp))
    while deep_node.father!=fatherNode:
        node_now,deep_node=recursion(dp,deep_node)
        dis = compute_distance(dp,node_now.point,len(dp))
        if dis_w>dis:
            node = node_now
    return node

def recursion(dp,current_node):
    """ find shortest distance between node in sub tree of  of current_node's father and the given node dp"""
    Cdis = 0
    CN = None
    current = current_node

    dis = compute_distance(dp,current.point,len(dp))
    #init the shortest node and distance
    Cdis = dis
    CN = current

    father = current.father
    dis = compute_distance(dp,father.point,len(dp))
    if dis < Cdis:
        CN = father

    #check if there is any node belong to other half area (which separate by father's line)\
    #falls in the (circle) area (the centre of a circle 'CN' ,with radius 'dis')
    other_side_dis = abs(father.point[father.split]-dp[father.split])
    if other_side_dis < Cdis:
        other_child = None
        if father.left == current:
            other_child = father.right
        else:
            other_child = father.left
        if other_child!=None:
            current_new = search_for_leaf_area_node(dp,other_child)
            node_shortest_distance_in_that_path=get_node(dp,current_new,father)
            dis = compute_distance(dp,node_shortest_distance_in_that_path.point,len(dp))
            if dis < Cdis:
                CN = node_shortest_distance_in_that_path
    return CN,father

def compute_distance(d1,d2,p):
    """this method is going to compute the distance between two data point :d1 and d2,
    with p dimension"""
    SUM = 0
    for i in range(len(d1)):
        SUM += abs((d1[i]-d2[i])**p)
    return SUM**(1./p)

list=[[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]

root1 = create_KD_tree(list,0,None)

dp=[7,6]
leaf = search_for_leaf_area_node(dp,root1)

print get_node(dp,leaf,None).point
