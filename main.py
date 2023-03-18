# python3

def parallel_processing(n, m, data):
    output = []
    GotTime = [0] * n 
    
    for i in range(m):
        next_t = min(range(n), GotTime.__getitem__) 
        output.append((next_t, GotTime[next_t])) 
        GotTime[next_t] = GotTime[next_t] +  data[i]  

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    data = list(map(int, input().split()))


    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread, starting in result:
        print(thread, starting)


if __name__ == "__main__":
    main()
