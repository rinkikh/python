#find the fisrt occurance of target element in an array

def binary(arr,target):
    ans=-1
    l=0
    h=len(arr)-1
    
    while(l<=h):
        mid=l+(h-l)//2
        if (target==arr[mid]):
            ans=mid
            h=mid-1
        
        elif(target>arr[mid]):
            l=mid+1
        
        else:
            h=mid-1
            
    print(ans) 

arr=[1,1,2,2,2,2,2,2,4,5,6]  
target = 4    

binary(arr,target)        