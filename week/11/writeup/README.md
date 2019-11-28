# Writeup 1 - Web I

Name: Cooper Willetts
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Cooper Willetts


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)
Input - http://142.93.136.81:5000/item?id=0%27+||+%271=1%27+--+- 
Flag - CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

Used the lecture slides to use an SQL attack, had to bypass the 'OR' due to website throwing errors. A couple tries of different methods lead to the result of using '||' and having the extra semi-colon with the comment on the end. 

### Part 2 (60 Pts)
Level 1 
Answer - <script>alert("xss")</script>
Just inputting some script into the text box, no sanitizing was done

Level 2 
Answer - <img src='testing' onerror='alert("xss")'>

Needed some wat for the alert to constantly render at each load of the page, like an image. Then just added an error message for the image to display what we needed.

Level 3 - 
Answer - https://xss-game.appspot.com/level3/frame#1' onerror='alert("xss")

after playing around I noticed there was an error if I entered certain input, thus I tried many methods to implement an error and putting it in the url worked

Level 4 - 
Answer - ');alert('xss 

Needed to add alittle extra work on the input string, it already added the paren and semi, so we just needed to add onto an empty string with our alert box for it to work. 

Level 5 - 
Answer - https://xss-game.appspot.com/level5/frame/signup?next=javascript%3Aalert%28%27xss%27%29 

Through testing was able to track down that input into the url would transfer into JS code if we had proper input, so we just had to input our needed script into the url

Level 6 -
Answer - https://xss-game.appspot.com/level6/frame#data:text/plain,alert('xss')

Not much to do here other than play with the URL, so after seeing that the text I inputted would appear on the screen, I decided to write a script and it worked properly. 

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
