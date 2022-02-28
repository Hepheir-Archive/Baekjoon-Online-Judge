import sys
import math

sys.setrecursionlimit(int(1e5))

SEGMENT_TREE = None # Node [(parent, left, right, depth), value]

def left(node_id):
    return node_id<<1

def right(node_id):
    return (node_id<<1)|1

def parent(node_id):
    return node_id>>1

def depth(node_id):
    return math.ceil(math.log2(node_id+1))

def make_segment_tree(array):
    global SEGMENT_TREE
    n_nodes = 4*len(array)
    SEGMENT_TREE = [[None]*len(array)]+[0]*n_nodes
    # +1 is for 0-base-index -> 1-base-index
    # use SEGMENT_TREE[0] as a Lookup table of node_ids correspond to array elements
    make_tree(array, 1, 0, len(array)-1)

def make_tree(array, node_id, start, end):
    # make current node
    if start == end:
        SEGMENT_TREE[0][start] = node_id # make look up table
        SEGMENT_TREE[node_id] = array[start]
    else:
        mid = (start+end)//2
        left_id = node_id<<1
        right_id = (node_id<<1)|1
        make_tree(array, left_id, start, mid)
        make_tree(array, right_id, mid+1, end)
        SEGMENT_TREE[node_id] = SEGMENT_TREE[left_id] + SEGMENT_TREE[right_id]
    return SEGMENT_TREE[node_id]
def query(search_start, search_end):
    answer = 0
    start_node_id = SEGMENT_TREE[0][search_start-1]
    end_node_id = SEGMENT_TREE[0][search_end-1]
    # _query_...()에서는 짝수번 노드가 left, 홀수번 노드가 right임을 이용.
    # 여기서는 가지치기를 한다.
    def _query_start_node():
        global SEGMENT_TREE
        nonlocal answer, start_node_id
        if (start_node_id & 1):
            answer -=  SEGMENT_TREE[start_node_id-1]
        start_node_id >>= 1 # parent_node_id
    def _query_end_node():
        global SEGMENT_TREE
        nonlocal answer, end_node_id
        if not (end_node_id & 1):
            answer -=  SEGMENT_TREE[end_node_id+1]
        end_node_id >>= 1 # parent_node_id
    # Match start-node's depth and end-node's depth
    while depth(start_node_id) > depth(end_node_id):
        _query_start_node()
    while depth(start_node_id) < depth(end_node_id):
        _query_end_node()
    # Find common parent-node
    while start_node_id != end_node_id:
        _query_start_node()
        _query_end_node()
    answer += SEGMENT_TREE[start_node_id] # start_node_id is common_parent_id
    print(answer)

def update(index, value):
    node_id = SEGMENT_TREE[0][index] # 1-base -> 0-base
    SEGMENT_TREE[node_id] = value
    while (node_id & ~1): # if has parent node
        node_id >>= 1 # parent_node_id
        SEGMENT_TREE[node_id] = SEGMENT_TREE[left(node_id)] + SEGMENT_TREE[right(node_id)]

if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split())
    numbers = [int(sys.stdin.readline()) for n in range(N)]
    make_segment_tree(numbers)
    del numbers
    for _ in range(M+K):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 1:
            update(b-1, c)
        elif a == 2:
            query(b, c)