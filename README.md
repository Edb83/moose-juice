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
Smoking will kill you. Anyone who smokes should explore vaping as an enjoyable means to kick the habit. The only risk is taking up a different, albeit much safter habit.

Vaping has become mainstream. The userbase is broad and has varied wants and expectations, from the older generation looking to quit the habit, to the hobbyists spending vast sums on their hardware. There are many online vaping stores out there, but they tend to be busy and bloated, selling anything you might ever need but with little style. The simplest and most crucial part of the industry is the e-liquid itself, and that's where Moose Juice comes in.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="ux"></span>

## UX

<span id="ux-overview"></span>

### Overview
Unconcerned with selling hardware in its myriad forms, Moose Juice is focused on providing nothing but high quality, home-brewed e-liquid and delivering a great user experience. With an aesthetic not typically seen in larger vaping e-commerce stores and an accessible rewards system, the company hopes to retain and grow its clientele, guided by their feedback. The target audience is 25 - 40-yr-old smokers and existing vapers looking for a dedicated juice supplier. Converting a sale will rely on quickly signposting potential customers to relevant products and then giving them options.

The two questions asked by the site are "What's your flavour?" and "How do you vape?"

#### Flavours
Flavour and choice are paramount at Moose Juice. That's what will keep people off cigarettes for good. Options to filter by common vaping flavour profiles (bakery, dessert, fruit etc) are complimented by the ability to search for individual flavour notes (cinnamon, cream, apple etc). When browsing for a new juice to try, most users will go straight for an individual flavour and then make a choice based on its popularity.

#### Brands
As far as e-liquid goes, all vapers will fall into one of three categories. Moose Juice has a brand for each category:

**Big Moose**

For use in 'sub-ohm' devices, which need a lot of juice to produce those thick clouds. This type of e-liquid has a thicker consistency and as it's used up quickly needs to come in larger bottles. Due to the TPD Regulations it cannot be sold pre-mixed with nicotine.

**Mini Moose**

One of two Moose Juice brands aimed at users of discreet 'pod' systems. These thinner juices come in a variety of pre-mixed freebase nicotine strengths and to comply with TPD Regulations must not be sold in bottles larger than 10ml.

**Salty Moose**

These pre-mixed juices use nicotine salts rather than freebase, providing a much quicker absorbtion rate akin to that of traditional cigarettes and a smoother 'throat hit' on the inhale.

The way each brand of e-liquid is made means that certain flavour combinations are better suited to one over another. Moose Juice's expertise in understanding these differences is what makes them so good. A particular mix of flavours will only appear in one brand.

<span id="ux-stories"></span>

### User stories

#### Overarching user expectations
- Consistent
- Easy to navigate
- Intuitive
- Responsive
- Secure
- Visually pleasing

|**As a...**|**I want to...**|**So I can...**|
|:-----|:-----|:-----|
|Potential customer|Immediately understand the purpose of the site|Decide whether to stay|
||Easily browse through juices|Learn how much they cost and how others have rated them|
||Create an account easily|Purchase products|
||Add items to my shopping cart before registering|Avoiding registering if not necessary|
||Learn about a specific juice's flavour profile|Make an informed purchase decision|
||Search by juice name and flavour|Find specific products|
||Filter by broad flavour profiles|Find juices matching my taste|
||Filter by individual flavours|Quickly find the flavours I like|
||Read reviews/ratings for juices|Making informed purchase decisions|
||Learn about any rewards system|Register with confidence|
||Choose bottle size and nicotine content|Customise purchases to my preference|
|Registered user|Save my default delivery details|Proceed to checkout more quickly in future|
||Add a juice to my favourites list|Quickly find a product I'd like to purchase again|
||View my previous purchases|Make repeat orders|
||Leave a review and rating for juices|Inform others about good/bad juices|
||Know that a review has come from a verified purchase|Make informed purchase decisions|
||Review my basket prior to checkout|Remove/adjust quantities|
||Receive confirmation of my orders|Have proof of purchase|
||See what juices are on sale|Find the best value for money|
||Receive free delivery above an order threshold|Feel rewarded for larger purchases|
||Receive reward points|Get discounts on future purchases and feel rewarded for my loyalty|
||View my reward points|See what I can redeem on future purchases|
|Site owner|View, add, edit and delete products|Keep the product list up to date|
||Have a flexible reward system|Entice new customers and reward existing members|
||Have a simple payment structure|Easily make price changes for all products|


