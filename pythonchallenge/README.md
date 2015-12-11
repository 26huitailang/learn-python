###一个古老的编程游戏：Python Challenge全通攻略
[pythonchallenge](http://www.pythonchallenge.com/)

[the anw hints](http://www.cnblogs.com/jimnox/archive/2009/12/08/tips-to-python-challenge.html)

Python Challenge是一个网页闯关游戏，通过一些提示找出下一关的网页地址。与众不同的是，它是专门为程序员设计的，因为大多数关卡都要编程来算哦！！

去年和同学一起玩的，他做了大半，我做了小半，作弊了一些，33关全通，今天逛硬盘发现这个资料，拿出来晃晃。

非常非常非常非常好玩，强烈推荐编程的朋友都玩玩，不一定要会Python，我和我同学都不会，不过我们用C#一样能搞出来，没有障碍的。

##0

http://www.pythonchallenge.com/pc/def/0.html

猜238，说是38在2上面一点点，猜238= 274877906944，进入下一关

	pow(2,38)
##1

http://www.pythonchallenge.com/pc/def/274877906944.html

http://www.pythonchallenge.com/pc/def/map.html

根据图上的提示，是位移加密，每个字符位移两次，把下面那些提示用这个方法的处理，告诉我用同样的方法处理url，得到ocr


##2

http://www.pythonchallenge.com/pc/def/ocr.html

提示看源文件，一大堆字符，说要找到出现次数最少的字符，发现是equality

	dict.get(c,0)+1
##3

http://www.pythonchallenge.com/pc/def/equality.html

一个小写字母，每边刚好有三个大写字母做保镖。

XXX

XxX

XXX

 

   X

   X

XXXxXXX

   X

   X

 

xXXXxXXXx 这个才是对的……

找到的答案是linkedlist
	
	正则表达
##4

http://www.pythonchallenge.com/pc/def/linkedlist.html

http://www.pythonchallenge.com/pc/def/linkedlist.php

点击网页上的图片之后，进入连接

http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

提示and the next nothing is 92512

然后就把12345改成92512，他又提示and the next nothing is 64505……

就这么一路下去，照着提示，几百次之后就行了……
##5

http://www.pythonchallenge.com/pc/def/peak.html

peak hell说要读出来，pickle

下载banner.p

然后就又不会了……
##6

http://www.pythonchallenge.com/pc/def/channel.html

从图片看出，拉链(zip)是主角……

下载channel.zip

然后和第4关差不多，做个程序一路走下去。

然后据说有注释，但是我找不到……

	hockey
	it's in the air. look at the letters. 
	hockey由oxygen组成
##7

http://www.pythonchallenge.com/pc/def/oxygen.html

图片上的那条灰度按照ASCII解码出来后是integrity

##8

http://www.pythonchallenge.com/pc/def/integrity.html

标题：working hard?

图片：一只蜜蜂

bee? busy. busy? busy too ? bz2?

下面的用户名和密码都是用bz2加密的，解密之后点图片的链接，然后进到下一关，输入用户名密码即可。
之后几关的用户名密码

huge

file
##9

http://www.pythonchallenge.com/pc/return/good.html

提示：connect the dots

后面代码里的first，second分别是两堆x和y的坐标，连起来以后first像一头牛，second像是一个十字，难道是横过来的X，叫做牛X……试了下cow，提示说是公的，bull。从这张图看出来，发现second原来只是描了下牛的头……
##10

http://www.pythonchallenge.com/pc/return/sequence.txt

a = [1, 11, 21, 1211, 111221,

len(a[30]) = ?

话说其实找到了个很诡异的规律，但是和官方的不一样。官方的规律是这样的：

1

1个1，写作11

2个1，写作21

1个2，1个1，写作1211

……

最后算一下就出来了5808
##11

http://www.pythonchallenge.com/pc/return/5808.html

图片一眼可以看出用了IE浏览器选中图片的那种效果，加上odd even的提示，更确信是这个了。一张图什么都没，另一张图一看以为什么都没，结果居然是显示器的问题……另一个显示气能很明显看出一种血红色的恐怖的图样，右上写着evil字样。
##12

http://www.pythonchallenge.com/pc/return/evil.html

一开始看着这么奇怪的图片，以为是图像处理的。看着图片叫evil1.jpg，感觉怪怪的，试了下evil2.jpg，还真有，提示说not jpg –gfx改成gfx真有这么个文件，不过不知道是什么东西。

evil3.jpg：no more evils…

evil4.jpg：Bert is evil! goback!

接下来就搞不懂怎么办了，看了提示才知道，原来原图那人把扑克牌分成5堆，提示着要把那个gfx文件用分牌的方式分成5个文件，结果图片的内容连起来就是下一关的网站了。
##13

http://www.pythonchallenge.com/pc/return/disproportional.html

按下数字键5之后会进入http://www.pythonchallenge.com/pc/phonebook.php

他说要打电话给一个evil的人，之前有提到Bert is evil，那就给他打电话吧……据说这个页面用了Remote Procedure Call (RPC)这种神奇的协议，反正照着一个例程改了下他就返回了555-ITALY
##14

http://www.pythonchallenge.com/pc/return/italy.html

根据网页标题的提示：walk around

网页代码的提示：100*100 = (100+99+99+98) + (...

还有那张螺旋状的面包图片，猜测，要把下面那张图（其实这个图是10000*1的，居然能显示成方的）以这种形式展开，结果出现一只猫。

在此之前有个小插曲，如果把那个图以一行行的形式展开会出现bit字样，然后进bit.html会提示说你走错路了……

然后输入cat.html，提示and its name is uzi. you'll hear from him later.
##15

http://www.pythonchallenge.com/pc/return/uzi.html

一张日历，1xx6年，根据星期和右下角显示的很小的二月份的29天，可以猜出是闰年，并且把答案缩小在：

这些年份中

1176

1356

1576

1756

1976

buy flowers for tomorrow，图上标了1.26，说明1.27有事发生

he ain't the youngest, he is the second

从上面这些年份中1976是最年轻的，第二年轻的是1756

2002年1月27日 尼日利亚首都拉各斯大爆炸2000人丧生

1999年1月27日 广西巨贪李乘龙一审被判处死刑

1998年1月27日 中国民乐除夕回荡维也纳（这是中国民族音乐历史上第一次在有“音乐圣殿”之称的金色大厅展现风采）

1997年1月27日 美科学家制造出原子激光

1982年1月27日 瓦尔德海姆获“联合国和平奖”

1973年1月27日 越美签定关于越南问题的巴黎协定

1964年1月27日 我国与法国建交

1950年1月27日 我国建立统一税收制度

1945年1月27日 苏军解放奥斯威辛集中营

1937年1月27日 美国遭受严重水灾，100万人无家可归

1926年1月27日 电视诞生

1901年1月27日 意大利作曲家威尔第逝世

1893年1月27日 宋庆龄诞辰

1822年1月27日 文明古国希腊独立

1756年1月27日奥地利音乐大师莫扎特诞生

1142年1月27日 岳飞被害

mozart
##16

http://www.pythonchallenge.com/pc/return/mozart.html

提示说把它弄直，图片里面杂乱无章的点很明显有很多是品红色的短线，把图按行平移，使得红线对齐，出现了romance字样。
##17

http://www.pythonchallenge.com/pc/return/romance.html

小牛做的，等他补解题报告

这个……我忘了，过程相当复杂，还是看国外的攻略吧。
##18

http://www.pythonchallenge.com/pc/return/balloons.html

提示说两张图片有什么不同，然后提示说区别比我们想的要简单，那就是亮度

http://www.pythonchallenge.com/pc/return/brightness.html

图片一样，源码里面提示下载deltas.gz

下载一看是个文本文件很明显分成了左右两块，写成了十六进制的形式，16个一行，然后按行求出了左右两边的最长公共子序列，并且左右分别减去这个LCS，得到三个png文件，一个写了http://www.pythonchallenge.com/pc/hex/bin.html

一个是butter

一个是fly

其中有一张图片需要用ps打开才行，浪费好多时间……
之后几关的用户名密码

butter

fly
##19

http://www.pythonchallenge.com/pc/hex/bin.html

一个电子邮件，下载后能弄出音乐，听到sorry。

图中显示的印度地图颜色是反的，联想到反转。

除了文件头之外的都前后字节交换，从新的音乐听到idiot，然后过去……

好神奇，居然正反都有能听的声音……
##20

http://www.pythonchallenge.com/pc/hex/idiot.html

http://www.pythonchallenge.com/pc/hex/idiot2.html

从图片的包头中看到range，然后编程构造请求的range，大概这样

 

var req =WebRequest.Create(@"http://www.pythonchallenge.com/pc/hex/unreal.jpg")as HttpWebRequest;

req.AddRange(r, r + len);

req.Credentials = newNetworkCredential("butter", "fly");

var rep = req.GetResponse();

using (var sr = rep.GetResponseStream())

{

   StreamWriter s = new StreamWriter("c:\\1.dat");

   byte[] a = new byte[10000000];

   int t;

   while ((t = sr.Read(a, 0, a.Length)) != 0)

    {

       // int t = sr.BaseStream.Read(a, 0, a.Length);

       s.BaseStream.Write(a, 0, t);

    }

   //Console.WriteLine("{0} {1}",r,sw.ReadToEnd());

   s.Close();

}

先是一大堆文字提示，说我入侵，然后尝试着把range的开始位置设置为2123456789，提示了密码是我的新昵称，还提示了结果所在的位置，然后在那个位置做完range的头，下载，发现一个压缩包，密码是redavni
##21

这关没实现，直接看网上的答案了。

大概的意思是，刚才下载到的那个压缩包里面有个package.pack文件，其实是个压缩文件，使用了zlib和bz2两种方式压缩，到时候还要适当地把文件逆序一下（关于这个的提示是他说这是个小时候的游戏，击鼓传花，国外的玩法不一样，需要一层层地拆传递的那个东西……）然后记录这三中东西的操作，一个记作“”，一个“#”，一个回车，就看到了用字符拼起来的copper字样。
##22

http://www.pythonchallenge.com/pc/hex/copper.html

提示：模拟，又提示white.gif会比想象中的亮度更大，发现这个gif是多帧的，差不多在图像的正中间有比黑色稍微亮一点的颜色……那些颜色出现在小键盘一样布局的3*3的9个位置上。然后一次当作方向向量描点处理，弄出来刚好是bonus这几个字母
##23

http://www.pythonchallenge.com/pc/hex/bonus.html

'va gur snpr bs jung?'

这个又是第1关中出现的位移加密……然后翻译过来就是in the face of what?

what is this module?

这个比较无语，在python里面输入 import this，显示了一大段：

The Zen of Python, by Tim Peters

 

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough tobreak the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse thetemptation to guess.

There should be one-- and preferably onlyone --obvious way to do it.

Although that way may not be obvious atfirst unless you're Dutch.

Now is better than never.

Although never is often better than *right*now.

If the implementation is hard to explain,it's a bad idea.

If the implementation is easy to explain,it may be a good idea.

Namespaces are one honking great idea --let's do more of those!

然后下一关就是ambiguity……
##24

http://www.pythonchallenge.com/pc/hex/ambiguity.html

bfs，从上到下，然后把路过的点的颜色（只看rgb中的r）全部间隔着写到一个文件中，发现是个zip，提示下一关lake
##25

http://www.pythonchallenge.com/pc/hex/lake.html

lake1.wav ~lake25.wav 按照图像拼起来
##26

http://www.pythonchallenge.com/pc/hex/decent.html

到19关那个地方写的邮件发道歉信过去

然后知道了之前21关那个压缩包里面的没用到的mybroken.zip的md5，还说错了一个字节，穷举一下，里面的图像里写着speed

下面提示要错过船了，speedboat
##27

http://www.pythonchallenge.com/pc/hex/speedboat.html

看了网上的提示才过的……

一开始当然先下载zigzag.gif

甚至研究了GIF的文件格式，发现文件结构很诡异，没用GIF的标准来压缩。

貌似他的tables一个是颜色表，一个是下面的图像

图像的灰度当作二进制输出，图像灰度的索引也输出，发现这两个几乎是一样的，但是差一个字节。

对齐之后，发现两个文件只有一点点不同，把不同之处提取出来，其中有一个可以看出是BZ2压缩的，解压之后是个文本，里面貌似都是下一关的网址和关键字。

网上找了一份python关键字，把文件中的关键字全删掉之后，得到了：

../ring/bell.html

switch

repeat

这3个字符串的序列，用户名repeat，密码switch
之后几关的用户名密码

repeat

switch
##28

http://www.pythonchallenge.com/pc/ring/bell.html

传说RING-RING-RING读着读着会变成green.

访问green.html会提示“yes! green!”

从图中也能看出很多绿色的竖条，提取绿通道之后发现那些竖条是成对的，偶数下标的和奇数下标的总是一个暗，一个亮。

网页标题也提示pairs，猜想两个一组。

组内求差之后发现差一般都是42或-42，只有180行头上有些不是，把那些的差值提前出来，是“whodunnit().split()[0] ?”

Python发明人Guido Van Rossum，结果就是guido
##29

http://www.pythonchallenge.com/pc/ring/guido.html

网页的源文件后面有大量的空格……

然后把每行的空格数写到一个文件里，又是BZh开头的，直接解压。

Isn't it clear? I am yankeedoodle!
##30

http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

把csv文件下载下来之后是一大堆浮点数，转成音频听不出东西。

里面一共有7367个浮点数，7367=139*53，用浮点数*256当灰度画成139宽53高的图像。显示出了一个方程。

n=str(x[i])[5]

+str(x[i+1])[5]

+str(x[i+2])[6]

然后浮点数当字符串，3个一组，使用公式计算n，转ASCII看，发现提示下一关是grandpa

28关猜名字的时候只猜了grandfather，差点猜到了……
##31

http://www.pythonchallenge.com/pc/ring/grandpa.html

先是要猜这块石头是什么地方的，找到是

Koh Samui

Thailand

然后用户名kohsamui，密码thailand，跳到下一个页面
之后几关的用户名密码

kohsamui

thailand

http://www.pythonchallenge.com/pc/rock/grandpa.html

不知道怎么猜到半径是2的，我是一点点试出来的。

画出自己的分形之后，和原图比较，发现新图和原图有些像素有不同。

不同的颜色的索引的差距都是16，有+16和-16。一共有1679处不同。

1679=23*73

于是根据差距的正负依次画出了这个图。

......*.*.*.*..........

..*.*.....*.*.......*..

*...*...*...*..*.**..*.

*.*.*.*.*.*.*.*..*..*..

.......................

............**.........

..........**.*.........

..........**.*.........

.........*.*.*.........

.........*****.........

.......................

**....***...**....**...

*.............**..*....

**.*...**...**....**.*.

*****.*****.*****.*****

.......................

...*.................*.

.......................

....*.................*

*****.............*****

.......................

**....**....***...**...

*.......*.........*....

**.*....**...***..**.*.

*****.*****.*****.*****

.......................

...*......**.........*.

..........**...........

....*.....**..........*

*****.....**......*****

..........**...........

..*........*........*..

...*......**.......*...

....**....**......*....

......**...*....**.....

..........**..**.......

......**...*....**.....

....**....**......*....

...*......*........*...

..*.......**........*..

.*........**........*..

.*.........*.......*...

..*.......*.......*....

...*............**.....

....**........**.......

..*...***.*.**.........

..*.......*............

..*.....*****..........

..*....*.***.*..*.**.**

......*..***..*..******

*.***....***.....**.***

.........*.*.....***.**

..*......*.*.....******

..*......*.*.....**....

..*.....**.**..........

.......................

..***.....*............

..***.*.*...*.*.*.*.*.*

..***.........*.*.*.*..

..............*.*......

........*****..........

......*********........

....***.......***......

...**...........**.....

..**.*.........*.**....

.**..**.......**..**...

.*...*.*.....*.*...*...

.*...*..*...*..*...*...

.....*...*.*...*.......

.....*....*....*.......

.....*.........*.......

.......*..*.*..........

.****..*****.*..****...

google找了好久……

Crop Circle

Chilbolton Radio Telescope

Wherwell, Hampshire, England

最后发现arecibo正是下一关的地址……
##32

http://www.pythonchallenge.com/pc/rock/arecibo.html

一个很神奇的游戏。每个行列的开头写着该行/该列有几个连续区段，分别多长。

给出这些表头的数字，要求这个图案。

先手算得到warmup的结果是一个向上的箭头，up.html里面有一个超大的要解……

弄出来一条蟒蛇python.html

页面上有提示

"Free" as in "Freespeech", not as in "free

Google到gnu上的信息： Tounderstand the concept, you should think of free as in free speech, not as infree beer.
##33

http://www.pythonchallenge.com/pc/rock/beer.html

代码中的图片为beer1，打开beer2.jpg，提示png

下载之后是个神奇的图片……

按照网页代码中那首诗的指导思想，要把图片中亮的点去掉，剩下的点数应该刚好是平方数，这样就能画在一张方的图里了。

测试发现图片中的颜色为1, 2, 7, 8, 13, 14都是成组出现的，这样就利用去掉比第一组亮的点，去掉比第二组亮的点……最后产生了33张图片。

其中均为字母，有些字母外面有框，连起来是 gremlins。

 

33关全结束了，很好很强大。

 

最后也分享个外国强人的解题报告，很华丽很完整，很好很强大。

http://garethrees.org/2007/05/07/python-challenge/