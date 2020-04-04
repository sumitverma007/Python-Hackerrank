# def swap_case(s):
#     temp=""
#     for i in s:
#         if i>='a' and i<='z':
#             temp+=i.upper()
#         elif i>='A' and i<='Z':
#             temp+=i.lower()   
#         else:
#             temp+=i      
#     return temp

#alternate
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)