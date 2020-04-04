# t=int(input())
# while t>0:
#     a,b=map(int,input().split())
#     try:
#         res=a//b
#     except ZeroDivisionError as e:
#         print(f"Error Code:{e}")
#     except ValueError as f:
#         print(f"Error Code:{f}")
#     else:
#         print(res)
#     t-=1        
for test in range(int(input())):
    try:
        a,b = map(int,input().split()) 
        division_result = a // b
        print(division_result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)