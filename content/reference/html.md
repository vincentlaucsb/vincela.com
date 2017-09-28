Title: HTML Reference Sheet
Date: 2017-08-19
Tags: html
Authors: Vincent La
Slug: html
Template: html
Summary: A quick guide to the building blocks of HTML
sortorder: 1

<!--
  _______  _______  _            _______  _______  _             
(  ____ \(  ___  )( \           (  ____ )(  ___  )( \   |\     /|
| (    \/| (   ) || (           | (    )|| (   ) || (   ( \   / )
| |      | (___) || |           | (____)|| |   | || |    \ (_) / 
| |      |  ___  || |           |  _____)| |   | || |     \   /  
| |      | (   ) || |           | (      | |   | || |      ) (   
| (____/\| )   ( || (____/\     | )      | (___) || (____/\| |   
(_______/|/     \|(_______/     |/       (_______)(_______/\_/   
                                                              
 _______           _______  _        _______                  
(  ____ \|\     /|(  ____ \| \    /\(  ____ \                 
| (    \/| )   ( || (    \/|  \  / /| (    \/                 
| (_____ | |   | || |      |  (_/ / | (_____                  
(_____  )| |   | || |      |   _ (  (_____  )                 
      ) || |   | || |      |  ( \ \       ) |                 
/\____) || (___) || (____/\|  /  \ \/\____) |                 
\_______)(_______)(_______/|_/    \/\_______)                 
                                                              
                                                              
For more information, see: http://www.calpoly.edu/
Thank you to http://patorjk.com for allowing me to place this inspirational message.                                                              
 -->

<h2>Table of Contents</h3>
<nav id="toc">
    <a href="#basics">Basics</a>
    <a href="#text-struct">Text Structure</a>
    <a href="#list">Lists</a>
    <a href="#font">Fonts</a>
    <a href="#text-style">Text Styling</a>
    <a href="#link">Links and Anchors</a>
    <a href="#special-char">Special Characters</a>
    <a href="#table">Tables</a>
    <a href="#code">Code Examples</a>
    <a href="#image">Images</a>
</nav>


<section id="basics">    
<h2>Basics of HTML and CSS</h2>
<h3>A Bare-Minimum HTML Document</h3>
<p>If you <em>would</em> like more information, feel free to read <a href="https://www.sitepoint.com/a-minimal-html-document-html5-edition/">this SitePoint</a> article
about what consitutes a minimal webpage under the HTML 5 standard.</p>

<p>The above HTML code is the suggested bare minimum for a page (you might want to keep it around as a template).
As you might have noticed, it doesn't do anything (except change the page title)!
We'll fix that in the next few pages.</p>

<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;

&lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;title&gt;A Webpage&lt;/title&gt;
&lt;/head&gt;

&lt;body&gt;
    &lt;!-- Content goes here --&gt;
&lt;/body&gt;

&lt;/html&gt;</code></pre>

<h3>Comments</h3>
<p>Comments are inert blocks of text that can be used as notes for yourself, 
or as a nice surprise to people who want to view your source code.</p>

<h5>Examples</h5>
<pre><code>&lt;!-- I am a comment! I don't actually do anything. --&gt;</code></pre>

<p>This example was found on <a href="http://infolab.stanford.edu/~sergey/resume.html">Sergey Brin's resume</a>:
<pre><code>&lt;!--&lt;h5&gt;Objective:&lt;/h5&gt;
A large office, good pay, and very little work.
Frequent expense-account trips to exotic lands would be a plus.--&gt;</code></pre>
</section>


<section id="text-struct">
<h2>Text Structure</h2>
<h3>Basic Structure</h3>
<p>Per web standards, HTML text should be "contained" in more than just <code>&lt;body&gt;&lt;/body&gt;</code>
tags. There is always some tag (or tags) text can be enclosed in depending on what purpose it serves.</p>

<h4>Headers</h4>
<p data-height="370" data-theme-id="light" data-slug-hash="VpLjZM" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Headings" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/VpLjZM/">Headings</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

<h4>Paragraphs</h4>
<p>You should wrap paragraphs with <code>&lt;p&gt;&lt;/p&gt;</code> tags.
Text wrapped in these tags, by default, also come with margins to space away them 
from other elements.</p>
</section>

<h3>More Advanced Options</h3>
<p>Reference: <a href="https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Advanced_text_formatting">Advanced text formatting</a> from the Mozilla Developer Network</p>

<h4>Abbreviations</h4>
<p>When including abbreviations in your web pages, especially obscure ones or jargon, the <code>&lt;abbr&gt;</code> tag allows you to provide an expansion of these acronyms.</p>
<p data-height="265" data-theme-id="light" data-slug-hash="WpvxXe" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Abbreviations and Definition Lists" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/WpvxXe/">Abbreviations and Definition Lists</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

<h4>Description Lists</h4>
<p>A description list is useful for presenting a list of terms and their definitions.</p>
<p data-height="265" data-theme-id="light" data-slug-hash="wJaWPL" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Description Lists" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/wJaWPL/">Description Lists</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

<h4>Quotes</h4>
<p>When including quotes, the <code>&lt;blockquote&gt;</code> tag marks a large
 chunk of text as part of a quote. On the other hand, the <code>&lt;q&gt;</code> tag
 is used for smaller quotes. Finally, to reference the source of a quote, the <code>&lt;cite&gt;
 </code> tag is used.</p>
<p data-height="394" data-theme-id="light" data-slug-hash="dvoXWd" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="HTML Quotes" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/dvoXWd/">HTML Quotes</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

<section id="list">
<h2>Lists</h2>
<p>By default, most browsers will rendered unordered lists with bullets,
and ordered lists with numbers.</p>
<p data-height="538" data-theme-id="light" data-slug-hash="EWjyxg" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Lists" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/EWjyxg/">Lists</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>
</section>

<section id="text-style">
<h2>Text Styling</h2>
<h3>Basic Styling</h3>
<h4>Bold, Italic, and Underline</h4>
<p data-height="509" data-theme-id="light" data-slug-hash="LWVZxO" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Basic Text Styling" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/LWVZxO/">Basic Text Styling</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

<h4>Coloring</h4>
<p>We can color our text in every shade of the rainbow using CSS.</p>
<p data-height="333" data-theme-id="light" data-slug-hash="GWJZax" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Basic HTML Coloring" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/GWJZax/">Basic HTML Coloring</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

<h4>Backgrounds and Shadows</h4>
<p data-height="265" data-theme-id="light" data-slug-hash="oZXxJZ" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Backgrounds and Shadows" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/oZXxJZ/">Backgrounds and Shadows</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>
</section>



<section id="font">
<h2>Fonts</h2>
<p data-height="265" data-theme-id="light" data-slug-hash="ZeGObb" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Fonts" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/ZeGObb/">Fonts</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>
</section>



<section id="link">
<h2>Links and Anchors</h2>
<p>Links should be created using the HTML anchor tag.</p>
<pre><code>&lt;h4&gt;Basic Links&lt;/h4&gt;
&lt;ul&gt;
    &lt;li&gt;&lt;a href="http://www.google.com"&gt;Google&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="mailto:inbox@prefered-email-service.com"&gt;Email&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;

&lt;h4&gt;Relative Links&lt;/h4&gt;
&lt;ul&gt;
    &lt;li&gt;&lt;a href="/"&gt;Go back to the root directory&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="../"&gt;Go up a directory&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;

&lt;h4&gt;Open in a New Tab&lt;/h4&gt;
&lt;p&gt;
    &lt;a
    href="http://www.google.com" target="_blank"
    rel="noopener noreferrer"&gt;
    Google (again)
    &lt;/a&gt;
&lt;/p&gt;

&lt;h4&gt;Some Cool Tricks&lt;/h4&gt;
&lt;ul&gt;
    &lt;li&gt;&lt;a href="#top"&gt;Go to top of page&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
</code></pre>

<h4>Basic Links</h4>
<ul>
    <li><a href="http://www.google.com">Google</a></li>
    <li><a href="mailto:inbox@prefered-email-service.com">Email</a></li>
</ul>

<h4>Relative Links</h4>
<ul>
    <li><a href="/">Go back to the root directory</a></li>
    <li><a href="../">Go up a directory</a></li>
</ul>

<h4>Open in a New Tab</h4>
<p>
    <a
    href="http://www.google.com" target="_blank"
    rel="noopener noreferrer">
    Google (again)
    </a>
</p>

<h4>Some Cool Tricks</h4>
<ul>
    <li><a href="#top">Go to top of page</a></li>
</ul>
</section>

<h3>Navbars</h3>
<p>Navigation bars are sets of links which are used as a primary way of moving about your website. Not every &lt;a&gt; tag should be encapsulated in a navbar, nor should every group of links. However, if a group of links contains the main destinations of your website, you should consider wrapping them with &lt;nav&gt; tags. Navigation bars are commonly styled with CSS&mdash;as shown below.</p>

<h4>An Advanced Example</h4>
<p data-height="265" data-theme-id="light" data-slug-hash="ZeGWaN" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Multi-Colored Flexible Navbar Example" class="codepen">See the Pen <a href="https://codepen.io/vincela9/pen/ZeGWaN/">Multi-Colored Flexible Navbar Example</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>


<section id="special-char">
<h2>Special Characters&#8482;&reg;</h2>
<p>Special characters can be inserted into HTML simply by typing a special code.
HTML special character codes typically begin with an amperstand and end with a semi-colon.</p>
<p>For more special characters, see: <a href="http://htmlarrows.com/">http://htmlarrows.com/.</a>
        

</section>




<section id="table">
<h2>Tables</h2>
<h3>A Basic Example</h3>
<ul>
    <li>thead (optional): Designate a row as the table's header</li>
    <li>tr: Table row</li>
    <li>td: Table cell/table data</li>

    </ul>
</section>
<p data-height="265" data-theme-id="light" data-slug-hash="Mpweea" data-default-tab="html,result" data-user="vincela9" data-embed-version="2" data-pen-title="Tables" class="codepen">See the Pen <a href="http://codepen.io/vincela9/pen/Mpweea/">Tables</a> by vincela9 (<a href="http://codepen.io/vincela9">@vincela9</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

<!--
<section id="code">
<h2>Code Examples</h2>
{#% eval_code filename="code.html" %#}
</section>
-->