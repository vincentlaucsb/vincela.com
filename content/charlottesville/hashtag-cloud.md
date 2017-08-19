Title: Building a Word Cloud in Python
Date: 2017-08-18
Modified: 2017-08-18 1809
Tags: python
Authors: Vincent La

## Building a Word Cloud
Any good statistical analysis begins with good exploratory data analysis. In addition to keying us in to things we may have never thought of, EDA can also be a valuable piece of the analysis itself. It's also a lot of fun!

Today I'm going to build a word cloud of hashtags that appear in the dataset, which will give us a good overview of what people are tweeting about.

## Prerequisites
The following Python packages are required:
* PIL (Python Imaging Library)
* numpy
* wordcloud

I'm going to use Python's built-in `csv` library to read the data, but there's a number of other appropriate libraries, such as `pandas`.


<pre><code class="python">
# Reading Data
import csv
import os
from io import BytesIO

# Word Cloud
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import wordcloud
</code></pre>

# A Blank Canvas
Here I create a blank canvas 1200 x 600 pixels big. By default, the image has a black background, but that can be changed. I'm also going to use the `RGB` (Red-Green-Blue) color system. If you're not familiar with this, it's just a way of defining different colors in terms of how much red, green, and blue light is required to produce those colors. A quick Google search will find you more information, including RGB values for common colors.

Reference: http://pillow.readthedocs.io/en/3.4.x/reference/Image.html#PIL.Image.new


<pre><code class="python">
width, height = (1200, 600)
background = Image.new('RGB', size=(width, height))
</code></pre>


<pre><code class="python">
background
</code></pre>




![png](output_4_0.png)



## Goal
My goal is to have "#charlottesville" in big bold letters in the center of the image, surrounded by other hashtags. <s>For simplicity, I'm going to use `Arial Bold` which is a font provided on all Windows installations.</s>

I'm going to use the beautiful fonts `Roboto` and `Roboto Slab` which can be downloaded for free from these links:

* https://fonts.google.com/specimen/Roboto
* https://fonts.google.com/specimen/Roboto+Slab?selection.family=Roboto


<pre><code class="python">
'''
Tell PIL where the font I want is located
 - Commented out code uses Arial Bold
'''

# Code for Arial Bold
# font_style = ImageFont.truetype(
#     os.path.join('C:', 'Windows', 'Fonts', 'arialbd.ttf'),
#     150)

font_style = ImageFont.truetype(os.path.join('fonts', 'Roboto-Bold.ttf'), 150)

# Text to be written
big_and_bold = "#charlottesville"
</code></pre>

Below, I use the `textsize` method of our canvas to calculate how wide and tall (in pixels) "#charlotteville" in 150 point Arial Bold will be. With some basic math, this also gives me the information needed to center it.


### Shoutout
Thank you to StackOverflow user `sastanin` for [providing an example of centering text with PIL](https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil).


<pre><code class="python">
# The Draw object gives us methods for manipulating our blank canvas
draw = ImageDraw.Draw(background)

# This method gives us the width and height of the text
text_width, text_height = draw.textsize(
    big_and_bold,
    
    # Make sure to pass in the font you are using,
    # or else the width and height using the DEFAULT FONT
    # will be calculated instead
    font=font_style)
</code></pre>


<pre><code class="python">
text_height
</code></pre>




    140




<pre><code class="python">
text_width
</code></pre>




    1048



The first argument here is a tuple describing the `(x, y)` position of where to draw the text.

Here's a quick geometry refresher. If you subtract the text width from the total image width, you get the amount of empty space left over. If you divide that quantity by two, then you get the amount of space (or "padding") required for both sides to have equal spacing. The same logic applies for height.

Lastly, `(255, 255, 255)` is the RGB designation for white.


<pre><code class="python">
draw.text(
    ((width - text_width)/2, (height - text_height)/2),
    big_and_bold,
    font=font_style,
    fill=(255, 255, 255))
</code></pre>


<pre><code class="python">
background
</code></pre>




![png](output_13_0.png)



# Read Tweets
Alright, now we have to filter out the hashtags. I'm going to use the `reader` and `DictReader` classes from the csv module. While `reader` spits out each row as a list, the `DictReader` spits out each row as an OrderedDict, making it easier to work with. However, the `DictReader` requires that you tell it what the column names are, which I'm too lazy to do. Because the first row of the CSV is a header row, we can use `reader` to parse it, and then feed it into `DictReader`.

