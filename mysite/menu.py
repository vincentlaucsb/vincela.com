from collections import OrderedDict

# Requirements:
# Should be able to use Menu like:

# 1) Creating a menu:
# recipes_menu = Menu(some list containing tuples of names and URLs,parent_dir="http://www.vincentla.me/")
# parent_dir specifies a path that should be added before the URL

# 2) Retrieving a menu:
# recipes_menu --> returns --> dictionary of links and stuff

# 3) Retrieving specific URLs:
# x = Menu()
# x["Home"]["url"]
# i.e. simply call the variable referencing the Menu object!

# Modification/Addition #1: Create a function that allows user to request a subset of the menu
# e.g. by specifying which data field to search and what string to match by

class Menu(OrderedDict):
    # Accessing output: #
    #{% for key, values in menu.items %}
    #    <a href="{{ values.url }}">{{ key }}</a>
    #{% endfor %}
    def __init__(self,menu="",parent_dir=""):
        super(Menu, self).__init__()
        # Example input: #
        # menu = [
        #     ("Home",{"url":""}),
        #     ("About Me", {"url":"aboutme"}),
        #     ("Projects", {"url":"projects"}),
        #     ("Resume", {"url":"resume"})
        # ]    
        for item in menu:
            name = item[0]
            data = item[1]
                
            # Empty dictionary will be populated with data like URLs
            self[name] = {}
            
            for item in data:
                self[name][item] = data[item]

        self.parent = parent_dir
        
    # Addition 1 #
    # Goal: Return a new Menu object which only has items satisfying a certain #
    # search parameter #
    def subset(self,field,param):
        results = Menu(parent_dir=self.parent)
        for item in self.keys():
            if param.lower() == self[item][field].lower():
                results[item] = self[item]
        return results
        
    # Addition 2: Returns a Menu with the parent directory appended to all urls when called #
    def __call__(self):
        results = Menu()
        for item in self.keys():
            results[item] = {"url":self.parent + self[item]["url"]}
        return results
    
    # Addition 3: Return the first item matching the parameters #
    def get_item(self,**kwargs):
        results = set()
        for search_item in kwargs.keys():
            match_criteria = kwargs[search_item]
            match_results = set(self.subset(field=search_item,param=match_criteria))
            temp = [results,match_results]
            if results:
                results = set.intersection(*temp)
            else: results = match_results
        
        # Return first match as a SearchResult object
        if results:
            match_key = list(results)[0]
            return SearchResult(key=match_key,values=self[match_key])
        else:
            return ()
            
    # Addition 4: Get the previous/next item as a SearchResult object
    # Input: An item in the Menu
    def prev_item(self,name):
        if name in self:
            keys = list(self.keys())
            prev_item_index = keys.index(name) - 1
            if prev_item_index >= 0:
                return SearchResult(keys[prev_item_index],self[keys[prev_item_index]])
            else:
                return None
        else:
            raise KeyError(name)
    def next_item(self,name):
        if name in self:
            keys = list(self.keys())
            next_item_index = keys.index(name) + 1
            if next_item_index < len(keys):
                return SearchResult(keys[next_item_index],self[keys[next_item_index]])
            else:
                return None
        else:
            raise KeyError(name)
    
    # Addition 5: Ability to add dictionaries together #
    
    ## !! Need a way to deal with Menus with different parent_dirs !! ##
    ## Or prevent it from happening ##
    def __add__(self,other):
        result = Menu(parent_dir=self.parent)
        for item in self.keys():
            result[item] = self[item]
        for item in other.keys():
            result[item] = other[item]
        return result
    
    # Addition 6: If a key does not exist, then automatically set its value to the empty dictionary
    def __getitem__(self,key,*args,**kwargs):
        
        # Why doesn't this work
        #if key not in self.keys():
        #    print("__getitem__ method called with",self,key,args,kwargs,sep="\n")
        #    self[key] = {}
            
        return super(Menu,self).__getitem__(key)    
                
# Generate a bulleted list from a Menu object #
def create_bulleted_list(input):
    if type(input) is Menu or type(input) is DjangoMenu:
        html = "<ul>"
        menu = input
        for item in menu:
            html += "<li><a href='{0}'>{1}</a></li>".format(menu[item]["url"],item)
        html += "</ul>"
        return html
    else:
        raise TypeError("This function only works on Menu or DjangoMenu objects")
            
# Used for representing search results from the Menu class
# Input: A key (string) and a dictionary of values
# Goal: A class that
#   1) Returns the name of its key
#   2) Stores the input dictionary keys and values as class attributes
class SearchResult:

    '''
    Example SearchResult instance: 

    >>>
    >>> x = SearchResult(key="About Me",values={'url':"/aboutme",'description':"About Vincent La"})
    >>> x
    About Me
    >>> x.url
    '/aboutme'
    >>> x.description
    'About Vincent La'

    '''
    def __init__(self,key,values):
        self.key = key
        for field in values.keys():
            self.__setattr__(field,values[field])
    def __repr__(self):
        return self.key
    def __getattr__(self,name):
        raise KeyError(name)