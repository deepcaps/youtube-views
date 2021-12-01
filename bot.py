#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = "deepcaps"
__contact__ = "deepcaps@outlook.com"
__version__ = "1.0"
__copyright__ = "deepcaps"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from colorama import init, Fore, Back, Style
import threading
from pystyle import Colorate, Colors, Center, Box
from time import sleep, monotonic
import os
import platform


def main():
    '''
    User graphic interface.
    Make speedtest, set variable and call threadInit
    return: True/False
    '''
    # main menu
    graphicTitle()
    text = Center.XCenter("|    press [ENTER] to start  |")
    print(Colorate.Horizontal(Colors.yellow_to_red, text))
    input()

    # ask for variables
    graphicTitle()   # title
    try:
        link = input(Colorate.Horizontal(Colors.yellow_to_red, "[>] youtube vidéo link : "))
        if link == "":   # check if is empty
            print(Fore.YELLOW +"system :" + Fore.RED + Style.BRIGHT + " ERROR !" + Style.NORMAL + " invalid answer" + Style.RESET_ALL)
            sleep(2)
            return False
        else:
            try:   # check if the answer is not a number
                int(link)
                print(Fore.YELLOW +"system :" + Fore.RED + Style.BRIGHT + " ERROR !" + Style.NORMAL + " invalid answer" + Style.RESET_ALL)
                sleep(2)
                return False
            except:
                pass
        print()
        watchTime = int(input(Colorate.Horizontal(Colors.yellow_to_red, "[>] watch time (in second ) (time bot stays on the video (for more referencing)) : ")))
        print()
        threadNbr = int(input(Colorate.Horizontal(Colors.yellow_to_red, "[>] thread nbr (sessions launched at the same time (use ram but is faster)) : ")))
        print()
        rep = int(input(Colorate.Horizontal(Colors.yellow_to_red, "[>] number of repetition (for more views) : ")))
    except:   # if answer is invalid
        print(Fore.YELLOW +"system :" + Fore.RED + Style.BRIGHT + " ERROR !" + Style.NORMAL + " invalid answer(s)" + Style.RESET_ALL)
        sleep(2)
        return False

    # speedtest
    graphicTitle()   # title
    print(Fore.YELLOW + "system :" + Style.RESET_ALL + " wait for internet speedtest ..." + Style.RESET_ALL)
    sleep(1)
    speed = speedTest()
    sleep(2)
    
    # calc time and views
    totalTime = rep * (watchTime + speed + 5)
    totalViews = rep * threadNbr

    # summary table
    graphicTitle()   # title
    table = """
time to access "www.youtube.com": """ + str(speed) + """ seconds
number of views: """ + str(totalViews) + """
estimated total time: """ + str(totalTime) + """ seconds
    """
    print(Center.XCenter(Box.DoubleCube(table)))
    print()

    # want continue ?
    choice = input(Colorate.Horizontal(Colors.yellow_to_red, "[>] do you want to continue ? (y/n): "))
    if choice == "y":
        graphicTitle()   # title
        threadInit(threadNbr, rep, watchTime, link)
        return True
    elif choice == "n":
        print(Fore.YELLOW + "system :" + Style.RESET_ALL + " closing program ..." + Style.RESET_ALL)
        sleep(2)
        return True
    else:   # if incorrect answer
        print(Fore.YELLOW +"system :" + Fore.RED + Style.BRIGHT + " ERROR !" + Style.NORMAL + " invalid answer" + Style.RESET_ALL)
        print(Fore.YELLOW + "system :" + Style.RESET_ALL + " closing program ..." + Style.RESET_ALL)
        sleep(2)
        return False

def graphicTitle():
    '''
    Graphic title.
    Clear console and print graphic title
    return: True
    '''
    title1 = """
$$\     $$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$\   $$\ $$$$$$$\  $$$$$$$$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |\__$$  __|$$ |  $$ |$$  __$$\ $$  _____|
 \$$\ $$  / $$ /  $$ |$$ |  $$ |   $$ |   $$ |  $$ |$$ |  $$ |$$ |      
  \$$$$  /  $$ |  $$ |$$ |  $$ |   $$ |   $$ |  $$ |$$$$$$$\ |$$$$$\    
   \$$  /   $$ |  $$ |$$ |  $$ |   $$ |   $$ |  $$ |$$  __$$\ $$  __|   
    $$ |    $$ |  $$ |$$ |  $$ |   $$ |   $$ |  $$ |$$ |  $$ |$$ |      
    $$ |     $$$$$$  |\$$$$$$  |   $$ |   \$$$$$$  |$$$$$$$  |$$$$$$$$\ 
    \__|     \______/  \______/    \__|    \______/ \_______/ \________|
"""                                                                    
    title2 = """
$$\    $$\ $$$$$$\ $$$$$$$$\ $$\      $$\  $$$$$$\ 
$$ |   $$ |\_$$  _|$$  _____|$$ | $\  $$ |$$  __$$\ 
$$ |   $$ |  $$ |  $$ |      $$ |$$$\ $$ |$$ /  \__|
\$$\  $$  |  $$ |  $$$$$\    $$ $$ $$\$$ |\$$$$$$\ 
 \$$\$$  /   $$ |  $$  __|   $$$$  _$$$$ | \____$$\ 
  \$$$  /    $$ |  $$ |      $$$  / \$$$ |$$\   $$ |
   \$  /   $$$$$$\ $$$$$$$$\ $$  /   \$$ |\$$$$$$  |
    \_/    \______|\________|\__/     \__| \______/
"""
    # clear console
    if platform.system() == "Windows":   # if os is windows
        os.system("cls")
    else:
        os.system("clear")

    # write title on console
    title1 = Center.XCenter(title1)
    print(Colorate.Horizontal(Colors.yellow_to_red, title1))
    title2 = Center.XCenter(title2)
    print(Colorate.Horizontal(Colors.yellow_to_red, title2))

    # space
    for i in range(3):
        print()
    return True

