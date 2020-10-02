T = int(input())
top_url = [[0,0]]

for case in range(T):
    for i in range(10):
        url,score = input().split()
        score = int(score)
        if score > top_url[0][1]:
            top_url = [[url,score]]
        elif score == top_url[0][1]:
            top_url.append([url,score])
    print("Case #%d:"%(case+1))
    for j in range(len(top_url)):
        print(top_url[j][0])
    top_url = [[0,0]]
