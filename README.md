# [Ask Japanese](https://ask-japanese.herokuapp.com/)
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/home-10.JPG)

 Ask Japanese is a restaurant website created to promote the restaurant and make table reservations online.

 
 [Click here](https://ask-japanese.herokuapp.com/) to visit the deployed site.

To access admin
- User: Admin 
- Password: askjapanese123

---

# Table of contents
1. [Owner/Admin Stories](#Owner/admin-Stories)
2. [User Stories](#user-stories)
3. [Structure](#structure)
4. [Features](#features)
    1. [User Features](#user-features)
    2. [Owner/Admin Features](#Owner/Admin-Features)
5. [Technologies Used](#technologies-used)
    1. [Main Tech](#Main-Tech)
    2. [Applications and Platforms](#Applications,-Libraries-and-Platforms)       
6. [Validation](#validation)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Owner/admin Stories

### EPIC 5 - Admin/Site-Owner Functionality
 
#### Admin manage tables 
As an admin I can manage tables so that tables available will be presented

- Acceptance Criteria 1: Admin can create tables and define the size
- Acceptance Criteria 2: Admin can delete tables
- Acceptance Criteria 3: Admin can update table size
#### Admin manage bookings
As an admin I can manage reservations so that are well maintained

- Acceptance Criteria 1: A reservation must include party size, date, and time
- Acceptance Criteria 2: The admin can edit a reservation
- Acceptance Criteria 3: The admin can create and delete reservations

  

## User Stories

### EPIC 1 - Core functionality
#### Purpose of the website

User Story: As a user I can understand the purpose of the website so that I use its features

- Acceptance Criteria 1: User can navigate through the home page
- Acceptance Criteria 2: User can navigate to a contact page
- Acceptance Criteria 3: User can navigate to a book page

### EPIC 2 - The home page
#### Where restaurant is based
User Story: As a user I can find where the restaurant is based so that I can get there
- Acceptance Criteria 1: Location information is found out on the home page and at the footer
- Acceptance Criteria 2: Full address is provided
 #### Restaurant working hours
 User Story: As a user I can find the restaurant opening time so that I know the times I can visit the restaurant

 - Acceptance Criteria 1: User can know the days it's open and closed
 - Acceptance Criteria 2: User can know the times of opening and closing
    
#### Home page
User Story: As a user I can navigate throw the home page so that I get to know the restaurant and its offers

 - Acceptance Criteria 1: User can read an about us section
 -  Acceptance Criteria 2: User can find general information about the restaurant
 - Acceptance Criteria 3: User can navigate to menu, book, contact

### EPIC 3 - The contact page
#### Contact Page
As a user I can contact the restaurant team so that clarify any doubts

- Acceptance Criteria 1: User can input their details and queries
- Acceptance Criteria 3: User details must include: Name, Last Name, Phone Number, Email, and Message
 
#### An automatic reply when contacting restaurant
As a user I can receive an automatic email for me to be sure my message was sent

- Acceptance Criteria 1: Restaurant team will receive user messages through email
- Acceptance Criteria 2: User will receive an automatic reply
- Acceptance Criteria 3: If the form is not valid, show an error to the user

### EPIC 4 - The booking page
 
#### User book a visit
As a user I can make a booking so that I will visit the restaurant for a meal

- Acceptance Criteria 1: A booking must include Full Name, Date, Time, Party Size
- Acceptance Criteria 2: A confirmation message must be displayed to the user
#### Cancel a booking
As a user I can cancel a booking so that I don't need to get in touch with the restaurant

- Acceptance Criteria 1: User can find their booking on the booking page
- Acceptance Criteria 2: User can cancel their booking
- Acceptance Criteria 3: User receives a canceling email confirmation

#### Edit a booking
As a user I can edit my booking so that I postpone or add more people to my booking

- Acceptance Criteria 1: User can find their booking on the booking page
- Acceptance Criteria 2: User can edit their booking
- Acceptance Criteria 3: User receives a new email booking confirmation
#### Automatic email confirmation
As a user I can receive an automatic email so that I will be able to review later on

- Acceptance Criteria 1: User receives an automatic email with full details of their booking

### EPIC 6 - The menu page
#### Menu
As a user I can visit the menu page so that I know the dishes from the restaurant

- Acceptance Criteria 1: Each dish has its own image
- Acceptance Criteria 2: Filter for each menu section
- Acceptance Criteria 3: Menu in a Grid layout

 [Back to Table of contents](#table-of-contents)

## Structure
 ### Wireframes
- [Check the wireframes used to this project](https://github.com/arthurvguide/ask-japanese/blob/main/docs/wireframes/Wireframes.pdf). 

 ### Diagrams
 
 - [Check the diagrams used to this project](https://github.com/arthurvguide/ask-japanese/tree/main/docs/diagrams). 

  [Back to Table of contents](#table-of-contents)

## Features
#### User Features
- User can book a table at the restaurant
- User can cancel the booking
- User can edit the booking
- User can view the restaurant menu
- User can contact the restaurant using a contact form
- User receives an booking confirmation by email

#### Owner/Admin Features
- Admin can create tables
- Admin can delete tables
- Admin can manage bookings
- Admin receives the contact form by email
 

## Future Features
- User will be able to place a order online.


 [Back to Table of contents](#table-of-contents)
## Technologies Used

### Main Tech
 - [Django](https://www.djangoproject.com/) 
 - [Java Script](https://www.javascript.com/)
 - [Bootstrap](https://getbootstrap.com/)


### Applications, Libraries and Platforms
This project is built solely through the framework Django, and I have tried to make use of its many powerfiul features.


- JQuery for datetimepicker.

- Font Awesome fonts were used for all icons in this project.

- Google Fonts - Were used for all fonts and icons in this project.

- Git - Version control system used to commit and push to Github via Gitpod.

- Github - The projects repository and all its branches were commited, and pushed to Github.

- Heroku - Used to deploy the application.

- Gitpod - All code was written and tested with the Gitpod web-based IDE.

- Balsamiq Wireframes was used to create wireframe images of the website which you can view here.

- Lucidchart was used to create the visual data schema of the project.

- CLoudinary - to host all images used.


[Back to Table of contents](#table-of-contents)

## Validation
 - Python files are clear of any errors, validated by PEP8 
 - HTML and CSS was validated, clear of any errors
 - JavaScript files was validated by JSHINT, no errors found

 - [Click here](https://github.com/arthurvguide/ask-japanese/tree/main/docs/validations).

## Testing
 

 [Back to Table of contents](#table-of-contents)

## Deployment
### Forking the GitHub Repository
To make a clone, or 'Fork' this repository, follow the steps below.

    1. Access your GitHub account and find the relevant repository.
    2. Click on 'Fork' on the top right of the page.
    3. You will find a copy of the repository in your own Github account.
### Making a Local Clone
    1. Access your GitHub account and find the relevant repository.
    2. Click the 'Code' button next to 'Add file'.
    3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
    4. Open Git Bash.
    5. Access the directory you want the clone to be have.
    6. In your IDE's terminal type 'git clone' and the paste the URL you copied.
    7. Press Enter.
    8. You now have a local clone.

### Heroku

This application has been deployed from Github using Heroku. Here's how:

    1. Create an account at heroku.com
    2. Create a new app, add app name and your region
    3. Click on create app
    4. Go to "Settings"
    5. Under Config Vars, add your sensitive data (creds.json for example)
    6. For this project, I set buildpacks to and in that order.
    7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
    8. Enter your repository name and click on it when it shows below
    9. Choose the branch you want to buid your app from

Any question about how to set up your ide is here. Credits to Code Institute:

- [Click here](https://github.com/arthurvguide/ask-japanese/blob/main/docs/django-cheat/Django%20Blog%20Cheat%20Sheet%20v1.pdf). 

 [Back to Table of contents](#table-of-contents)

## Credits

#### Content
 * All content was written by me.

#### Media
 * Website logo was made by me.

 * All images came from [Unsplash](https://unsplash.com/.).

[Back to Table of contents](#table-of-contents)

## Screenshots

### Home Page
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/home-10.JPG)
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/home%201.png)
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/home%202.png)

### Menu
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/Menu%201.png)

### Book
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/booking%201.png)
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/booking.cancel.png)
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/edit.JPG)

### Contact 
![](https://github.com/arthurvguide/ask-japanese/blob/main/docs/screenshots/contact%202.png)

[Back to Table of contents](#table-of-contents)