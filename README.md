## NOTICE
This project was used as a project for a course on Interaction Design, and is not under development anymore. Feel free to dive in.

## About
Project for the Interaction Design course.

The project consists of a website for people who wants to create their own portfolio.
The website should also contain functionality for browsing/searching through portfolios, to find potential employees.

## Model
Our model is a website (written in HTML, CSS and Python).

### Required
Required modules is needed:
 - python (possibly python3)
 - cherrypy
 - jinja2

### How to start the site

Edit ```portfoliosite.conf``` and change the ```tools.staticdir.root``` parameter according to your local path to the project folder.

Run to start the webserver
```
python3 portfoliosite.py
```

If no errors occurs, the website should be accessible at
```
localhost:8080
```

## References
We've made use of the fancyBox jQuery lightbox (http://fancyapps.com/fancybox/), which is awesome!	
