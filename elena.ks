
website: {
    name: "elena",
    prettyName: "Elena's Homeschool Website",
    author: "Lacey B Carlyle", 
    theme: "minecraft",
    hostname: "homework.brilliantsquid.com",
    root: "/home/homework/laceyhw/"
}, 

apps: {
    science: {
	models: {

	    Subject: {
		fields: {
		    title: {type: "CharField", length: 30}
		},
		admin: "%title"
	    },
	    
	    Source: {
		fields: {
		    title: {type: "CharField", length: 30, label: "Field of Study:"}
		},
		admin: "%title"
	    },

	    Submission: {
		fields: {
		    date: {type: "DateField", argstring: "auto_now=True", form: "False"},
		    source: {type: "ForeignKey", link: "'Source'", label: "Created By:"},
		    title: {type: "CharField", length: 64, label: "I watched:"},
		    subject: {type: "ForeignKey", link: "'Subject'", label: "Field of Study:"},
		    summary: {type: "TextField", label: "Short paragraph about what I learned:"},
		    other: {type: "TextField", label: "Other ideas or thoughts:"}

		},
		admin: "%title from %source",
		listing: "<h3>%title% - %subject% (%date%)</h3><p>By: %source%</p><p>Summary: %summary%</p><p>Other ideas: %other%</p>",
		display: "<h3>%title% - %subject% (%date%)</h3><p>By: %source%</p><p>Summary: %summary%</p><p>Other ideas: %other%</p>"
	    }
	}
    },

    current_events: {
	models: {
	    Source: {
		fields: {
		    title: {type: "CharField", length:30}
		},
		admin: "%title"
	    },

	    Submission: {
		fields: {
		    date: {type: "DateField", argstring: "auto_now=True", form: "False"},
		    source: {type: "ForeignKey", link: "'Source'"},
		    title: {type: "CharField", length: 64 },
		    whatDidYouLearn: {type : "TextField", label:"What did you learn?" }
		},
		admin: "%title",
		listing: "<h3>%title% - %source% (%date%)</h3><p>%whatDidYouLearn%</p>",
		display: "<h3>%title% - %source% (%date%)</h3><p>%whatDidYouLearn%</p>"
	    }
	}
    },

    math_history: {
	models: {
	    Submission: {
		fields: {
		    date: {type: "DateField", argstring: "auto_now=True", form: "False"},
		    mainContributor: { type: "CharField", length: 64, label: "Main Contributor:" },
		    year: {type: "CharField", length: 4 },
		    bigIdea: {type: "TextField", label: "What\\'s the big idea?"},
		    whatDidYouLearn: {type: "TextField", label: "What did you learn?"}
		},
		admin: "%mainContributor - %year",
		listing: "<h3>%mainContributor% - %year% (%date%)</h3><p>%bigIdea%</p><p>%whatDidYouLearn%</p>",
		display: "<h3>%mainContributor% - %year% (%date%)</h3><p>%bigIdea%</p><p>%whatDidYouLearn%</p>"
	    }
	}
    },

    pe: {
	models: {
	    Duration: {
		fields: {
		    time: { type: "SmallIntegerField" }
		},
		admin: "%time min"
	    },
	    
	    Activity:{
		fields: {
		    name: { type: "CharField", length: 64, label: "New Activity:" }
		},
		admin: "%name"
	    },
	    
	    Submission: {
		fields: {
		    date: {type: "DateField", argstring: "auto_now=True", form: "False"},
		    activity: {type: "ForeignKey", link:"'Activity'"},
		    duration: {type: "ForeignKey", link: "'Duration'" },
		    notes: {type: "TextField", label: "What did you do?"}

		},
		admin: "%activity %duration",
		listing: "<h3>%activity% - %duration% (%date%)</h3><p>%notes%</p>",		
		display: "<h3>%activity% - %duration% (%date%)</h3><p>%notes%</p>"

	    }
	}
    },
    
    mathematics: {
	models: {
	    Submission: {
		fields: {
		    date: {type: "DateField", argstring: "auto_now=True", form: "False"},
		    description: { type: "TextField", label: "What was the lesson about?" },
		    whatDidYouLearn: {type: "TextField", label: "What did you learn?" }
		},
		admin: "%description",
		listing: "<h3>%description% - (%date%)</h3><p>%whatDidYouLearn%</p>",
		display: "<h3>%description% - (%date%)</h3><p>%whatDidYouLearn%</p>"
	    }
	}
    }
},




menu: {
    Home:{ title: "Home", link: "/", placement: 0 },
    science: {title: "Life Science", link: "/science", placement: 1},
    currentEvents: {title: "Social Studies", link: "/current", placement: 2},
    math: {title: "Math", link: "/math", placement: 3},
    pe: {title: "P.E.", link: "/pe", placement: 4},
    log: {title: "Logs", link: "/log", placement: 5}
},

pages: {
    Home: {
	title: "Elena Bernard",
	url: "",
	template: f"home.html"
    },
    Science:{
	title: "Life Science",
	url: "science/",
	template: "<h1>Life Science</h1><div class='box'>%homework%</div><div class='box'>%addSubject%</div>",
	homework: { type: "expr", expr: F[](science->Submission), title: "What did you watch?", description: "Whether it was from <em>The Shape of Life</em> or a documentary from Netflix, log your science knowledge here." },
	addSubject: { type: "expr", expr: F[](science->Subject), title: "Add a new field of study", description: "Is the subject you want not in the list? Add it below, and refresh the page. <br> <center>ex. Anthropology, Paleontology, Xenolinguistics, etc.</center>" }
    },
    Current: {
	title: "Social Studies",
	url: "current/",
	template: f"ss.html",
	homework: { type: "expr", expr: F[](current_events->Submission),title:"", description: "" }
    },
    MathHistory: {
	title: "Math History",
	url: "mathhistory/",
	template: "<h1>Math History!</h1><div class='box'>%homework%</div>",
	homework: { type: "expr", expr: F[](math_history->Submission) }
    },
    Mathematics: {
	title: "Mathematics",
	url: "math/",
	template: "<h1>Mathematics!</h1><div class='box'>%homework%</div>",
	homework: { type: "expr", expr: F[](mathematics->Submission), title: "", description: "" }
    },
    PE: {
	title: "Physical Education",
	url: "pe/",
	template: "<h1>Physical Education</h1><div class='box'>%homework% %addSubject%</div>",
	homework: { type: "expr", expr: F[](pe->Submission), title: "Log Your Activities", description: "What did you do to move your body today?" },
    	addSubject: { type: "expr", expr: F[](pe->Activity), title:"Add a New Activity", description: "Add a new activty, then refresh the page. <br> <center>ex. Unicycle Ride, Bike Ride, Beach, Swimming, etc.</center>" }
    },
    log: {
	title: "Log",
	url: "log/",
	template: f"log.html",
	scienceList: { type: "expr", expr: S[](science->Submission) },
	currentList: { type: "expr", expr: S[](current_events->Submission) },
	peList: { type: "expr", expr: S[](pe->Submission) },
	mathList: { type: "expr", expr: S[](mathematics->Submission) }
    }
},

database: {
    name: "elena.db",
    engine: "django.db.backends.sqlite3"
}
