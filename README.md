# Moose Juice
![alt text](# "Responsive sample")

**[Live demo](#)**
---
<span id="top"></span>
## Index
- <a href="#context">Context</a>
- <a href="#ux">UX</a>
  - <a href="#ux-overview">Overview</a>
  - <a href="#ux-stories">User stories</a>
  - <a href="#ux-wireframes">Wireframes</a>
  - <a href="#ux-design">Design</a>
- <a href="#database-model">Database model</a>
- <a href="#features">Features</a>
  - <a href="#features-current">Current</a>
  - <a href="#features-future">Future</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>
---
<span id="context"></span>

## Context
The COVID-19 pandemic has had a dramatic effect on everyone's lives, not least those of working parents who can no longer rely on childcare or school due to the restrictions put in place.

When a case occurs in your child's bubble and they are forced to self-isolate at home, you can expect to spend your days fitting work in around your children's homeschooling
and other needs. Without the option of leaving the house you'll be climbing the walls in no time, feeling guilty that you've left them to watch Peppa Pig for 4 hours straight, again.
You need to break the cycle and find some inspiration without having to create elaborate plans which will likely be greeted with a slow clap and roll of the eyes, leaving you
ever more frustrated with them, yourself and the situation at large. You need a Self Isolution.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="ux"></span>

## UX

<span id="ux-overview"></span>

### Overview
Self Isolution is a site aimed at parents of young children who have been put into self-isolation. Users are looking for ideas for simple activities to entertain, educate and somehow enrich the lives of their offspring, without leaving the comfort of their own homes. All content is available without registering, but once logged in users can add their
own activity ideas and share the collective burden of raising this misfortunate generation.
All design decisions have been made with the following goals in mind:
- TBC
<span id="ux-stories"></span>

### User stories

#### Overarching user expectations
- TBC
#### As a first-time visitor I want
- TBC
#### As a returning user I want
- TBC
#### As the site owner I want:
- TBC
<span id="ux-wireframes"></span>

### Wireframes
Wireframes created at the start of the project for **mobile**, **tablet** and **desktop** can be accessed [here](wireframes/), as well as the planned **site map** and **data schema**.

There were some noteworthy deviations from the plan. These were:
1. TBC

<span id="ux-design"></span>

### Design choices
TBC

#### Colours
TBC

**Core**
TBC
- ![#3949ab](https://via.placeholder.com/15/3949ab/000000?text=+) #3949ab (indigo darken-1)
- ![#1a237e](https://via.placeholder.com/15/1a237e/000000?text=+) #1a237e (indigo darken-4)

**Cards**
TBC
- ![#e8eaf6](https://via.placeholder.com/15/e8eaf6/000000?text=+) #e8eaf6 (indigo lighten-5)
- ![#f1f8e9](https://via.placeholder.com/15/f1f8e9/000000?text=+) #e8eaf6 (light-green lighten-5)
- ![#0077ff](https://via.placeholder.com/15/0077ff/000000?text=+) #0077ff ("Dodger Blue")

**Buttons**
TBC
- ![#26a69a](https://via.placeholder.com/15/26a69a/000000?text=+) #26a69a (teal lighten-1)
- ![#3f51b5](https://via.placeholder.com/15/3f51b5/000000?text=+) #3f51b5 (indigo)
- ![#f44336](https://via.placeholder.com/15/f44336/000000?text=+) #f44336 (red)
- ![#ff6d00](https://via.placeholder.com/15/ff6d00/000000?text=+) #f44336 (orange accent-4)

**Transition and transformation**
TBC

#### Fonts
[Bubblegum Sans](https://fonts.google.com/specimen/Bubblegum+Sans#about)
TBC
[Montserrat](https://fonts.google.com/specimen/Montserrat#about)
TBC
<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="database-model"></span>

### Database model
TBC

#### Activities collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|TBC|TBC|TBC|

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="features"></span>

## Features
<span id="features-current"></span>

### Current

**1. Material design**
MaterializeCSS features:
- [Cards](https://materializecss.com/cards.html)
- [Forms](https://materializecss.com/text-inputs.html)
- [Menu dropdown](https://materializecss.com/dropdown.html)
- [Modals](https://materializecss.com/modals.html)
- [Sidenav](https://materializecss.com/sidenav.html)
- [Toasts](https://materializecss.com/toasts.html)

**2. Secure passwords**
When registering for the site, the user's password is hashed so that it is not revealed to the database owner.

**3. CRUD functionality**

Visitors can:
- View all activities
- View all categories.

Users can:
- Add their own activities
- Edit their own activities 
- Delete their own activities.

The admin can:
- Add their own activities
- Edit any users' activities
- Delete any users' activities
- Add a category
- Edit a category
- Delete a category.

**4. Image uploads**
Rather than having to find a URL for an image, users can upload their own files. This encourages them to provide their own content, but if they skip this step then a default image is displayed from the relevant category.

**5. Image resizing**
Prior to uploading an image, a user's file is resized so that it does not adversely affect site load times, and also gives some control over its dimensions.

**6. User profile**
Users can view all activities they have created in one place and easily edit or delete them.

**7. Admin rights**
The admin has the additional ability to:
- Edit or delete any activity on the site from its View Activity page
- Add categories
- Edit a category summary or image (but they cannot edit the name of a category to preserve relationship integrity)
- Delete categories from the Categories page, with measures for preserving relational integrity for activities no longer associated with a category.

**8. Confirm delete**
When the user or admin clicks to delete an activity or category, a modal pops up to confirm they wish to do so to prevent accidental deletion.

**9. Category reassignment on deletion**
When the admin chooses to delete a category which has associated activities, these activities are moved to the 'Unassigined' category and are still visible on the site.

**10. Search**
All users can search for keywords appearing in:
- Activity title
- Activity summary
- Activity description
- Activity required equipment
Activities can be filtered by category from the Categories page and also by target age or activity author by clicking on the associated tag from the Activities, View Activity or Profile pages.

**11. Pagination**
The Activities page (and any search or filters applied) will limit the number of activities visible to 9 in order to reduce the number of images loaded and keep the focus on the content. As individual users are unlikely to be adding much more than 9 activities, it makes sense not to paginate the Profile page to avoid spilling onto a second page in this rare instance.

**12. Access protection**
Routes to restricted functions such as add, edit and delete (for both session user and admin) are protected so that they cannot be accessed by brute force via the URL.

**13. 404 and 500 error handling**
Pages for 404 and 500 errors keep the user on the site when something goes wrong, allowing them to return to the content with minimal disruption.

<span id="features-future"></span>

### Future
- TBC
<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="technologies"></span>

## Technologies Used

### Languages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Frameworks
- [Flask](https://palletsprojects.com/p/flask/)
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)

### Extensions and kits
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [django-colorfield](https://pypi.org/project/django-colorfield/)
- [jscolor](https://jscolor.com/)

### Project management
- [Amazon AWS](https://aws.amazon.com/) (S3)
- [Balsamiq](https://balsamiq.com/wireframes/)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)

### Tools
- [Am I Responsive?](http://ami.responsivedesign.is/)
- [Autoprefixer](https://autoprefixer.github.io/)
- [Favicon.io](https://favicon.io//)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="deployment"></span>

## Deployment
The master branch of this repository is the most current version and has been used for the deployed version of the site. A separate branch was used for implementing... TBC

### Prerequisites
[Python 3](https://www.python.org/downloads/) - core code
[PIP](https://pypi.org/project/pip/) - package installation
[Git](https://git-scm.com/) - version control
[Amazon AWS S3 Bucket](https://aws.amazon.com/)
- An Amazon S3 Bucket is used to host the images uploaded to the app by its users.

***Values for the env.py environment variables and Heroku Cvars used in the sections below will be unique to each MongoDB and S3 Bucket created. Please refer to their respective documentation for further details.***

### How to clone Moose Juice
To clone this project from its [GitHub repository](https://github.com/Edb83/moose-juice):
1. From the repository, click **Code**
2. In the **Clone >> HTTPS** section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2
```console
git clone https://github.com/Edb83/moose-juice.git
```
6. Press Enter. Your local clone will be created
7. Create a file called env.py to hold your app's environment variables, which should contain the following:

```console
import os
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<app secret key>")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg.mongodb.net/<database_name>?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<database name>")
os.environ.setdefault("S3_BUCKET", "<S3 bucket name>")
os.environ.setdefault("S3_KEY", "<S3 key>")
os.environ.setdefault("S3_SECRET_ACCESS_KEY", "<S3 secret key>")
os.environ.setdefault("S3_LOCATION", "https://<S3 bucket name>.s3.<S3 bucket region>.amazonaws.com/")
```
8. **Make sure that env.py is listed in your .gitignore file to prevent your environment variables being pushed publicly**
9. The app can now be run locally using
```console
python3 app.py
```

### How to deploy to Heroku
To deploy the app to Heroku from its [GitHub repository](https://github.com/Edb83/moose-juice), the following steps were taken:
1. From the GitPod terminal, create **requirements.txt** and **Procfile** using these commands:
```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```
2. **Push** these files to GitHub
3. **Log In** to [Heroku](https://id.heroku.com/login)
4. Select **Create new app** from the dropdown in the Heroku dashboard
5. Choose a unique name ('self-isolution') for the app and the location nearest to you
6. Go to the **Deploy** tab and under **Deployment method** choose GitHub
7. In **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
9. Enter the following keys and values, which must match those in the env.py file created earlier:

|**Key**|**Value**|
|:-----|:-----|
|IP|`0.0.0.0`|
|PORT|`5000`|
|SECRET_KEY|`<app secret key>`|
|MONGO_URI|mongodb+srv://`<username>`:<password>@`<cluster_name>`-ofgqg.mongodb.net/`<database_name>`?retryWrites=true&w=majority|
|MONGO_DBNAME|`<database name>`|
|S3_BUCKET|`<S3 bucket name>`|
|S3_KEY|`<S3 key>`|
|S3_SECRET_ACCESS_KEY|`<S3 secret key>`|
|S3_LOCATION|https://`<S3 bucket name>`.s3.`<S3 bucket region>`.amazonaws.com/|
10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
11. Under **Manual deploy**, select **master** and click **Deploy Branch**
12. Once the app has finished building, click **Open app** from the header row of the dashboard
<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>
<span id="testing"></span>

## Testing
Full details of testing can be found [here](TESTING.md).

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="credits"></span>

## Credits

### Tutorials / Resources
- [How to work with AJAX requests with Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html)

### Student projects
- [LigaMoon's Prickly](https://github.com/LigaMoon/Prickly)

### Code modified from other sources
- [TBC](#)

### Content
- All text outside of user-generated content is original
- [Star rating implementation](https://github.com/LigaMoon/Prickly/blob/main/products/static/products/js/product_item.js)
- [Favicon](https://favicon.io/emoji-favicons/house)
- Images from [Pixabay](https://pixabay.com/)

### Acknowledgements
- TBC

### Disclaimer
This site was developed for educational purposes.
<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>
