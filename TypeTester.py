import curses
from curses import wrapper
import time


def mainScreen(stdscr):
    stdscr.clear()
    stdscr.addstr("TYPING SPEED TEST \n PRESS ANY KEY TO TYPE \n ESCAPE TO EXIT...",curses.color_pair(3))
    stdscr.refresh()
    k=stdscr.getkey()
    if ord(k)==27:
        return False
    else:
        return True

def displayText(stdscr,sent,text,wpm=0):
    stdscr.clear()
    stdscr.addstr(sent)

    for i,char in enumerate(text):
        color=curses.color_pair(1)
        if not(char==sent[i]):
            color=curses.color_pair(2)
        stdscr.addstr(0,i,char,color)
        stdscr.addstr(1,4,f"WPM : {wpm}")
    stdscr.refresh()


def load_text():
    return "All the other kids wth the pumped up kicks, You better run better run Outrun my gun.."


def check_wpm(stdscr,sent,text):
    RUN_2=True
    start_time=time.time()
    wpm_list=[]
    stdscr.nodelay(True)
    while RUN_2:

        elapsed_time=max(1,time.time()-start_time)
        wpm=round(len(text)*(60/elapsed_time)/5)
        wpm_list.append(wpm)
        try:
            key=stdscr.getkey()
        except:
            displayText(stdscr,sent,text,wpm)
            continue
        if ord(key)==27:
            RUN_2=False
        if len(text)<=len(sent) :
            if key in ("KEY_BACKSPACE","\b","\x7f") and len(text)>0:
                text.pop()
            else:
                if not(len(text)>=len(sent)):
                    text.append(key)

            displayText(stdscr,sent,text,wpm)

        if sent=="".join(text):
            stdscr.nodelay(False)
            print("yes")
            stdscr.clear()
            avg=round(sum(wpm_list)/len(wpm_list))
            stdscr.addstr("Sentence completed! Press any key to continue",curses.color_pair(4))
            stdscr.addstr(1,0,f"AVG WPM: {avg}",curses.color_pair(5))
            wpm_list=[]
            RUN_2=False            
            ch=stdscr.getch()
            stdscr.refresh()



def main(stdscr):

    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_WHITE)
    curses.init_pair(4,curses.COLOR_MAGENTA,curses.COLOR_WHITE)
    curses.init_pair(5,curses.COLOR_WHITE,curses.COLOR_RED)

    RUN_1=True

    while RUN_1:
        stdscr.nodelay(False)
        if not(mainScreen(stdscr)):
            RUN_1=False
            continue

        SENT=load_text()
        my_text=[]
        check_wpm(stdscr,SENT,my_text)


wrapper(main)
