This document is an appendice to the ReadMe file.

### Full Manual Testing 

[Readme](/README.md)

**Test:** Login button takes the user to the login page.

**Result:** Works as intended.

**Test:** afterlogin user is redirected to the landing page

**Result:** Works as intended.

**Test:** Honeypot logo redirects to the home page

**Result:** Works as intended.

**Test:** Clicking on a product opens the product on the info page 

**Result:** Works as intended. 

**Test:** using the quantity buttons to increase or decrese the quantitiy

**Result:** works as intended.

**Test:** Clicking add to cart adds product to cart and the back button takes the user to the product info page.

**Result:** Works as intended. 

**Test:** Clicking create review directs the user to a form to create a review 

**Result:** Works as intended. 

**Test:** The save button saves the form and redirects to the product info, the back buton does the same without saving the form.

**Result:** Works as intended. 

**Test:** The edit and delete buttons are only visible to the user who created them.

**Result:** Works as intended. 

**Test:** The edit review button takes the user to the edit review form and the done button saves the form and redirects the user the the products info page

**Result:** Works as intended. 

**Test:** the delete button deletes the review.

**Result:** Works as intended. 

**Test:** When a product is added to cart a small cart button will apper next to the back button and direct you to the cart.

**Result:** Works as intended. 

**Test:** While in the cart the update button updates quantity and the remove button removes the item from the cart.

**Result:** Works as intended. 

**Test:** the keep browsing button takes the user back to the landing page where the products are.

**Result:** Works as intended. 

**Test:** the secure checkout button takes the user to the checkout

**Result:** Works as intended. 

**Test:** When at the checkout a form is displayed with the full name field highlighted

**Result:** Works as intended. 

**Test:** When filling out the form all required fields give user feedback befoire the form can be submitted

**Result:** Works as intended. 

**Test:** When a product is added to the cart and checkout is entered, with the form filled out and the test card number, then the order submits corectly

**Result:** Works as intended. 

**Test:** Payment with card number 4242 4242 4242 4242 submits an order and stripe says the payment was successful

**Result:** Works as intended. 

**Test:** Payment with card number 4000 0027 6000 3184 stripe askes for authentication in a popup box and on clicking fail a warning message is displayed under the card inputbox

**Result:** Works as intended. 

**Test:** On clicking full authentication the payment is sent succefully

**Result:** Works as intended. 

**Test:** Check if webhook recieved from account.external_account.created from stripe 

**Result:** Recieved Successfully

**Test:** Check if webhook recieved from payment_intent.succeeded

**Result:** Recieved Successfully

**Test:** Check if webhook recieved from payment_intent.payment_failed

**Result:** Recieved Successfully

**Test:** After a succesful purchace the thank you page is displayed with the order details

**Result:** Works as intended. 

**Test:** the blog button at the bottom of the form takes the user to the blog section.

**Result:** Works as intended. 

**Test:** The create blog button and delete is only visible to the super user and not standard user 

**Result:** Works as intended. 

**Test:** The blog cards appear on the page with the read more button

**Result:** Works as intended. 

**Test:** The read more button takes the user to the blog post 

**Result:** Works as intended. 

**Test:** the image and text is displayed and the back to blog button redirects back to blog.

**Result:** Works as intended. 

**Test:** The edit blog button is only visible to the super user and takes them to the edit blog form

**Result:** Works as intended. 

**Test:** the save button saves the form and the back button redirects back to the blogs

**Result:** Works as intended. 

**Test:** The create blog button takes the user to the blog create form. The required fields give feed back, the upload image button opens a local box for selection of images
and the save button saves the form and redirects to the blog. The backbutton redirects to the same place. 

**Result:** Works as intended. 

**Test:** The home button on the navigation bar redirects to home  

**Result:** Works as intended. 

**Test:** On clicking the profile button the user is redirected to the profile page

**Result:** Works as intended.

**Test:** the form on the profile page contains the email and user name and the update button updates the form 

**Result:** Works as intended.

**Test:** The order history is displayed and the oder numbers can be clicked 

**Result:** Works as intended.

**Test:** On clicking the order number the user is taken to the order history page and that order is displayed

**Result:** Works as intended.

**Test:** the blog button redirects to the blog page and the back button takes the user back to the profile page.

**Result:** Works as intended.

**Test:** The blog button on navigation bar redirects to the get blog page 

**Result:** Works as intended. 

**Test:** if logged in, clicking on the users name will give a drop down menu with access to profile and logout

**Result:** Works as intended. 

**Test:** If super user also gives a link to the admin payment_failed

**Result** ***BUG:*** Bug found, if the user has only just logged in, the drop down menu will drop but their admin or profile buttons will not be accessable until the user has clicked on the home button,
then the user can click on all buttons.

**Resolved** It was the case that a Toast was not showing infront of the menu, as I had not included the {{ block.super }} in the script tab so the toast was transparent.

**Test:** the shopping cart icon on the nav bar is empty when it contains no products and the icon changes and a item quantity number appears next to it.

**Result:** Works as intended. 

**Test:** If superuser, when clicking admin in the dropdown navigation menu it will take the user to the admin panel

**Result:** Works as intended. 

**Test:** All products are visible in a table

**Result:** Works as intended. 

**Test:** On clicking on either add product button, the product add form is displayed. All necessary fields give user feedback or the form will not submit, also when clicking on the choose file button a 
box opens so the user can select the image for the product. The add product button saves the form and redirects to the admin panel 

**Result:** Works as intended. 

**Test:** the back button redirects to the admin panel

**Result:** Works as intended. 

**Test:** The to bottom button takes you to the bottom of the page and the to top button takes the user to the top of the page

**Result:** Works as intended. 

**Test:** The update button take the user to the product update form and the done button saves the form and redirects to the admin pannel

**Result:** Works as intended. 

**Test:** All social media icons link to respective sites in separate tabs

**Result:** Works as intended. 

**Test:** Clicking an empty cart will take you to your cart is empty page where the keep browsing button redirects to the landing page

**Result:** Works as intended.

**Test:** The logout button takes you to the logout confirmation page and the logout button logs the user out 

**Result:** Works as intended. 

**Test:** All other features of allauth such as signup, forgot password etc. work as intended

**Result:** Works as intended.

**Test:** Email is sent to the user after signup for confirmation

**Result:** Works as intended.

**Test:** Email confirmations of you order sends

**Result:** Works as intended.
