<h1 align="center">
   <a href="" target="_blank"><img src="" alt="logo image"/></a>
 </h1>
 
<div align="center">
    
#### Click on image for live version
</div>

The Honey pot is a site for people passionate about good quality natural bee products, whether its honey or furiture polish, with the ability to 
purchase products they have never tried before such as bees wax food wraps, or beeswax soap.

The User has the ability to create edit and delete their own reviews on products as well as find out what is happening on the apiary with the bees. 
The Superuser is the only user that has full create update delete abilities with the products and blogs.



#### The users goals of this website are:
* Easy to navigate. 
* able to login.
* view there profile and previouse orders.
* Read the blog to keep upto date with what the bees are doing

#### The Admin goals of this website are:
* Easy to navigate. 
* Able to login.
* View there product list.
* Create new products.
* View there produts.
* Update ther products.
* Delete Products.
* Create, update & delete there blog posts

#### The Business potentials of this website are:
* Selling advertising space to businesses with bee related products.
* Stock more products and training courses on beekeeping.


#### Visitors to this website are searching for:
* Infomation on Honey bees and honey.
* Ability to learn about where there honey comes from.


#### This Website is the best way to help them achieve these things because:
* Other websites are too cluttered and hard to navigate.
* The user is able to create a login.
* The user can see there profile.
* The user can see their past order history.
* The site owner/admin can create, update, delete products.


#### This website is:
* Providing clear artwork and details of each product.


## Features:
* 


 

#### Home





### Nice to have: 
These features may be included in future releases of this application.
* 



