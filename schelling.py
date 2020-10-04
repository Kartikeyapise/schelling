import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph(N):
    return nx.grid_2d_graph(N, N)

def add_diagonal_edges(g):
    for (u,v) in g.nodes():
        if (u+1<=N-1) and (v+1<=N-1):
            g.add_edge((u,v),(u+1,v+1))
    for (u,v) in g.nodes():
        if (u-1>=0) and (v+1<=N-1):
            g.add_edge((u,v),(u-1,v+1))

def assign_type(g):
    for i in g.nodes():
        r=random.choice([0,1,2])
        g._node[i]['type']=r
        # labels[i]=r
def get_boundary_internal_nodes(g,N):
    l=[]
    for (u,v) in g.nodes():
        if u==0 or v==0 or u==N-1 or v==N-1:
            l.append((u,v))
    li=list(set(g.nodes())-set(l))
    return l,li

def num_unsatified_nodes_list(g,N,t):
    g=create_graph(N)
    add_diagonal_edges(g)
    assign_type(g)
    lu=[]
    for (u,v) in g.nodes():
        if g._node[(u,v)]['type']==0:
            continue
        else:
            count=0
            nbs=g.neighbors((u,v))
            for i in nbs:
                if g._node[i]['type']==g._node[(u,v)]['type']:
                    count=count+1
            if count<t:
                lu.append((u,v))
    return len(lu)

def visualise():
    nx.draw_networkx_nodes(g,pos,node_color='green',nodelist=type1_nodes)
    nx.draw_networkx_nodes(g,pos,node_color='red',nodelist=type2_nodes)
    nx.draw_networkx_nodes(g,pos,node_color='white',nodelist=empty_cells)
    nx.draw_networkx_labels(g,pos,labels=labels)
    nx.draw_networkx_edges(g,pos)
    plt.show()

def get_unsatisfied_nodes(g):
    lu=[]
    t=3
    for (u,v) in g.nodes():
        if g._node[(u,v)]['type']==0:
            continue
        else:
            count=0
            nbs=g.neighbors((u,v))
            for i in nbs:
                if g._node[i]['type']==g._node[(u,v)]['type']:
                    count=count+1
            if count<t:
                lu.append((u,v))
    return lu


def get_satisfied_nodes(g):
    lu=[]
    t=3
    for (u,v) in g.nodes():
        if g._node[(u,v)]['type']==0:
            continue
        else:
            count=0
            nbs=g.neighbors((u,v))
            for i in nbs:
                if g._node[i]['type']==g._node[(u,v)]['type']:
                    count=count+1
            if count>=t:
                lu.append((u,v))
    return lu

def make_a_node_satisfied(unsatisfied_nodes_list,empty_cells):
    if len(unsatisfied_nodes_list)!=0:
        node_to_shift=random.choice(unsatisfied_nodes_list)
        new_position=random.choice(empty_cells)
        t=g._node[node_to_shift]['type']
        g._node[new_position]['type']=t
        g._node[node_to_shift]['type']=0
        labels[node_to_shift],labels[new_position]=labels[new_position],labels[node_to_shift]
    else:
        pass


N=10
t=2
g=create_graph(N)
add_diagonal_edges(g)
assign_type(g)
pos=dict((n,n) for n in g.nodes())
labels=dict(((i,j),10*i+j) for i,j in g.nodes())
while 1:
    empty_cells=[i for i in g.nodes() if g._node[i]['type']==0]
    type1_nodes=[i for i in g.nodes() if g._node[i]['type']==1]
    type2_nodes=[i for i in g.nodes() if g._node[i]['type']==2]
    boundary_nodes,internal_nodes=get_boundary_internal_nodes(g,N)
    # internal_nodes=list(set(g.nodes())-set(boundary_nodes))
    if len(get_unsatisfied_nodes(g))==0:
        break
    make_a_node_satisfied(get_unsatisfied_nodes(g),empty_cells)
    visualise() 
# # print(boundary_nodes,internal_nodes)
# # print(list(g.neighbors((1,5))))
# # print(get_unsatisfied_nodes(g))
# # print(g.nodes(data=True))
# # visualise() 
visualise() 

