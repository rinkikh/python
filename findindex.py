# def index_num(series,sum):
    
#  serieslen = len(series)
#  indarr=[]
 
#  for i in range(serieslen-1):
#      for j in range(i+1,serieslen):
#       if series[i]+series[j]==sum:
#          indarr.append((i,j))
    
#  return indarr

# series=[5, 6, 8, 9, 10, 16]
# sum=15

# result=index_num(series,sum)
# print(result)


# two pointer technique

def index_num(series,sum):
    series.sort()
    indexarr=[]
    i=0
    j=len(series)-1
        
    while i<j:
           if series[i] +series[j] ==sum:
                indexarr.append((i,j))
               # i+=1
                #j-=1
            
           elif series[i] +series[j] >sum:
                j-=1
         
           else:
                i+=1
            
    print(indexarr)          
                      
        

series = [5, 6, 8, 9, 10, 16]
target_sum = 15

index_num(series, target_sum)