### Technology’s used will include:
[HTML5](https://en.wikipedia.org/wiki/HTML5), [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets), [Bootstrap](https://getbootstrap.com/), [Javascript](https://en.wikipedia.org/wiki/JavaScript), [Python3](https://www.python.org/),  [Gitpod](https://www.gitpod.io/), [Sublime text](https://www.sublimetext.com/), [Balsamiq Mockup 3](https://balsamiq.com/wireframes/desktop/), [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html?gclid=EAIaIQobChMIzNru2Myo6AIVF-DtCh28Fgn0EAAYASAAEgKkdvD_BwE&sdid=88X75SKR&mv=search&ef_id=EAIaIQobChMIzNru2Myo6AIVF-DtCh28Fgn0EAAYASAAEgKkdvD_BwE:G:s&s_kwcid=AL!3085!3!394411736356!e!!g!!photoshop)
 and [Heroku](https://www.heroku.com/).


## WireFrame Mockups:
#### Desktop View:
- [Home]



#### Mobile & Tablet View:
- [Mobile Login]
- [Tablet Login]


![Am I Responsive]

## Screen Shots:
#### Mobile & Tablet View:
- [Desktop]
- [Desktop]
- [Desktop]
- [Desktop]
- [Mobile]
- [Tablet]
- [Tablet]


 
## cansAndBottleInfo

| Field         | Type     | Description                                |
| :------------ | :------- | :----------------------------------------- |
| \_id          | ObjectId | ID is auto-created by MongoDB              |
| name          | String   | Name of beer                               |




## users

| Field         | Type     | Description                                |
| :------------ | :------- | :----------------------------------------- |
| \_id          | ObjectId | ID is auto-created by MongoDB              |




## Defensive Design




## Testing:
**Test:** Check if webhook recieved from account.external_account.created from stripe 

**Result:** Recieved Successfully

**Test:** Check if webhook recieved from payment_intent.succeeded

**Result:** Recieved Successfully

**Test:** Check if webhook recieved from payment_intent.payment_failed

**Result:** Recieved Successfully

## Bugs & ongoign fixes
* On the chrispy forms image input i have yet to find a way to style it in the next release i will have styled these buttons also.
* The sign up form atomatically auto focuses on user name instead of email.
* the product admin page on smaller screens is not quite a contrained as i would prefer however it does not affect the usabillity of the page just rather athetics.



### Validation Using Jigsaw, Validator, Jshint and pep8
| Page                      | Result   | Any Errors                                     |
| :------------             | :------- | :--------------------------------------------- |
| index.html                | Pass     |  No Errors                                     |
| product_info.html         | Pass     |  No Errors                                     |
| create_review.html        | Pass     |  No Errors                                     |
| edit_review.html          | Pass     |  No Errors                                     |
| cart.html                 | Pass     |  No Errors                                     |
| checkout.html             | Pass     |  No Errors                                     |
| order_history.html        | Pass     |  No Errors                                     |
| checkout.html             | Pass     |  No Errors                                     |
| checkout_success.html     | Pass     |  No Errors                                     |
| user_profile.html         | Pass     |  1 Error was using action instead of type      |
| blogposts.html            | Pass     |  No Errors                                     |
| blogpostsform.html        | Pass     |  No Errors                                     |
| blogdetail.html           | Pass     |  No Errors                                     |
| blog.css                  | Pass     |  No Errors                                     |
| checkout.css              | Pass     |  No Errors                                     |
| cart.css                  | Pass     |  No Errors                                     |
| products.css              | Pass     |  1 Error was using -webkit-center              |
| profiles.css              | Pass     |  No Errors                                     |
| review.css                | Pass     |  No Errors                                     |
| bass.css                  | Pass     |  No Errors                                     |



### Cross Browser Compatibility
Tested on four Browsers
* Chrome    
* Opera     
* Firefox   
* Edge      



### Deployment:
##### To deploy this page to Heroku from its GitHub repository:

Log into GitHub.
Then clone this project from GitHub:

Follow this link to the Project's GitHub repository https://github.com/jonathanw82/the-honey-pot
Under the repository name, click "Clone or download".
Select clone with HTTPs, copy the clone URL for the repository.

In your local IDE open Git Bash Terminal.
Change the current working directory to the location where you want the cloned directory to be made.
Type git clone, and then paste the URL you copied earlier.
(git clone "https://github.com/jonathanw82/the-honey-pot")
Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

##### Forking the repository.
If you would like to take a copy of this repository in its current state, this can be done by forking.

Follow this link to the Project's GitHub repository https://github.com/jonathanw82/the-honey-pot

From the menu items near the top of the page, select Fork.
On doing so the repository will be added to your own gitHub account. From there you can follow the deployment 
details as stated below. You will also be able to make any changes you require that will not affect the 
original master from the original repository.


##### How to deploy from Heroku
To deploy from Heroku, first sign up to do this go to https://www.heroku.com/
and click the sign up button on right hand side and fill out the form to create a new account,then select Python as the development language. 

At this point you will be sent a confirmation email, once the link in the email has been clicked you will be prompted to input a password and the account will be set up.

Once all setup and logged in, click on the create new app button, then give your project a name using hyphens instead of spaces. The name has to be unique as 
Heroku has thousands of apps and they cannot have the same name, select your region and select create app.

You will then be presented with a dashboard with listings of command lines for use in a bash command line.

From your workspace of choice open the command line and install Heroku depending on workspace, type (pip3 install heroku) once installed, type (heroku login -I)
then enter your email and password you set Heroku up with. It will then state you are logged in. 

We will now need to push our files to Heroku to be deployed or our live version.

To do this in Heroku go to the app you created earlier then select deploy, under app information you will see Heroku git URL copy the url, in the bash 
command line in the work space of choice type (heroku git:remote –a <app_name>) at this point you need to push all your data up to Heroku.

To do this from your git bash command line type (git add .) then (git commit –m “deploy to heroku”) then (git push –u heroku master ) this will take a few minutes to push all the data to 
Heroku. 

We then need to setup a web process to do this at the command prompt type (heroku ps:scale web=1) after this our web process will be running we will now need to set up some 
config Vars in heroku.

Go back to heroku go to settings click reveal config vars, there will be a few things to add here, first we will setup the email:
* In the Key box enter EMAIL_HOST_USER the value thehoneypotms4@gmail.com
* In the Key box enter EMAIL_HOST_PASS the value key can be obtained from your developer

Then To setup Stripe for payments
* In the Key box enter SECRET_KEY the value key can be obtained from your developer
* In the Key box STRIPE_PUBLIC_KEY the value key can be obtained from your developer
* In the Key box STRIPE_SECRET_KEY the value key can be obtained from your developer
* In the Key box STRIPE_WH_KEY the value key can be obtained from your developer

Then Amazon Web Service
* In the Key box AWS_ACCESS_KEY_ID the value key can be obtained from the info about Amazon web service below
* In the Key box AWS_SECRET_ACCESS_KEY the value key can be obtained from the info about Amazon web service below
* In the Key box AWS_STORAGE_BUCKET_NAME the value key can be obtained from the info about Amazon web service below

Then the Database 
* In the key box DATABASE_URL the value key can be obtained from your developer

Once all the steps have been taken, click more top right hand side of page and select restart all dynos the application will now be deployed.
If a message pops up stating there may be some down time until the restart has finished click OK.
Under the settings tab in Heroku, scroll down to domains and your link will be displayed there. It can be used to access the live version of the application.

Deployment: The site will be deployed by 
https://www.heroku.com/

### How to deploy from Amazon Web Services

First we need to sign up to AWS (Amazon Web Service) to host all our images, when you first sign up this can take a couple of hours to get working.
When signed up login and in the dashboard search s3 then click create bucket 
Give the bucket a name in this case (the-honey-pot), 
Select your region, 
Then uncheck the block all public access as the bucket needs to be public and then after click acknowledge.
Then create bucket
Click on the name of the bucket you have made, click permissions, then bucket policy, at the bottom of the page click policy generator but right click the mouse 
to open it in another tab as not to go away from the page you are currently on.
Go to the next tab ,
In the security type of policy, select s3 bucket Policy, effect leave on allow,
In the principle box jut type a star symbol *, In action select get object.
Just under that select box you will need to paste in the amazon resource name, 
Next select the previous tab without closing in the one you are on copy the amazon resource name details down that are at the end of the buck policy 
editor arn arn:aws:s3:::the-honey-pot make sure there are no full stops or quotes, go back to the policy generator tab and past it in to the amazon resource name box and put a forward slash and a star at the end arn:aws:s3:::the-honey-pot /* 
Click add statement then the generate polices button, a window will pop up, with some lines of code copy all the code from the box, then past it in on 
the bucket policy editor below where you found the amazon resource name details.
Click save 
Then click the over view tab, then create folder, create a folder and call it media.
Leave all the settings below as none and click save.
At this point it is advised to upload a sample image into that folder, click on the folder and press the upload button, select an image and upload. 
Once uploaded click on the image and a box will appear to the right, in the section overview find object url click the link if the image appears the setup is correct.
At this point at the top right of the page there is a bell symbol to their right of it is a dropdown menu click and select my security credentials , 
once on that page click access keys 
Then click the button create new access key, at this point a box will pop up with a  2 keys ID and secret key take note of both I would advise clicking 
the download button and saving an excel file containing  the keys. 
It is of upmost importance NOBODY else sees these keys they are a high security key, failure to day so could compromise security of your website and you 
could leave you with extremely large bills form Amazon.
For where to place these secure keys please refer to deploy with Heroku above. 



### Credits:

The cart, checkout and stripe tutorials from boutique ado, Code Institute.




##### Media:
The Photos used in this site were obtained from

favicon.ioc
http://clipart-library.com/clipart/8TG9rrqTa.htm
Honey Pot Images #1191196

Moving letters
https://tobiasahlin.com/moving-letters/#2

images

product images of jars on a wedding table.
http://www.cassidycarsonphotography.com/

candle and flower
Image by Lolame from Pixabay 

owel canddles
vimar 211821178

Adobestock
laveder soap
343003179 aprilante

wax polish
Amazon

Aipeiry
Okssi 163828907

Repository Image 