<span id="ux-wireframes"></span>

### Wireframes
Wireframes created at the start of the project for **mobile**, **tablet** and **desktop** can be accessed [here](wireframes/), as well as the planned **site map** and **data schema**.

There were some noteworthy deviations from the plan. These were:
1. Not including a blog app due to time constraints. This would be relatively simple to implement
2. Not including a suggestion for similar products, again due to time constraints. This could be expanded to include an algorithm to suggest products based on order history or current browsing habits
3. Not including a bespoke login page as the allauth template was adequate
4. Not including breadcrumbs due to unexpected complexity and insufficient time
5. Not including pagination due to lack of time

<span id="ux-design"></span>

### Design choices
Bootstrap provides a flexible framework for building upon and wherever possible its structure has been used and modified to achieve the desired functionality and feel.

#### Core colour scheme
The colour scheme is based on the orange colour of a traditional cigarette's filter in order to inspire familiarity in potential customers who may look to vaping on their road to quitting smoking. 

The 'filter-tip' orange is consistently used as an accent colour against Bootstrap's cool `dark` tones, along with judicious white space.

- ![#343a40](https://via.placeholder.com/15/343a40/000000?text=+) #343a40
- ![#ff7f54](https://via.placeholder.com/15/ff7f54/000000?text=+) #ff7f54 (for dark backgrounds)
- ![#e4714b](https://via.placeholder.com/15/e4714b/000000?text=+) #e4714b (for light backgrounds)

The aim was to provide a solid colour base which could bring the other elements on the site to life, most notably the multi-coloured juice bottles.

#### SVGs

In the planning stages the project was going to use images of existing vape products. However, in order to provide a different overall aesthetic (and in part due to the challenge of sourcing relevant data and images) the decision was made to use an inline SVG which could be varied per product. The result is a broad spectrum of colours which work well to punctuate the otherwise restricted colour palette. 

#### Buttons, Tabs, Pills

The same colours are used as for the core site elements, with variations depending on the action. Affirmative actions (choose, confirm, submit, delete) have a solid dark background with orange hover effects whereas negative actions (back, cancel etc) are indicated an outline which is filled dark on hover. Other splashes of colour are used to highlight important information, such as the pill to show a discount has been applied on an otherwise two-tone page (Boostrap's `warning`). 

#### Hero image

Another SVG has been used for the hero image to compliment the juice bottles. It has been edited to match the site's core colours and a subtle blurring effect applied to evoke clouds of vapor clearing from the silhouette.

#### Icons

Simple icons are used with variations on the core colour scheme. Orange hover effects are used for user feedback, as are Font Awesome `fas` and `far` icons to indicate whether a product is a user favourite or not. On the favourites page itself, `broken-heart` is used to indicate that the product has been removed from favourites. Icons are also used to give context to buttons during the checkout process (`piggy-bank`, `lock`, `times`), some information about nicotine on the product details page, and for the `star` icon on ratings.

#### Shadows
In order to highlight particular areas of interest to the user, some subtle shadowing is used when products are hovered (larger screens only) and also for modals, toasts, product reviews and the add/edit product page (larger screens only). Used sparingly, these effects have impact on an otherwise flat canvas.

#### Fonts

[Raleway](https://fonts.google.com/specimen/Raleway#about) - A hard, slender font used for all the site's headers.

[Karla](https://fonts.google.com/specimen/Karla#about) - A softer font used for everything other than headings. It compliments the rounded edges of the other elements on the site.

#### Bootstrap

The following Bootstrap components have been used:

- [Buttons](https://getbootstrap.com/docs/4.6/components/buttons/)
- [Cards](https://getbootstrap.com/docs/4.6/components/card/)
- [Forms](https://getbootstrap.com/docs/4.6/components/forms/)
- [Modals](https://getbootstrap.com/docs/4.6/components/modal/)
- [Navs](https://getbootstrap.com/docs/4.6/components/navs/)
- [Navbar](https://getbootstrap.com/docs/4.6/components/navbar/)
- [Toasts](https://getbootstrap.com/docs/4.6/components/toasts/)

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

#### Site-wide

**Favourites**

- Users can easily save their favourite juices from any of the product pages, and remove from favourites just as easily
- A heart icon shows whether or not a product is a user favourite (full vs empty). When clicked an ajax request updates the database without reloading the page, providing a more seamless user experience

**Rewards**

- Points are rewarded for various user actions:
  - Registering (100 points)
  - Leaving a review following a verified purchase (5 points)
  - For every £1 spent (1 point)
- They can be redeemed for a discount of 1 penny per point until the order total is zero.
- Points earned for purchases are calculated on the order total after an existing discount has been applied, and before the delivery cost is added on.
- Users can track how they have earned and spent points via their Account Dashboard.

**Navbar**

Consistent on all pages, the navbar provides quick access to all areas of the site.

**Search bar**

The search bar finds juices matching a user's query either by name or from their constituent flavours. If a user knows what they want, this is their route to finding it. The user's search term is displayed once submitted.

**Toasts**

These pop-ups give context to and confirmation of user actions, including error messages, login/out, and success on leaving a review or on checkout. Where appropriate they also show a summarised copy of the shopping cart with a link to review before heading to checkout.

#### Page-specific

**Home**

- Striking hero image draws potential customers in and a simple call to action links straight to the juice products page.
- Trio of action cards invite further exploration of the home page (the brands and flavour categories) and a link to sign up to start receiving rewards.
- Brand section establishes how Moose Juice has separated its product range, gives details about each brand and a link to the respective juices.
- Flavour categories need no more explanation than a bold thumbnail icon which will filter the juices accordingly.

**Products**

- Sort field to order filtered juices by new arrivals, rating or name. The number of matching juices is displayed.
- Product cards show the essential details (name, category, rating and price), with a satisfying box-shadow hover effect.
- SVG used to depict each card, with an endless possibility of colours as chosen by the admin.
- Product rating is shown depicted as a set of stars.
- Product RRP is visible and if on sale this is struck out and replaced by the sale price.

  *Registered users*
- Can add/remove favourites by clicking the heart icon.

  *Super users*
- Those with admin rights get an extra icon which links to the edit product page.

**Product details**

- In addition to the information and functionality of the products page, a product description and list of individual flavour notes is included.
- Flavours link to all other products with the same flavour.
- A form allows users to pick options for the product, as well as the quantity, before submitting and adding the item to their cart.
- Only options available for the brand in question are available.
- Product reviews can be found under the form, including the star rating and whether the review is following a verified purchase.

  *Registered users*
- Have the ability to leave and edit reviews, but not to delete them.

  *Super users*
- Can both edit and delete a juice from the product detail page.
- Can edit and delete any user's review.

**Cart**

**Checkout**

**Checkout success**

**Account dashboard**

**Add/edit product**








**Secure passwords**
When registering for the site, the user's password is hashed so that it is not revealed to the database owner.

**CRUD functionality**

All users can:
- Read all products

Registered users can:
- Create product reviews
- Update product reviews
- Update their delivery details
- Update their list of favourites

Superusers can:
- Frontend:
  - Create, Update and Delete products
  - Create, Update and Delete any product reviews


**Static and image file hosting**

- Static and image files are served from an Amazon S3 Bucket

**Confirm delete**
When the admin clicks to delete a product or review, a modal pops up to confirm they wish to do so to prevent accidental deletion.

**Access protection**

Routes are protected using Django's `@login_required` route decorators to ensure non-super-users cannot interfere with the database.

**404 and 500 error handling**
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