def speedTest():
    '''
    Internet connection speed test.
    Try to access to "www.youtube.com" and get to access
    return: result or 5
    '''
    try:
        # set options
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--log-level=3')

        # start chromedriver
        driver = webdriver.Chrome(chrome_options=options)

        # test link
        timerStart = monotonic()   # start timer
        driver.get("https://www.youtube.com/")   # get link of video
        timerStop = monotonic() # Stop timer
        
        speedTest = timerStop - timerStart   # calcul speedtest
        
        # rounded speedtest
        try:
            speedTest = str(speedTest)
            rounded = speedTest.index(".")
            speedTest = speedTest[:rounded]
        except:
            pass

        speedTest = int(speedTest)

        print(Fore.YELLOW + "speedtest :" + Style.RESET_ALL + " successfully get internet speed !" + Style.RESET_ALL)
        driver.close()
        return speedTest
    except:
        print(Fore.BLUE +"speedtest :" +Fore.RED + Style.BRIGHT + " ERROR !" + Style.NORMAL + " unable to get internet speed" + Style.RESET_ALL)
        driver.close()
        return 5

def threadInit(threadNbr, rep, watchTime, link):
    '''
    Initializing threads.
    Initializes threads and manage repetition
    return: True
    '''
    global threads
    for u in range(rep):   # "rep" repetition
        print(Fore.YELLOW + "system : start repetition", u+1, "/",rep , "" + Style.RESET_ALL)
        threads = []
        for i in range(threadNbr):   # "threadNbr" repetition
            t = threading.Thread(name="thread"+str(i), target=session, args=(link, watchTime, i+1, ))   # create thread
            threads.append(t)   # add thread in "threads"
            t.start()   # start thread
            print(Fore.YELLOW + "system :" + Style.RESET_ALL + " successfully started session", i+1, "!" + Style.RESET_ALL)

        while len(threads) != 0:   # wait to all thread are finished
            pass
        if u+1 == rep:   # if is the last "rep"
            print(Fore.YELLOW + "system : end of process" + Style.RESET_ALL)
            sleep(2)
            return True

def session(link, watchTime, threadNbr):
    '''
    Session start.
    Go to the video link, accept condition of utilisation and stay "watchTime" seconds
    return: True/False
    '''
    # set options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')

    # start chromedriver
    driver = webdriver.Chrome(chrome_options=options)
    print(Fore.BLUE +"session", threadNbr,":" +Fore.GREEN + " started successfully !" + Style.RESET_ALL)
    try:
        driver.get(link)   # get link of video
        print(Fore.BLUE +"session", threadNbr,":" + Fore.GREEN + " success to get link !" + Style.RESET_ALL)
    except:
        print(Fore.BLUE +"session", threadNbr,":" + Fore.RED + Style.BRIGHT + " ERROR !" + Style.NORMAL + " unable to get link" + Style.RESET_ALL)
        driver.close()
        del threads[threads.index(threading.current_thread())]   # delete thread
        return False

    # accept condition
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button").click()   # click on "accept condition" button
        sleep(1)
        print(Fore.BLUE +"session", threadNbr,":" +Fore.GREEN + " success to accept condition !" + Style.RESET_ALL)
    except:
        print(Fore.BLUE +"session", threadNbr,":" +Fore.RED + Style.BRIGHT + " ERROR !" + Style.NORMAL + ' unable to access the element: "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button" !' + Style.RESET_ALL)
        driver.close()
        del threads[threads.index(threading.current_thread())]   # delete thread
        return False

    # wait watchTime
    print(Fore.BLUE +"session", threadNbr,":" + Style.RESET_ALL + " start watchTime's timer (", watchTime, " seconds)")
    sleep(watchTime)   # sleep "watchTime"
    print(Fore.BLUE +"session", threadNbr,":" + Style.RESET_ALL + " end of watchTime's timer")
    print(Fore.YELLOW +"system :" + Style.RESET_ALL + " close session", threadNbr, "" + Style.RESET_ALL)

    # close session
    del threads[threads.index(threading.current_thread())]   # delete thread
    driver.close()   # close chromedriver session
    return True


if __name__ == "__main__":
    main()