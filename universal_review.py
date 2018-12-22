import queue
import webbrowser

filePath = "review_urls.txt"
urls = queue.Queue()
browser = webbrowser.get()
unsolved = []
In_use = True

def init() : 
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
    unsolved.reverse()

def update() : 
    update = unsolved
    update.reverse
    with open(filePath, mode = "w") as file : file.write('\n'.join(update))

def Add_Problem() :
    print("Please input URL")
    new_ploblem = input()
    unsolved.append(new_ploblem)
    urls.put(new_ploblem)
    update()

def Pop_Problem() : 
    try : 
        ploblem_url = urls.get_nowait()
        browser.open(ploblem_url,2)
        print("sloved? y:n") 
        solved = input() 
        if solved  == 'y' : 
            unsolved.pop()
            update()
    except queue.Empty : 
        print("queue is empty... Please push url!\n")

def Quit() :
    global In_use
    In_use = False
    update()

def main() :  
    global In_use
    print("The numbor of problems in queue is " + str(urls.qsize()) + '\n')
    print("Mode Select" + "\n" + "push : i" + "\n" + "pop : p" + "\n" + "quit : q")
    commnd = input()
    if commnd == 'i' : Add_Problem()
    if commnd == 'p' : Pop_Problem()
    if commnd == 'q' : Quit()


if __name__ == "__main__" :
    init()
    while In_use : main()
'''
TO DO
submitterの機能を取り込む
'''
