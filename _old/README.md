<h1 align="center">
   <a href="" target="_blank"><img src="" alt="logo image"/></a>
 </h1>
 
<div align="center">
    
#### Click on image for live version
</div>



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
* Giving education on bees and the honey process.
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


### Validation Using Jigsaw, Validator, Jshint and pep8
| Page                      | Result   | Any Errors                                     |
| :------------             | :------- | :--------------------------------------------- |
| app.py                    | Pass     |  No Errors                                     |




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

Go back to heroku go to settings click reveal config vars, there will be a few things to add here, first setup IP so in the box that says Key type (IP) and in 
the value box type (0.0.0.0) click add then do the same but type (PORT) and set that to (5000) click add. You will also need to add (MONGO_URI) and the (SECRET_KEY) for this information contact You site developer.
#######################################################################################################################################################################################
Once all the steps have been taken, click more top right hand side of page and select restart all dynos the application will now be deployed.

If a message pops up stating there may be some down time until the restart has finished click OK.

Under the settings tab in Heroku, scroll down to domains and your link will be displayed there. It can be used to access the live version of the application.

Deployment: The site will be deployed by 
https://www.heroku.com/


### Credits:

The Blog was a mini project from Code Institute.
The cart, checkout and stripe tutorials from boutique ado, Code Institute




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








