import numpy as np
import os
from io import StringIO
global distance

def readfile():
    global distance
    # print("sys.executable directory: ", os.path.dirname(sys.executable))
    # dist = os.path.dirname(sys.executable).rsplit('/', 1)
    # dist = dist[0] + "/Dataset/Hopfield_dataset"
    dist = os.getcwd()
    print("\ndist: ", dist)
    distance = []
    with open(dist + '/TSP.txt', 'r') as f:
        for i, line in enumerate(f):
            if i != 0:
                distance.append(line[2:])
        distance = ''.join(distance)
        c = StringIO(distance)
        distance = np.loadtxt(c)
def generate_new_state(S):
    global distance
    new_state = list(S)
    changepoint = np.random.choice(distance.shape[0], 2)
    temp = new_state[changepoint[0]]
    new_state[changepoint[0]] = new_state[changepoint[1]]
    new_state[changepoint[1]] = temp
    return new_state

def calculate_distance(S):
    global distance
    pathlength = 0
    for i in range(len(S)-1):
        pathlength += distance[ S[i] ][ S[i+1] ]
    return pathlength

if __name__ == '__main__':
    global distance
    readfile()
    T = 100
    k = 0.99
    terminate = False
    S = np.arange(distance.shape[0])
    L = 50
    while terminate != True:
        for _ in range(L):
            new_state = generate_new_state(S)
            delta_t = calculate_distance(new_state) - calculate_distance(S)
            if delta_t < 0 or np.exp(-1*(delta_t)/T) >= np.random.rand(1)[0]:
                S = new_state
            if T < 20:
                terminate = True
        T = k * T
    citydef = dict({'0':'A', '1':'B', '2':'C', '3':'D', '4':'E', '5':'F', '6':'G', '7':'H', '8':'I', '9':'J', })
    way = [citydef[str(S[i])] for i in range(len(S))]
    print('-'.join(way), "Path Length: ", calculate_distance(S))
