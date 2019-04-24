
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


# Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://artistmatch-humbleafrika.c9users.io/' and the admin page from 
'https://artistmatch-humbleafrika.c9users.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

# Art Match Final Milestone Project #

## Project Requirements ##
    
In this project I'll be building a website using the django/python interactive framework for a start-up project called *Art Match*. The requirements of the project is shown below :

Now that you’re a full-fledged web developer you’ve decided it’s probably time for you to start your very own cool, modern startup, offering the extremely awesome UnicornAttractor web app to your users. It’s really really amazing, but we don’t care about it at all in this project. The exciting thing is the business model that you’ve decided upon – you chose to offer the service and bug fixes for free, but ask for money from your users to develop additional features.
The primary entity in the Issue Tracker is a ticket describing a user’s issue, and similar to Github’s issue tracker, you should allow users to create tickets, comment on tickets, and show the status of the ticket (e.g. ‘to do,’ ‘doing,’ or ‘done’). As mentioned, issues come in two varieties – ‘bugs’ (which you’ll fix for free, eventually), and ‘features’ which you’d only develop if you’re offered enough money. To help you prioritize your work, your users will be able to upvote bugs (signifying ‘I have this too’), and upvote feature requests (signifying ‘I want to have this too’). While upvoting bugs is free, to upvote a feature request, users would need to pay some money (with a minimum amount of your choice) to pay for your time in working on it. In turn, you promise always to spend at least 50% of your time working on developing the highest-paid feature.
To offer transparency to your users, you decide to create a page that contains some graphs showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features.
Add any additional pages that would help you attract users to the Issue Tracker (and have them pay you well). To make the users participate as much as possible in your online community, make sure that your UI/UX is sublime. Feel free to add additional features, such as a blog, extra perks for active participants, etc.
If you want to have some more fun with this, feel free also to add pages describing your fictional UnicornAttractor application.
And of course, as this project is going to be the lifeblood of your company, it’s essential that new developers that join the company will be able to get up and running as quickly as possible. Documentation is the best way to achieve this.

    
As stated earlier I am building a site named *Art Match (AM)*
    
The idea is to match Art (both Audio and Visual).

It will qualify the following categories in the assignment brief 
    
    - Users can sign up to the site for free
    - The can report bugs (ticket creation)
    - They can also suggest features / updates (ticket creation)
    - Issue Trackers (ticket tracker)
    - Comment on tickets
    -- added extras -- could be an about page (time dependant)
        
### *Sign Up and Artist Profiles* ###
     - Sign up will include Art profiles where Art
     - Upload their work to be considered by other Art
     - Their work can be voted on by fellow Art
         
### *Bug Requests* ###
     - Artist can also post bug resolution requests
     - All Art having the same issue can click on a tag to signal 
     the instance of the same issue
            
### *Feature Requests* ###
     - Art can request a feature to be added to the page at a minimum cost of £3.
     - This can be voted on as well as funding topped up by other Art
     - The first feature request to cross the threshold of £250 will 
        trigger an immediate attention flag (moved to to-do list)
         
### *Issue Trackers* ###
     - I intend to use charts and graphs visible to all users to track progress 
        of requests and bug updates
         
### *Developers* ###
     - Can mark tickets/ tasks as working on to move tickets into work in progress.

[ ] An uncompleted task
[x] A completed task
          
## FEATURES ##
    
    Each page will have a standard menu across the site. 
    A default homepage - Then extra menu options after login
    
### PAGES ###
     - Index
     - Works
     - Bug Requests
     - Feature Requests
     - Work With Artist (test feature)
     - Sample Art Work (Music test feature)
     - About
    
## TECHNOLOGY USED ##
    
    The technologies used in this project are HTML5, CSS, Python, Django JavaScript and Bootstrap.
        
    django will allow me to build a website in smaller feature chunks with little effort. 
        
        HTML was use for the structuring of the pages
        Bootstrap was use to ensure that the page appear a certain way on mobiles and another on tablets, desktops and laptops
        Javascript was used mainly for showing the mapping on the home page
        CSS was used to beautify the page and make the structure stand out with the different colours.
    
    I used the following libraries || link to libraries
    
    bootstrap || https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css 
    fontawesome || https://use.fontawesome.com/releases/v5.5.0/css/all.css
    css libraries || https://cdnjs.cloudflare.com/ajax/libs/hover.css/2.1.1/css/hover-min.css
    
    https://git.heroku.com/artisth.git
    
    https://developers.google.com/maps

    
## TESTING ##
    
    Mobile - I have accessed the site on my mobile as well as asked others in my household to access it on their mobiles and give me feedback. No errors were encounted.
    
    Tablet - I have accessed the site on my ipad with no issues recognised.
    
    Desktop - I have accessed the site on my desktop. No errors were encounted. I also tested using the element inspector and showed the various
    pages in the virtual devices build into my browser.
    
    Javascript - JavaScript was tested in console and jsfiddle (see image file in images photo of testing.jpg)
    
    The project appears well on a number of virtual screens therefore we can only rely on user feedback to make any improvements.
    
    The project was produced in cloud9 
    
    Updates have been saved to :
    
    https://github.com/humbleafrica/UCFDMP
    
    The Webpage is hosted at:
    
    https://preview.c9users.io/humbleafrika/user_centric_milestone_project/index.html
    
    
    
## MEDIA ##
    

    The photos and music material used in this site were obtained from:
    
    https://www.google.com
    https://soundcloud.com/akanmusic
    
    
    
## ACKNOWLEDGEMENTS ##

    I received inspiration for this project from 
    
    UserCentricFrontendDevelopment CV resume example
    
    Sincere thanks to Kwabena Appiah who allowed me to use his material and social media sites for this project
    
    
Thank you for 
You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide