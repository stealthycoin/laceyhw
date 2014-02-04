class R_Expr:
    def __init__(self,r_type,r_restrictions,r_set):
        self.expression_type = r_type
        self.restrictions = r_restrictions
        self.target_set = r_set
    def show(self,key,title,desc):
        #always need this just to be able to retrieve things from database
        result = self.expression_type.showImports(self.target_set)
        result += self.restrictions.show()
        result += self.expression_type.show(key,self.target_set,title,desc)

        return result

class R_Type:
    def __init__(self,t):
        self.type_symbol = t

    def showImports(self, ts):
        if self.type_symbol == 'S':
            result = "from %s.views import get%s\n" % (ts.app,ts.model)
            result += "from %s.models import %s\n" % (ts.app,ts.model)
            result += "qs = %s.objects.all()\n" % ts.model
            return result
            
        if self.type_symbol == 'F':
            return "from %s.forms import %sForm\n" % (ts.app,ts.model)

    def show(self,key,ts,title,desc):
        result = "from django.template import RequestContext\n"
        result += "d['%s'] = " % key
        if self.type_symbol == 'S':
            result += "get%s(qs)\n" % ts.model
        if self.type_symbol == 'F':
            result += "render_to_string('form.html', {'title':'%s', 'description': '%s', 'action':'/api/%s/%s/create/','formFields':%sForm().as_p()},context_instance=RequestContext(request))\n" % (title,desc,ts.app,ts.model,ts.model)

        return result

class R_Restrictions:
    def __init__(self,restrictions):
        self.restrictions = restrictions

    def showEquality(self, r):
        """TODO: Needs to eventually deal with types"""
        return "qs = qs.filter(%s=%s)\n" % (r[0],r[2].replace('%','u_'))

    def show(self):
        #restrictions are a tuple (field,op,value) different ops imply different logic
        result = ""
        for restriction in self.restrictions:
            if restriction[1] == '=':
                result += self.showEquality(restriction)

        return result

class R_Set:
    def __init__(self,app,model):
        self.app = app
        self.model = model

    def showUserCase(self):
        return ""

    def show(self):
        return "(%s->%s)" %(self.app, self.model)

    
d = {"database":{"engine":"django.db.backends.sqlite3","name":"elena.db"},"pages":{"log":{"mathList":{"expr":R_Expr(R_Type("S"),R_Restrictions([]),R_Set("mathematics","Submission")),"type":"expr"},"peList":{"expr":R_Expr(R_Type("S"),R_Restrictions([]),R_Set("pe","Submission")),"type":"expr"},"currentList":{"expr":R_Expr(R_Type("S"),R_Restrictions([]),R_Set("current_events","Submission")),"type":"expr"},"scienceList":{"expr":R_Expr(R_Type("S"),R_Restrictions([]),R_Set("science","Submission")),"type":"expr"},"template":"<h1>Log</h1>\n\n<div class='box'>\n  <h2>Life Science</h2>\n  %scienceList%\n</div>\n\n<div class='box'>\n  <h2>Social Studies</h2>\n  %currentList%\n</div>\n\n<div class='box'>\n  <h2>Math</h2>\n  %mathList%\n</div>\n\n<div class='box'>\n  <h2>Physical Education</h2>\n  %peList%\n</div>\n\n\n","url":"log/","title":"Log"},"PE":{"addSubject":{"description":"Add a new activty, then refresh the page. <br> <center>ex. Unicycle Ride, Bike Ride, Beach, Swimming, etc.</center>","title":"Add a New Activity","expr":R_Expr(R_Type("F"),R_Restrictions([]),R_Set("pe","Activity")),"type":"expr"},"homework":{"description":"What did you do to move your body today?","title":"Log Your Activities","expr":R_Expr(R_Type("F"),R_Restrictions([]),R_Set("pe","Submission")),"type":"expr"},"template":"<h1>Physical Education</h1><div class='box'>%homework% %addSubject%</div>","url":"pe/","title":"Physical Education"},"Mathematics":{"homework":{"description":"","title":"","expr":R_Expr(R_Type("F"),R_Restrictions([]),R_Set("mathematics","Submission")),"type":"expr"},"template":"<h1>Mathematics!</h1><div class='box'>%homework%</div>","url":"math/","title":"Mathematics"},"MathHistory":{"homework":{"expr":R_Expr(R_Type("F"),R_Restrictions([]),R_Set("math_history","Submission")),"type":"expr"},"template":"<h1>Math History!</h1><div class='box'>%homework%</div>","url":"mathhistory/","title":"Math History"},"Current":{"homework":{"description":"","title":"","expr":R_Expr(R_Type("F"),R_Restrictions([]),R_Set("current_events","Submission")),"type":"expr"},"template":"<h1>Social Studies!</h1>\n<div class='box'>\n  <h2>Watch Daily:</h2>\n  \n  <a href=\"http://www.cnn.com/studentnews/\">CNN Student News</a>\n<br>\n<center><h3>What was in the News today?</h3></center>\n  %homework%\n<br><br>\n</div>\n\n<br>\n\n<div class='box'>\n<h2>Watch 3 per Week:</h2>\n\n\n<h3>Crash Course #1</h3>\n<center><iframe width=\"640\" height=\"360\" src=\"//www.youtube.com/embed/Yocja_N5s1I?list=PLBDA2E52FB1EF80C9\" frameborder=\"0\" allowfullscreen></iframe></center>\n<br>\n%homework%\n<br><br>\n<h3>Crash Course #2</h3>\n<center><iframe width=\"640\" height=\"360\" src=\"//www.youtube.com/embed/n7ndRwqJYDM?list=PLBDA2E52FB1EF80C9\" frameborder=\"0\" allowfullscreen></iframe></center>\n<br>\n%homework%\n<br><br>\n<h3>Crash Course #3</h3>\n<center><iframe width=\"640\" height=\"360\" src=\"//www.youtube.com/embed/sohXPx_XZ6Y?list=PLBDA2E52FB1EF80C9\" frameborder=\"0\" allowfullscreen></iframe></center>\n<br>\n%homework%\n<br><br>\n</div>\n","url":"current/","title":"Social Studies"},"Science":{"addSubject":{"description":"Is the subject you want not in the list? Add it below, and refresh the page. <br> <center>ex. Anthropology, Paleontology, Xenolinguistics, etc.</center>","title":"Add a new field of study","expr":R_Expr(R_Type("F"),R_Restrictions([]),R_Set("science","Subject")),"type":"expr"},"homework":{"description":"Whether it was from <em>The Shape of Life</em> or a documentary from Netflix, log your science knowledge here.","title":"What did you watch?","expr":R_Expr(R_Type("F"),R_Restrictions([]),R_Set("science","Submission")),"type":"expr"},"template":"<h1>Life Science</h1><div class='box'>%homework%</div><div class='box'>%addSubject%</div>","url":"science/","title":"Life Science"},"Home":{"template":"<div class='box'><h2>Welcome!</h2></br><center><img src=\"http://hydra-media.cursecdn.com/minecraft.gamepedia.com/thumb/a/aa/Babycow.png/88px-Babycow.png\" alt=\"LOOK AT THIS BABY COW. LOVE IT. WOOOOOOOOORSHIP IT.\" title=\"LOOK AT THIS BABY\\n COW. LOVE IT. WOOOOOOOOORSHIP IT.\"></center></br>Click on the links above to go to a topic page.</div>\n\n<br>\n\n</div>\n","url":"","title":"Elena Bernard"}},"menu":{"log":{"placement":5,"link":"/log","title":"Logs"},"pe":{"placement":4,"link":"/pe","title":"P.E."},"math":{"placement":3,"link":"/math","title":"Math"},"currentEvents":{"placement":2,"link":"/current","title":"Social Studies"},"science":{"placement":1,"link":"/science","title":"Life Science"},"Home":{"placement":0,"link":"/","title":"Home"}},"apps":{"mathematics":{"models":{"Submission":{"display":"<h3>%description% - (%date%)</h3><p>%whatDidYouLearn%</p>","listing":"<h3>%description% - (%date%)</h3><p>%whatDidYouLearn%</p>","admin":"%description","fields":{"whatDidYouLearn":{"label":"What did you learn?","type":"TextField"},"description":{"label":"What was the lesson about?","type":"TextField"},"date":{"form":"False","argstring":"auto_now=True","type":"DateField"}}}}},"pe":{"models":{"Submission":{"display":"<h3>%activity% - %duration% (%date%)</h3><p>%notes%</p>","listing":"<h3>%activity% - %duration% (%date%)</h3><p>%notes%</p>","admin":"%activity %duration","fields":{"notes":{"label":"What did you do?","type":"TextField"},"duration":{"link":"'Duration'","type":"ForeignKey"},"activity":{"link":"'Activity'","type":"ForeignKey"},"date":{"form":"False","argstring":"auto_now=True","type":"DateField"}}},"Activity":{"admin":"%name","fields":{"name":{"label":"New Activity:","length":64,"type":"CharField"}}},"Duration":{"admin":"%time min","fields":{"time":{"type":"SmallIntegerField"}}}}},"math_history":{"models":{"Submission":{"display":"<h3>%mainContributor% - %year% (%date%)</h3><p>%bigIdea%</p><p>%whatDidYouLearn%</p>","listing":"<h3>%mainContributor% - %year% (%date%)</h3><p>%bigIdea%</p><p>%whatDidYouLearn%</p>","admin":"%mainContributor - %year","fields":{"whatDidYouLearn":{"label":"What did you learn?","type":"TextField"},"bigIdea":{"label":"What\\'s the big idea?","type":"TextField"},"year":{"length":4,"type":"CharField"},"mainContributor":{"label":"Main Contributor:","length":64,"type":"CharField"},"date":{"form":"False","argstring":"auto_now=True","type":"DateField"}}}}},"current_events":{"models":{"Submission":{"display":"<h3>%title% - %source% (%date%)</h3><p>%whatDidYouLearn%</p>","listing":"<h3>%title% - %source% (%date%)</h3><p>%whatDidYouLearn%</p>","admin":"%title","fields":{"whatDidYouLearn":{"label":"What did you learn?","type":"TextField"},"title":{"length":64,"type":"CharField"},"source":{"link":"'Source'","type":"ForeignKey"},"date":{"form":"False","argstring":"auto_now=True","type":"DateField"}}},"Source":{"admin":"%title","fields":{"title":{"length":30,"type":"CharField"}}}}},"science":{"models":{"Submission":{"display":"<h3>%title% - %subject% (%date%)</h3><p>By: %source%</p><p>Summary: %summary%</p><p>Other ideas: %other%</p>","listing":"<h3>%title% - %subject% (%date%)</h3><p>By: %source%</p><p>Summary: %summary%</p><p>Other ideas: %other%</p>","admin":"%title from %source","fields":{"other":{"label":"Other ideas or thoughts:","type":"TextField"},"summary":{"label":"Short paragraph about what I learned:","type":"TextField"},"subject":{"label":"Field of Study:","link":"'Subject'","type":"ForeignKey"},"title":{"label":"I watched:","length":64,"type":"CharField"},"source":{"label":"Created By:","link":"'Source'","type":"ForeignKey"},"date":{"form":"False","argstring":"auto_now=True","type":"DateField"}}},"Source":{"admin":"%title","fields":{"title":{"label":"Field of Study:","length":30,"type":"CharField"}}},"Subject":{"admin":"%title","fields":{"title":{"length":30,"type":"CharField"}}}}}},"website":{"root":"/home/homework/laceyhw/","hostname":"homework.brilliantsquid.com","theme":"minecraft","author":"Lacey B Carlyle","prettyName":"Elena's Homeschool Website","name":"elena"}}

