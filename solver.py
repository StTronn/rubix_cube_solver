import rubik
from collections import deque

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    visited_front={}
    parent_front={}
    q_front=deque()
    parent_front[start]=None
    q_front.append(start)
    visited_front[start]=1

    visited_back={}
    parent_back={}
    q_back=deque()
    parent_back[end]=None
    q_back.append(end)
    visited_back[end]=1

    mid_point=end
    while q_front:
        cur_front=q_front.popleft()
        if cur_front==end:
            break
        for item in get_neighbours(cur_front):
            if item not in visited_front:
                visited_front[item]=1
                parent_front[item]=cur_front
                q_front.append(item)
                
        #single bfs
        cur_back=q_back.popleft()
        for item in get_neighbours(cur_back):
            if item not in visited_back:
                visited_back[item]=1
                parent_back[item]=cur_front
                q_back.append(item)
        if visited_front.keys()==visited_back.keys():
            front_set=set(visited_front)
            back_set=set(visited_back)
            mid_point=list(front_set.intersection(back_set))[0]
            break
    ret=[]
    x=mid_point
    #x=end
    while x!=None:
        ret.append(x)
        x=parent_front[x]
    ret.pop(-1)
    ret.reverse()
    x=parent_back[mid_point]
    while x!=None:
        ret.append(x)
        x=parent_back[x]
    return ret

def get_neighbours(config):
    ret=[]
    for perm in rubik.quarter_twists:
        ret.append(rubik.perm_apply(perm,config))
    return ret

# start = rubik.I
# middle = rubik.perm_apply(rubik.F, start)
# end = rubik.perm_apply(rubik.L, middle)
# ans = shortest_path(start, end)
# print (ans)
# print ([rubik.F,rubik.L])

#test_start=(6, 7, 8, 0, 1, 2, 9, 10, 11, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)

# start = rubik.I
# end = rubik.perm_apply(rubik.F, start)
# ans = shortest_path(start, end)
# print (ans,rubik.F)