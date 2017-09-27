## The script of the game goes in this file.
# Declare images used by this game.
image bg wake_up = "background/wake_up.jpg"
image bg hallway = "background/hallway.jpg"

image snowman attack = "雪叔/snowman_attack.jpg"

## Declare characters used by this game. The color argument colorizes the name
## of the character.

# Declare characters used by this game.
define Nater = Character('納特', color="#c8ffc8")
define Nacho = Character('納丘', color="#c8ffc8")
define Nacelin = Character('納希琳', color="#c8ffc8")
define Snowman = Character('雪叔', color="#c8ffc8")
define Angolen = Character('鞍哥隆', color="#c8ffc8")
define Kartman = Character('卡特曼', color="#c8ffc8")
define Zelo = Character('傑諾', color="#c8ffc8")
define Hurrie = Character('赫里', color="#c8ffc8")

## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg wake_up

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    # show snowman attack

    ## These display lines of dialogue.

    "哈囉冠之狗血的故事要開始了！主角的一天"

    Nater "......"

    show screen profile(Hurrie)

    Nater "納希琳...還在睡啊？"

    Nater "今天做點什麼好呢？"

    scene bg hallway
    with fade

    Hurrie "「你能不能別去打擾他們夫婦？」"

    menu:
        "調戲":
            jump Tease
        "反諷":
            jump Irony

label Tease:
    
    Nater "友好的調戲他一下好了"

    Nater "「嘿嘿，赫里你害羞了？"

    Hurrie "「誰跟你害羞！」"

    Nater "這不是就是害羞嗎？生氣什麼？還推人咧！"

    jump Hungry

label Irony:
    
    Nater "反正他也是來巴結納丘的嘛，不安好心"

    Nater "「嘿嘿，赫里你也是啊，這麼早在外頭幹麻？」"

    "被戳破的赫里果然反應很激烈，臉全紅了，外加一臉驚恐"

    Hurrie "「誰跟你一樣了！別把我跟你混為一談！給我滾開~~」"

    Nater "哎喲，居然推人。"

    Nater "嘖嘖。被說中就生氣，跟外表一樣真沒度量"

label Hungry:

    Nater "話說回來，肚子有點餓了呢.......去食堂看看吧......"

    "食堂一片吵鬧聲"

    Nater "又來了。"

    Nater "唉，大概又是再吵著午餐要吃啥了吧？"

    Nater "要接任務啦！"

    menu:
        "唉，沒辦法，我不去的話他們會餓死的":
            jump OpenTheDoor
        "反正也只有餓一天，死不了的。":
            jump NotOpenTheDoor

label OpenTheDoor:

    狗黨們 "「納特啊！等你好久啦！我們快餓死啦！"

    Nater "「欸～又是這樣了～桌上有食物不會先吃啊～」"

    狗黨們 "「這不能吃啊！」"

    "黑暗世界清淡無比的食物"

    狗黨1 "「比薩～！欸不要好了，牛排？」"

    狗黨2 "「欸，我要吃上次那個熱炒。」"

    Nater "「是不會統一一家喔，要跑很遠欸！」"

    狗黨1 "「欸吃牛排啦！現代人沒人在吃熱炒了啦！」"

    狗黨2 "「拜託啦！反正你一次可以帶兩個人出去，總共可以去三家不同的店吧！對吧對吧？」"

    Nater "「白癡！去了外面，我也不能離開他們啊！還不是得一家一家去，所以比薩、牛排、熱炒已經三家了喔！下好離手。」"

    狗黨3 "「欸，我要吃湯麵的，哪有人一次點兩樣！」"

    Nater "「好、好～你們去旁邊打架，寫完菜單給我。」"

    Nater "好了，那麼多人都要吃，現在該找誰陪我去提便當呢～？"

    Nater "只能帶兩個外地人出門幫忙，但要提10幾個便當，找誰好呢？"

    menu:
        "邀請傑諾":
            jump InviteZelo
        "邀請卡特曼":
            jump InviteKartman
        "邀請鞍哥隆":
            jump InviteAngolen
        "邀請納丘":
            jump InviteNacho

label InviteAngolen:

    "鞍哥隆.....這渾身都是肌肉的傢伙，靠你了。"

    "反正你電影也快看完了吧，正好出去一下不是正好嗎？"


label NotOpenTheDoor:


    ## This ends the game.

    return
