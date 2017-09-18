## The script of the game goes in this file.
# Declare images used by this game.
image bg wake_up = "background/wake_up.jpg"
image bg hallway = "background/hallway.jpg"

image snowman attack = "snowman/snowman_attack.jpg"

## Declare characters used by this game. The color argument colorizes the name
## of the character.

# Declare characters used by this game.
define Nater = Character('納特', color="#c8ffc8")
define Nacho = Character('納丘', color="#c8ffc8")
define Nacelin = Character('納希琳', color="#c8ffc8")
define Snowman = Character('雪叔', color="#c8ffc8")
define Angolen = Character('鞍哥隆', color="#c8ffc8")
define Kartman = Character('卡特曼', color="#c8ffc8")
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

    Nater "納希琳...還在睡啊？"

    Nater "今天做點什麼好呢？"

    scene bg hallway
    with fade

    Hurrie "「你能不能別去打擾他們夫婦？」"

    menu:
        "調戲":
            jump tease
        "反諷":
            jump irony

label tease:
    
    Nater "友好的調戲他一下好了"

    Nater "「嘿嘿，赫里你害羞了？」"

    Hurrie "「誰跟你害羞！」"

    Nater "這不是就是害羞嗎？生氣什麼？還推人咧！"

    jump hungry

label irony:
    
    Nater "反正他也是來巴結納丘的嘛，不安好心"

    Nater "「嘿嘿，赫里你也是啊，這麼早在外頭幹麻？」"

    "被戳破的赫里果然反應很激烈，臉全紅了，外加一臉驚恐"

    Hurrie "「誰跟你一樣了！別把我跟你混為一談！給我滾開~~」"

    Nater "哎喲，居然推人。"

    Nater "嘖嘖。被說中就生氣，跟外表一樣真沒度量"

label hungry:

    Nater "話說回來，肚子有點餓了呢.......去食堂看看吧......"
    
    ## This ends the game.

    return
