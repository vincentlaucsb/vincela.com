from quiz.models import Category, FillInTheBlank, MultipleChoice
from django.utils.html import format_html

# Multi-replace
import re


# rep: Mapping of strings to replacement text
# string: String to be modified
def multi_replace(rep,string):
    #rep = {
    #    "[b]": "<strong>",
    #    "[/b]": "</strong>",
    #    "[samp]": "<pre style='color: white'><samp>",
    #    "[/samp]": "</samp></pre>",
    #    "[code]": "<code>",
    #    "[/code]": "</code>",
    #    "[pcode]": "<pre><code>",
    #    "[/pcode]": "</pre></code>",
    #    
    #}
    
    string = str(string)
    
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], string)
    
    return text

# Used for storing questions and answers associated with a single quiz page 
class QuizKey(dict):
    def __init__(self,url):
        super(QuizKey,self).__init__()
        
        self.url = url
        question_category = url.replace("-quiz","")
        
        # Pull questions from the Django DB and add them to the key #
        for question in FillInTheBlank.objects.filter(category__short_name=question_category):
            self[question.id_name] = FillBlankKey(question)
            
        for question in MultipleChoice.objects.filter(category__short_name=question_category):
            self[question.id_name] = MCKey(question)
            
    ''' Input: attempt should be a dictionary containing form data from a quiz page
        Output: Returns a QuizKey where all of the entries have their "html" key 
        modified to return an answer instead of a form
    '''
    
    # This is where it is determined if the user submitted a correct answer or not
    def score(self,attempt):
        scored = QuizKey(url=self.url)
        for qstn in self:
            # Only score questions that are actually on the page
            if qstn + "_answer" in attempt.keys():
                # user_answer only gets the answer so far for FillBlankKey
                user_answer = attempt[qstn + "_answer"]
                correct_answer = self[qstn]["answer"]
                #if user_answer != correct_answer:
                if verify(user_answer,correct_answer):
                    scored[qstn]["html"] = scored[qstn].html_score(correct=True,attempt=user_answer)
                else:
                    scored[qstn]["html"] = scored[qstn].html_score(attempt=user_answer)
        return scored
        
# Returns True or False if the user's answer was correct or not
# Will attempt to mark reasonable answers that are not exact matches as correct
def verify(user_answer,correct_answer):
    ''' Default rules:
        1. Spaces don't matter
        2. ' and " should be equivalent
        
        Known issue: fruits["apple"] = fruits['apple'] = fruits['apple"]
                     Last case is the problem
    '''
    replace = {
            " ":"", # Strip out white-space
            "'":'"'
            }
            
    if user_answer == correct_answer: return True
    elif multi_replace(replace,user_answer) == multi_replace(replace,correct_answer): return True
    else: return False

# Base class for FillInTheBlank, etc.
class QuestionKey(dict):
    # question should be a some sort of object from a Django DB query
    def __init__(self,question):
        super(QuestionKey,self).__init__()
        
        #self["question"] = question.question
        #self["answer"] = question.answer
        #self["id_name"] = question.id_name
        #self["html"] = self.html_question()
    
        fields = question.__dict__
        for item in fields:
            self[item] = fields[item]
    
    ''' Return the HTML code for the question
        answers:    Should be HTML code used for generating the answer choice section
    '''
    def html_question(self,answers):
        id_name = self["id_name"]   
        
        # Get rid of problem characters in question
        q_text = self["question"]
        
        problems = {
                    "{":"&#123;",
                    "}":"&#125;",
                    ">":"&gt;",
                    "<":"&lt;"
                   }
        html = multi_replace(problems,q_text)
        
        # Answer field
        html += answers
        
        # Custom formatting
        html = html.replace("[p]","<p>").replace("[/p]","</p>")
        html = html.replace("[c]","<code>").replace("[/c]","</code>")
        html = html.replace("[ul]","<ul>").replace("[/ul]","</ul>")
        html = html.replace("[li]","<li>").replace("[/li]","</li>")
        html = html.replace("[code]","<pre><code>").replace("[/code]","</code></pre>")
        html = html.replace("[samp]","<pre><samp>").replace("[/samp]","</samp></pre>")
        
        # Add a CSS-powered counter to each question
        html = html.replace("<p>","<p class='counter'> ",1)
        
        return format_html(html)
        
    ''' Return the HTML code for the question on the score page, telling the user if their answer 
        was correct or not 
        
        By default, correct_answer will be the "answer" field provided in the database
        Questions such as the MultipleChoice type may want to override this
    '''
    def html_score(self,attempt,correct_answer="",correct=False):
        if not correct_answer: correct_answer = self["answer"]
        answer_html = "<p>Your Answer: " + attempt + "</p>"
        
        if correct:
            answer_html += "<p>Correct!</p>"
        else:
            answer_html += "<p>Correct Answer: " + correct_answer + "</p>"
            
        # Provide an explanation if it exists:
        if self["explanation"]:
            answer_html += "<p>Explanation: " + format_html(self["explanation"]) + "</p>"
        
        return QuestionKey.html_question(self,answers=answer_html)
        
class FillBlankKey(QuestionKey):
    def __init__(self,question):
        super(FillBlankKey,self).__init__(question)
        self["html"] = self.html_question()
    
    ''' Generate HTML code for one question
        <p>{{ list_index_1.question }}</p>
        <label for="list_index_1">Answer:</label>
        <input type="text" id="list_index_1" name="list_index_1_answer" />
    '''
    def html_question(self,answers=""):
        id_name = self["id_name"]
    
        answer_html = "<label for='{0}'>Answer: </label>".format(id_name)
        answer_html += "<input type='text' id='{0}' name='{0}_answer' />".format(id_name)
        return super(FillBlankKey,self).html_question(answers=answer_html)
        
        
class MCKey(QuestionKey):
    def __init__(self,question):
        super(MCKey,self).__init__(question)
        
        # self['choices'] should be a string of answer choices separated by '----'
        temp = self["choices"]
        self["choices"] = []
        for item in temp.split('----'):
            self["choices"].append(item)
            
        self["html"] = self.html_question()
        
    ''' Generate HTML code for one question
        <p>{{ list_index_1.question }}</p>
        <label for="list_index_1">Answer:</label>
        <input type="text" id="list_index_1" name="list_index_1_answer" />
    '''
    def html_question(self,answers=""):
        id_name = self["id_name"]
    
        answer_html = ""
    
        '''
            self['choices'] should be a list of answer choices separated by '----'
            value should be a counter referring to the answer's position on the list
        '''
        assert(type(self["choices"]) == list)
        i = 0
        for item in self["choices"]:
            answer_html += "<input type='radio' id='{0}_choice_{2}' name='{0}_answer' value='{2}'><label class='radio' for='{0}_choice_{2}'>{1}</label><br />".format(id_name,item,i)
            i += 1
    
        return super(MCKey,self).html_question(answers=answer_html)
    def html_score(self,*args,**kwargs):
        # Replace index numbers with the text strings they are referring to
        kwargs['attempt'] = self["choices"][int(kwargs['attempt'])]
        i = self["answer"]
        correct_answer = self["choices"][i]
        return super(MCKey,self).html_score(*args,correct_answer=correct_answer,**kwargs)