#30thOctober2024
#CTS Problem 2
# input1=3
# input2=5
# input3={{1,0,1,0,1},{0,1,1,0,1},{1,1,1,0,0}}

def traffic_light(no_traffic_lignts,moments_in_traffic_lights,traffic_signals):
    index=0
    inx=-1
    for col in range(moments_in_traffic_lights):
        cnt=0
        for row in range(no_traffic_lignts):
            if(traffic_signals[row][col]==1):
                cnt+=1
        if(cnt==no_traffic_lignts):
            inx=index
        index+=1
    print(inx)

input1=3
input2=5
input3=[[1,0,1,0,1]
      ,[0,1,1,0,1],
       [1,1,1,0,0]]
traffic_light(input1,input2,input3)

input1=3
input2=5
input3=[[1,0,1,0,1],[0,1,0,0,1],[1,1,1,0,0]]
traffic_light(input1,input2,input3)