Before working with the DictReader, I'm going to print out the ten rows of the CSV--as interpreted by DictReader--so I can see what I'm going to be working with.


<pre><code class="python">
# Use UTF-8 encoding so we can read special tweet characters
with open(os.path.join('csv', 'aug15_sample.csv'), 'r', encoding='utf-8') as tweets:
    # Read the header line
    header_reader = csv.reader(tweets)
    headers = next(header_reader)
    
    # Use DictReader for the rest
    reader = csv.DictReader(tweets, fieldnames=headers)
    for i, j in enumerate(reader):
        print(i, j)
        if i > 10:
            break
</code></pre>

    0 OrderedDict([('id', '897632879060144130'), ('user_id', '5385802'), ('user_name', 'FirniBeth'), ('screen_name', 'Firni'), ('user_statuses_count', '86340'), ('user_favorites_count', '57225'), ('friends_count', '3657'), ('followers_count', '2707'), ('user_location', 'Washington, USA'), ('user_description', 'Breast cancer survivor, mother, wife. Music lover. Metal4Lyfe \\\\m/ 18+ pls also no Trump posters,trolls or porn-spammers. Insta-block. #TheResistance'), ('user_time_zone', 'Pacific Time (US & Canada)'), ('user_profile_text_color', '000000'), ('user_profile_background_color', '000000'), ('full_text', "I'm white and I won't go anywhere near Alabama. https://t.co/onuzwbOsVb"), ('created_at', '2017-08-16 01:35:30'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', '"“Barack Obama is to blame”: 13 Alabama conservatives on Charlottesville - Vox https://t.co/ONjQ58ShEG https://t.co/Lzgb7BppXd"'), ('quoted_status_id', '897630433214595074'), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '')])
    1 OrderedDict([('id', '897660836579299328'), ('user_id', '880381231468343296'), ('user_name', 'Neisy Guerra'), ('screen_name', 'NeisyGuerra4'), ('user_statuses_count', '9487'), ('user_favorites_count', '9765'), ('friends_count', '1067'), ('followers_count', '341'), ('user_location', 'Miami Lakes, FL'), ('user_description', "History .Politics General. News US News .World News .science \\nProud democrat. Cats lover. Love books\\nWasn't born in US BUT love this country"), ('user_time_zone', 'null'), ('user_profile_text_color', '333333'), ('user_profile_background_color', 'F5F8FA'), ('full_text', "Another chief leaves Trump's manufacturing council\nhttps://t.co/NqZDz9WMkw"), ('created_at', '2017-08-16 03:26:35'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '')])
    2 OrderedDict([('id', '897636986357469184'), ('user_id', '804748553365102592'), ('user_name', 'Kraynyak'), ('screen_name', 'Kraynyak39'), ('user_statuses_count', '404'), ('user_favorites_count', '117'), ('friends_count', '260'), ('followers_count', '11'), ('user_location', 'Slovak Republic'), ('user_description', 'Emigrant Americkým občanom viazaná na New England záujemcov o amatérske i profesionálne hokej s občasnými úvah o ekonomike, politike a aktuálnom dianí.'), ('user_time_zone', 'null'), ('user_profile_text_color', '333333'), ('user_profile_background_color', 'F5F8FA'), ('full_text', "@SenWarren No he didn't #fauxcohontas! He condemned those who participated in the violence at #Charlottesville on both sides!"), ('created_at', '2017-08-16 01:51:49'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', '897564488475586560'), ('in_reply_to_user_id', '970207298'), ('hashtags', '"Charlottesville" "fauxcohontas"')])
    3 OrderedDict([('id', '897659001021845504'), ('user_id', '2185085300'), ('user_name', 'milenio 2052'), ('screen_name', 'Milenio2052'), ('user_statuses_count', '333552'), ('user_favorites_count', '140'), ('friends_count', '7532'), ('followers_count', '7359'), ('user_location', 'España'), ('user_description', 'Quizás algún día nos deremos cuenta  que perdimos la luna  por andar contando estrellas.'), ('user_time_zone', 'Madrid'), ('user_profile_text_color', '333333'), ('user_profile_background_color', 'C0DEED'), ('full_text', 'https://t.co/zA33WQp977 #News Histórico líder de KKK alaba a Trump por ‘decir la verdad’ de Charlottesville https://t.co/Y5fOI9FYLm'), ('created_at', '2017-08-16 03:19:18'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '"News"')])
    4 OrderedDict([('id', '897634959896260609'), ('user_id', '841162509419720704'), ('user_name', 'Price'), ('screen_name', 'price1000000'), ('user_statuses_count', '16532'), ('user_favorites_count', '11374'), ('friends_count', '521'), ('followers_count', '598'), ('user_location', 'United States'), ('user_description', "I'm only here to voice myself using the protection of my 1st amendment right (Bill of Rights/first 10 amendments) and trigger pansies with reality."), ('user_time_zone', 'null'), ('user_profile_text_color', '333333'), ('user_profile_background_color', 'F5F8FA'), ('full_text', '"@DavidEMcK59 @cathymdonker @southoflife75 @SusanDa50168535 @timkaine @realDonaldTrump Like first crime I noticed in this Charlottesville BS was kidnapping. Done by the opposition or so called left. you can\'t block people\'s...."'), ('created_at', '2017-08-16 01:43:46'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', '897634541682249728'), ('in_reply_to_user_id', '841162509419720704'), ('hashtags', '')])
    5 OrderedDict([('id', '897652746530291717'), ('user_id', '1024713882'), ('user_name', 'Citoφen Insφumis 🔻'), ('screen_name', 'clairvoyant_le'), ('user_statuses_count', '95001'), ('user_favorites_count', '64191'), ('friends_count', '4995'), ('followers_count', '4565'), ('user_location', 'Là-haut sur la montagneuuu'), ('user_description', 'Je ne suis rien, je le sais, mais je compose mon rien avec un petit morceau de tout. Victor Hugo. \\nINSOUMIS ET SANS CRAVATE. 🌿'), ('user_time_zone', 'null'), ('user_profile_text_color', '333333'), ('user_profile_background_color', 'C0DEED'), ('full_text', 'Depuis le drame de #Charlottesville, il me semble que le concept de #PointGodwin a volé en éclats.'), ('created_at', '2017-08-16 02:54:27'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '"PointGodwin" "Charlottesville"')])
    6 OrderedDict([('id', '897650937808003072'), ('user_id', '35211413'), ('user_name', 'Vince Young'), ('screen_name', 'Blackout20'), ('user_statuses_count', '5837'), ('user_favorites_count', '2858'), ('friends_count', '1303'), ('followers_count', '309'), ('user_location', 'Cheektowaga,NY'), ('user_description', 'Father,Bills season ticket holder section 127 and lifelong fan,crimson tide Fan ROLL TIDE!!! Buffalo PD retired. #billsmafia'), ('user_time_zone', 'Eastern Time (US & Canada)'), ('user_profile_text_color', '666666'), ('user_profile_background_color', '1A1B1F'), ('full_text', "I try to watch,I just can't stomach him. https://t.co/0z9VKCssNa"), ('created_at', '2017-08-16 02:47:15'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', '"Hannity is so ridiculous it\'s actually hard to turn away. You want to see how far it will dip into fantasy. #Trump #Charlottesville"'), ('quoted_status_id', '897649060072566784'), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '')])
    7 OrderedDict([('id', '897651929639211008'), ('user_id', '13045032'), ('user_name', 'RonEdens'), ('screen_name', 'RonEdens'), ('user_statuses_count', '4432'), ('user_favorites_count', '665'), ('friends_count', '998'), ('followers_count', '328'), ('user_location', 'Sacramento!'), ('user_description', 'Member of the Lame Stream media.'), ('user_time_zone', 'Pacific Time (US & Canada)'), ('user_profile_text_color', '333333'), ('user_profile_background_color', '709397'), ('full_text', 'Get....  out.... https://t.co/dSJqIzQMAV'), ('created_at', '2017-08-16 02:51:12'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', '"WATCH: White House chief of staff John Kelly reacts to President Trump\'s latest remarks on violence in Charlottesvi… https://t.co/Gd39HxBZVL"'), ('quoted_status_id', '897616420854317056'), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '')])
    8 OrderedDict([('id', '897634106288328704'), ('user_id', '1594271929'), ('user_name', 'baltazar  jr'), ('screen_name', 'baltazarjr3'), ('user_statuses_count', '4452'), ('user_favorites_count', '2183'), ('friends_count', '176'), ('followers_count', '258'), ('user_location', 'Valle de Coachella'), ('user_description', 'Education is a progressive discovery of our own ignorance'), ('user_time_zone', 'Arizona'), ('user_profile_text_color', '333333'), ('user_profile_background_color', '131516'), ('full_text', 'The folks that protested vs the nazis @ #Charlottesville are real patriots , neo Nazism has no chance here in America'), ('created_at', '2017-08-16 01:40:22'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '"Charlottesville"')])
    9 OrderedDict([('id', '897649332094107650'), ('user_id', '17612485'), ('user_name', 'T.J~'), ('screen_name', 'Td0GG066'), ('user_statuses_count', '8960'), ('user_favorites_count', '584'), ('friends_count', '1668'), ('followers_count', '394'), ('user_location', '32.459022,-85.022086'), ('user_description', 'Dare to be different come natural of me :-)'), ('user_time_zone', 'America/Chicago'), ('user_profile_text_color', '666666'), ('user_profile_background_color', '1A1B1F'), ('full_text', 'Charlottesville murder suspect failed basic training at Fort Benning in 2015 - https://t.co/rWRAnLA3us'), ('created_at', '2017-08-16 02:40:52'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '')])
    10 OrderedDict([('id', '897665101339254786'), ('user_id', '287469883'), ('user_name', 'The Right is Wrong'), ('screen_name', 'therightswrong'), ('user_statuses_count', '47417'), ('user_favorites_count', '27557'), ('friends_count', '2502'), ('followers_count', '4344'), ('user_location', 'null'), ('user_description', 'Clear-thinking. Progressive. Atheist. #RaiseTheWage #Resist ▶Racist, homophobic, Islamophobic pro-Trump trolls can hit the road & let the adults talk◀'), ('user_time_zone', 'null'), ('user_profile_text_color', '333333'), ('user_profile_background_color', 'C0DEED'), ('full_text', '"@ScottMGreer Here\'s a post from one of your @DailyCaller kameraden urging Right Wingers to drive cars into \'liberal protestors.\' #Charlottesville https://t.co/wcufG3vKQ1"'), ('created_at', '2017-08-16 03:43:32'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', '897649119312961537'), ('in_reply_to_user_id', '599817378'), ('hashtags', '')])
    11 OrderedDict([('id', '897663443670634496'), ('user_id', '17561562'), ('user_name', 'slone'), ('screen_name', 'slone'), ('user_statuses_count', '400126'), ('user_favorites_count', '711'), ('friends_count', '227'), ('followers_count', '57260'), ('user_location', '♡ Right where God wants me ♡'), ('user_description', 'Circumstances do not make the man, they reveal him.  James Allen ✡PRO-ISRAEL✡  #99/150 MIT TOP election influencers'), ('user_time_zone', 'Eastern Time (US & Canada)'), ('user_profile_text_color', '786A4A'), ('user_profile_background_color', '14ABD1'), ('full_text', 'DONALD DEFIANT: Blame on both sides https://t.co/opwHgY48La'), ('created_at', '2017-08-16 03:36:57'), ('is_retweet', 'f'), ('retweeted_status_text', ''), ('retweeted_status_id', ''), ('quoted_status_text', ''), ('quoted_status_id', ''), ('in_reply_to_status_id', ''), ('in_reply_to_user_id', ''), ('hashtags', '')])
    

## Filtering Out Tweets without Hashtags
Not every tweet has a hashtag, so we'll want to filter out rows in the `hashtags` column with empty entries.


<pre><code class="python">
with open(os.path.join('csv', 'aug15_sample.csv'), 'r', encoding='utf-8') as tweets:
    header_reader = csv.reader(tweets)
    headers = next(header_reader)
    
    reader = csv.DictReader(tweets, fieldnames=headers)
    for i, j in enumerate(reader):
        print(i, j['hashtags'])
        
        if i > 10:
            break
</code></pre>

    0 
    1 
    2 "Charlottesville" "fauxcohontas"
    3 "News"
    4 
    5 "PointGodwin" "Charlottesville"
    6 
    7 
    8 "Charlottesville"
    9 
    10 
    11 
    

The good news is that we can do this with a simple conditional statement.


<pre><code class="python">
with open(os.path.join('csv', 'aug15_sample.csv'), 'r', encoding='utf-8') as tweets:
    header_reader = csv.reader(tweets)
    headers = next(header_reader)
    
    reader = csv.DictReader(tweets, fieldnames=headers)
    for i, j in enumerate(reader):
        # Filter out tweets without hashtags
        # This is the prefered way to write: if len(j['hashtags']) == 0
        if j['hashtags']:
            print(i, j['hashtags'])
            
        if i > 10:
            break
</code></pre>

    2 "Charlottesville" "fauxcohontas"
    3 "News"
    5 "PointGodwin" "Charlottesville"
    8 "Charlottesville"
    

### Creating a Function
Based off the code above, I'm now going to modify it so it builds up a string of different hashtags which we can pass in to `wordcloud`. Furthermore, I'm going to write it as a function with takes in a file name, so I can easily join together different strings produced by different files.


<pre><code class="python">
# Build up a string
def hashtag_string(infile):
    hashtags = []
    
    with open(infile, 'r', encoding='utf-8') as tweets:
        header_reader = csv.reader(tweets)
        headers = next(header_reader)

        reader = csv.DictReader(tweets, fieldnames=headers)
        for i, j in enumerate(reader):
            if j['hashtags']:
                hashtags.append(j['hashtags'])
                
    # Combine everything in the list hashtags into a string, separated by spaces
    return ' '.join(hashtags)
</code></pre>

### Building the String: For Real
The string contains quotes, which is fine. The `worldcloud` package will strip them out for us.


<pre><code class="python">
hashtags = hashtag_string(os.path.join('csv', 'aug15_sample.csv')) + \
    hashtag_string(os.path.join('csv', 'aug16_sample.csv')) + \
    hashtag_string(os.path.join('csv', 'aug17_sample.csv'))

# Print first 200 characters for a quick manual check
print(hashtags[:200])
</code></pre>

    "Charlottesville" "fauxcohontas" "News" "PointGodwin" "Charlottesville" "Charlottesville" "JanBrewer" "Trump" "JamesAlexFields" "Charlottesville" "Virginia" "大学生" "学生" "自治体" "企業" "渡航禁止" "外務省" "Charlot
    

## Build Word Cloud
Original Inspiration: [Alice in Wonderland Wordcloud](https://amueller.github.io/word_cloud/auto_examples/masked.html)


We're going to use the image we made above as a "mask" for the word cloud. Basically, this means the `wordcloud` package is going to try to fill in the black areas of our script with words and avoid the rest. I'm not sure exactly how this feature works, but guessing from the output below, I believe what it does is convert every black and not-black pixel into a 1 or 0, and fills in everything with a 0.


<pre><code class="python">
cloud_mask = np.array(background)
cloud_mask
</code></pre>




    array([[[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ..., 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
    
           [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ..., 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
    
           [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ..., 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
    
           ..., 
           [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ..., 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
    
           [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ..., 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
    
           [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ..., 
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]], dtype=uint8)



### Adding Stopwords
Stopwords are basically non-interesting words we don't want to include in our wordcloud, such as conjunctions and pronouns. The wordcloud package already provides a good starter, but we're going to add "Charlottesville" to the list since we already plan to add it manually.


<pre><code class="python">
print(list(wordcloud.STOPWORDS)[:10])
</code></pre>

    ['out', 'herself', "they'll", 'most', "i'll", 'in', "didn't", "isn't", "mustn't", 'has']
    


<pre><code class="python">
stopwords = wordcloud.STOPWORDS
stopwords.add('Charlottesville')
</code></pre>


<pre><code class="python">
# If you want a nice looking font that's also provided by default for Windows, try
# 'font_path': os.path.join('C:', 'Windows', 'Fonts', 'GARA.TTF')
# for Garamond

tweet_storm = wordcloud.WordCloud(
        font_path=os.path.join('fonts', 'RobotoSlab-Regular.ttf'),
        max_font_size=80,
        width=width, height=height, max_words=500,
        mode='RGB',
        background_color=None,
        colormap="terrain",
        mask=cloud_mask)

tweet_storm.generate_from_text(hashtags)
</code></pre>




    <wordcloud.wordcloud.WordCloud at 0x6fa8970>



### Almost Done
As we can see, there's a nice cutout in the middle for us the add "#charlottesville".


<pre><code class="python">
cville_cloud = tweet_storm.to_image()
cville_cloud
</code></pre>




![png](output_31_0.png)



All we're going to do here is use the same code from above to re-insert "#charlottesville".


<pre><code class="python">
cville_draw = ImageDraw.Draw(cville_cloud)
cville_draw.text(
    ((width - text_width)/2, (height - text_height)/2),
    "#charlottesville",
    font=font_style,
    fill=(255, 255, 255))
</code></pre>


<pre><code class="python">
cville_cloud
</code></pre>




![png](output_34_0.png)



## Playing with Different Colors
As you may have noticed above, I used a "colormap" called "terrain". `wordcloud` uses [matplotlib colormaps](https://matplotlib.org/examples/color/colormaps_reference.html) to determine the color of every word.

Below, I encapsulated all the code above into a reusable function which takes an argument `wc_args`. This `wc_args` argument should be a dictionary of keywords arguments normally passed to the `WordCloud` constructor. The `**wc_args` syntax in Python basically means "parse this dictionary as keyword arguments." If you need more help understanding the `**wc_args` syntax, Google "python arbitrary arguments".


<pre><code class="python">
def make_cloud(wc_args):
    cloud_mask = np.array(background)
    
    stopwords = wordcloud.STOPWORDS
    stopwords.add('Charlottesville')
    
    tweet_storm = wordcloud.WordCloud(
            width=width, height=height,
            max_font_size=110,
            max_words=500,
            mode='RGB',
            background_color=None,
            mask=cloud_mask,
            **wc_args)

    tweet_storm.generate_from_text(hashtags)
    cville_cloud = tweet_storm.to_image()
    cville_draw = ImageDraw.Draw(cville_cloud)
    cville_draw.text(
        ((width - text_width)/2, (height - text_height)/2),
        "#charlottesville",
        font=font_style,
        fill=(255, 255, 255))

    return cville_cloud
</code></pre>

### nipy_spectral
This palette isn't listed on the link above, but when I tried to use `spectral`, I was warned to use this palette instead. Now, I can imagine this pallete working for other word clouds, but with the combination of a dark background and bright words makes this really hard on the eyes.


<pre><code class="python">
make_cloud(wc_args={
    'font_path': os.path.join('fonts', 'RobotoSlab-Regular.ttf'),
    'colormap': 'nipy_spectral'
})
</code></pre>




![png](output_38_0.png)



### Accent
This is visually appealing, but feels inappropriate given the subject matter. Honestly, I feel like this belongs in a magazine about home decorating or something.


<pre><code class="python">
make_cloud(wc_args={
    'font_path': os.path.join('fonts', 'RobotoSlab-Regular.ttf'),
    'colormap': 'Accent'
})
</code></pre>




![png](output_40_0.png)



### Viridis
This palette is easy on the eyes and visually appealing, but I think it also feels too "detached" from the seriousness of the matter.


<pre><code class="python">
make_cloud(wc_args={
    'font_path': os.path.join('fonts', 'RobotoSlab-Regular.ttf'),
    'colormap': 'viridis'
})
</code></pre>




![png](output_42_0.png)



## YlGnBu (Yellow, Green, Blue)
This is my personal favorite. I think it could go on the front page of the New York Times or Wall Street Journal (but that's just me).


<pre><code class="python">
make_cloud(wc_args={
    'font_path': os.path.join('fonts', 'RobotoSlab-Regular.ttf'),
    'colormap': 'YlGnBu'
})
</code></pre>




![png](output_44_0.png)



### Alternative Version with Garamond


<pre><code class="python">
make_cloud(wc_args={
    'font_path': os.path.join('C:', 'Windows', 'Fonts', 'GARA.TTF'),
    'colormap': 'YlGnBu'
})
</code></pre>




![png](output_46_0.png)


