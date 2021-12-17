T = int(input())

w = []

for x in range(T):
    each_word = input()
    w.append(each_word)

for word in w:
    #ბოლოდან - არაზრდადი სუფიქსის წერტილის პოვნა
    i = len(word) - 1
    while i > 0 and word[i - 1] >= word[i]:
        i = i - 1
    
    #თუ საწყის სიტყვაზე ლექსიკოგრაფიულად დიდი სიტყვა არ არსებობს - no answer
    if i == 0:
        print('no asnower')
    #თუ არსებობს
    else:
        #ბოლოდან - სუფიქსის წერტილზე დიდი & ყველაზე მარჯვენა წერტილის პოვნა
        j = len(word) - 1
        while word[j] <= word[i - 1]:
            j = j - 1
        
        #სუფიქსის შეტრიალება
        l = list(word)
        
        l[i - 1], l[j] = word[j], word[i - 1]
        
        l[i:] = l[len(word) - 1:i - 1:-1]
        
        #საბოლოო შედეგი
        word = ''.join(l)
    
        print(word)


