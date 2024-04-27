def valid(s):
    while "()" in s or "{}" in s or "[]" in s:
        s=s.replace("()","").replace("{}","").replace("[]","")
    return not s
for i in range(int(input())):
    a=input()
    if valid(a):
        print("true")
    else:
        print("false")
