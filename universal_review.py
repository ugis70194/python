import queue
import webbrowser

filePath = "review_urls.txt"

urls = queue.Queue()
browser = webbrowser.get()
unsolved = []

try : 
    with open(filePath, mode = "r") as file : 
        for url in file : 
            url = url.strip()
            if(url != "") : 
                urls.put(url)
                unsolved.append(url)
except FileNotFoundError :
    print("create File...")
    with open(filePath, mode = "w") as file : pass

In_use = True
unsolved.reverse()

while In_use : 
    print("The numbor of problems in queue is " + str(urls.qsize()) + '\n')
    print("Mode Select" + "\n" + "push : i" + "\n" + "pop : p" + "\n" + "quit : q")
    commnd = input()
    if commnd == 'i' : 
        print("Please input URL")
        new_ploblem = input()
        urls.put(new_ploblem)

    if commnd == 'p' :
        try : 
            ploblem_url = urls.get_nowait()
            browser.open(ploblem_url,2)
            print("sloved? y:n") 
            solved = input() 
            if solved  == 'y' : 
                unsolved.pop()
                update = unsolved
                update.reverse
                with open(filePath, mode = "w") as file : file.write('\n'.join(update))
        except queue.Empty : 
            print("queue is empty... Please push url!\n")

    if commnd == 'q' : 
        In_use = False
        unsolved.reverse()
        with open(filePath, mode = "w") as file : file.write('\n'.join(unsolved))

'''
TO DO
submitterの機能を取り込む
'''
