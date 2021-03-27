
# ArtWitch - handmade with love!

This web app represents a 4th milestone project for Code Institute's Fullstack Web Developer course.
This app will also be used as real world e-commerce web site later on by my friend who decided to venture into business of selling handmade products online.
My idea was to bulid basic e-commerce site with all of the needed functionality which can later be customized with different design layouts and user interface.





# USER STORIES

## Searching and buying


    - As as shopper I want to view list of products by categories.

    - As a shopper I want to be able search for specific product.

    - As a shopper I want to see product's details(price, picture, description, size and rating).
    
    - As a shopper I want to be able to put product in shopping cart so that I can pay for it and have it delivered.

    - As a shopper I want to see total sum for payment in my shopping cart.

    - As a shopper I want to be able to remove product from shopping cart.

    - As a shopper I want to be able to pay for product easyly(card payment and paypal/stripe).

    - As a shopper I want to be able to leave review and rating for product.

    - As a shopper I want to recive an email confirmation of my order.

    - As a shopper I want to be able to order product without registering.

## Creating and managing user account

    - As a shopper I want to be able to register for a account with my email address and/or social media account.

    - As a shopper I want to get email confirmation that my account was created.

    - As a shopper I want to easly Log in/ Log out.

    - As a shopper I want to be able to retrive new password in case I forget it.

    - As a shopper I want to add/remove and save my prefered payment method.

    - As a shopper I want to able to change my account details (email address, payment methods, username).

    - As a shopper I want to see history of my orders and transactions.

    - As a shopper I want to be able to add/remove/edit my delivery address.

## Design

    In designing this e-commerce app I was aiming for a simple rudimentary design witch can be easly customizable later on. I knew designing backend would be major challenge 
and that I would have design talks with friend for whom this web app is intended. Therefor my main focu was app functionality.
    I used Figma to create mockups which are hosted in github reository in Mockups folder.

### Colours

- I was aiming for clean and simple design guided by Butique Ado lessons. Simple black and white design with blue in deliveri banner and green "back-to-shopping" button.


### Fonts

- [**Lobster**](https://fonts.google.com/specimen/Lobster) - I used this font on landing page(for logo text) and around different views to give unfied feel for visitors.


### Mockups
 I created mockups for desktop primary and used Bootstrap to make them responsive for mobile. They can be found in [Mockups folder]().

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) - This was used for the overall structure of the website.

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - This was used for the overall styling of elements on the website.

- [Bootstrap](https://getbootstrap.com/docs/)- Used for styling and layout of the site.

- [Bootstrap Icons](https://icons.getbootstrap.com/) - Used for all icons in web app.

- [Python](https://www.python.org/) - This was used for all the backend coding of the website. Also, I used many Python libraries which are listed in requirements.txt.

- [Django](https://www.djangoproject.com/) - Web framework used as main architecture for the site following MVT priciples.

- [Google Fonts](https://fonts.google.com/) - Used for fonts across site.

- [GitHub](https://github.com/) - It was used for version controll.

- [Amazon Web Services](https://aws.amazon.com/) - used to host images for the e-shop.

- [Stripe](https://stripe.com) - used for secure and easy payment.

- [Heroku](https://www.heroku.com/) - I used Heroku to deploy the live version of my site.

- [Figma](https://www.figma.com/)** - used for mockup.

- [Visual Studio Code](https://code.visualstudio.com/) - used this to write the code for my site.


## Features

### Existing Features

- **Registration/ login/logout**

    - This is where user can register account. I used Django Allauth for all matters related to user authentication.
    
    - User is required real email address for registration and account confirmation

  - **Profile Features**
    
        - User can  update their  payment and delivery information.

        - Superuser/store owner user can add products, edit products and delete products.
          Superuser can also edit database and see all of orders made on site.

        - User can see all of orders that they made with product quatity and price.

- **Search feature**

        - here user can search products by name and description.

        - user can also sort product by category, price and rating.

- **Navigation** 

    - here user can easly navigate site and browse products by category, rating or price.

- **Shopping bag**

        - user can add, remove products to/from shopping bag. Bag displays quantity, size, individual and total price of 
          products. Also it calculates delivery costs.
        
        - from bag user can access secure checkout for payment.
    
- **Secure checkout**

        - here user can pay for order in secure and easy way using Stripe payment system.

### Features to be implemented at later date

- **Rating system**

        - Implement rating system for all products.

- **Review system**

    - implement written review system to compliment rating system.

## Testing

* **Automated testing**

    * **[CSS Validator](http://jigsaw.w3.org/css-validator/)** - found parse error related to bootstrap 5..

    * **[HTML Validator](https://validator.w3.org/)** - gave errors in navbar that list item can't be child of div element. Remains to be fixed in future. Not a DOM flow braking.

    * **[PEP8]**(http://pep8online.com) - found 'line too long errors in settings.py file taken from Django. Not fixed since it's not app breaking.

* **Manual Testing**

    * **Desktop**
        
        * **Google Chome**: everything is working good. Page loads, and all of the page features are working.

        * **Mozilla Firefox**: everything is working good. Page loads, and all of the page features are working.
        

    * **Mobile**

        * **Mozilla Firefox Dev Tools**

            * tested with Firefox Dev tools for all available devices (from Moto G4 to iPad),
            webpage works well. It is responsive as intended, no weird page deformations.

        **Real-world testing:**

        * **Huawei P20Pro** - site loads good. It is responsive as intended. All of the features are working.

        * **Samsung Galaxy S9** - site loads good. It is responsive as intended. All of the features are working.

        * **Samsung Galaxy A5** - site loads good. It is responsive as intended. All of the features are working.

        * **Xiaomi mi 9t** - site loads good. It is responsive as intended. All of the features are working.


## Deployment

 **[GitHub](https://github.com/)** - is used to host code and files for this project. The project has only one branch(master). Deployed version is most current version of repository.

 **[Heroku](https://www.heroku.com/)** -  was used to deploy this site.

 **How to run this project locally**
 **To clone this project from GitHub:** 
([Source](https://github.com/Edb83/penny-for-your-thoughts/blob/master/README.md#testing))

* Under the repository name, click "Clone or download".
* In the Clone with HTTPs section, copy the clone URL for the repository.
* In your local IDE open Git Bash.
* Change the current working directory to the location where you want the cloned directory to be made.
* Type git clone, and then paste the URL you copied in Step 3.
* Press Enter. Your local clone will be created.

**Some Issues I ran into developing with VS Code:**
- if you need to run venv in terminal:
	- go to .venv/scripts/activate.ps1 to activate venv in terminal


- loading data from fixtures in VS code created lot of errors(UTF encoding issue) but managed to fix them after long nights.

## Media

- Some of the photos of products are taken from Etsy.com just as placeholders until shop owner creates and photographs enough of their own producs.

- Home page background photo was take from [pexels.com](https://www.pexels.com).

## Credits

- Chris for exelent lesson in CI course. His code is backbone of project upon I built my very small contribution.

