word = "man"
word=word.upper()
word_show = "_"*len(word)
trynum = 0
ok_list= []
no_list = []
while True :
    ans = input.upper()
    result = word.find(ans)
    if result == -1 :
        print("오답")
        trynum += 1
        no_list.append(ans)
    else :
        print("정답")
        ok_list.append(ans)
        for i in range(len(word)) :
            if word[i] == ans :
                word_show = word_show[:i + ans + word_show[i+1:]]
            print(word_show)
    if trynum == 7 :break
    if word_show.find("_") == -1 : break