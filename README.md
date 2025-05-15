# Mollavie

 
- ### Database planning 
<hr>  
  Database Structure     
     
![admin page]()  
-   ### Design
    -  ##  BlockArt Color Scheme

| Element      | Color Code | Description |
|-------------|------------|-------------|
| **Primary** | `#103E26` | Dark Green (Navbar, Buttons, Highlights) |
| **Background** | `#F5F1EA` | Light Beige (Main Content Area) |
| **Accent** | `#D5C4A1` | Muted Gold (Borders, Cards, Shadows) |
| **Text** | `#2D2D2D` | Deep Charcoal (Headings, Body Text) |
| **Secondary** | `#B0302D` | Rich Red (Icons, Hover Effects) |

This color scheme defines the aesthetic of **BlockArt**, giving it a **classic, vintage, and artistic** look! 


- Images  what are used are from mayself and my dother.

   #### Typography

 -   The fonts used are [Open Sans](https://fonts.google.com/specimen/Open+Sans) and [Lato](https://fonts.google.com/specimen/Lato).
   

  ## Wireframe
***

<details open>
<summary>Wireframe - Homepage  </summary>  

![homepage wireframe-mobile & desktop]()
</details> 
<details >
<summary>Wireframe - About page </summary>  

![homepage wireframe-mobile & desktop]()
</details> 
<details>
<summary>Wireframe - New Post</summary>  

![homepage wireframe-mobile & desktop]()
</details>    
<details>
<summary>Wireframe - SignUp page </summary>  

![homepage wireframe-mobile & desktop]()
</details> 
<details>
<summary>Wireframe - Mobile </summary>  

![homepage wireframe-mobile & desktop]()
</details>              



## Agile Development Process

This project was developed using the **Agile methodology** with a **Kanban board** hosted on GitHub Projects.

###  Planning and Workflow

- The development process was broken into **user stories**, representing real user needs and functionality goals.
- Each user story was converted into a GitHub **issue** with acceptance criteria and added to the project board.
- The board was divided into columns:
  - **Backlog** – ideas/features not yet started
  - **To Do** – stories selected for the current sprint
  - **In Progress** – tasks currently being worked on
  - **Review / Testing** – features completed and ready for testing
  - **Done** – completed and deployed features

###  User Stories

User stories were written from the perspective of different users, including:
- Unauthenticated users (browsing, viewing artwork)
- Authenticated users (making purchases, viewing order history)
- The site owner (managing inventory, monitoring sales)

Each story followed the standard format:

> As a [type of user], I want [some goal] so that [some reason].

 All user stories were manually tested and tracked via GitHub issues and commits.

###  Agile Features Summary

| Sprint | Key Features Delivered                                  |
|--------|----------------------------------------------------------|
| 1      | Project setup, user authentication, base templates       |
| 2      | Product model, gallery view, detail page                 |
| 3      | Shopping cart and session-based storage                  |
| 4      | Stripe integration, success page, and order saving       |
| 5      | Order history page, mobile navbar, deployment prep       |

---

 A full list of issues and progress can be viewed on the [GitHub Project Board](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/projects/X).


 ## Technologies Used

### Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)



### Frameworks, Libraries & Programs Used


- [Git](https://git-scm.com/)
  - Version control.
- [GitHub](https://github.com/)
  - For storing code and deploying the site.
- [Gitpod](https://www.gitpod.io/)
  - Used for building and editing my code.
- [Django](https://www.djangoproject.com/)
  - A python based framework that was used to develop the site.
- [Bootstrap](https://getbootstrap.com/)
  - For help designing the html templates.
- [Google Fonts](https://fonts.google.com/)
  - Used to style the website's logo.
- [Font Awesome](https://fontawesome.com/)
  - Used to obtain the icons used.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
  - Used to help fix problem areas and identify bugs.
- [Cloudinary](https://cloudinary.com/)
  - Used to store static files and images.
- [Favicon.io](https://favicon.io/)
  - Used to generate the site's favicon.
- [SQlite](https://www.sqlite.org/index.html)
  - Used when performing unit tests.
- [PostgreSQL](https://www.postgresql.org/)
  - Database used through heroku.
- [Lucidchart](https://www.lucidchart.com/)
  - To draw out the database schema.
- [W3C Markup Validation Service](https://validator.w3.org/) 
  - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
- Used to validate CSS code.
- [Pep8](http://pep8online.com/)
  - Used to validate Python code.
- [JSHint](https://jshint.com/)
  - Used to validate JS code.
- [Tinyjpg](https://tinyjpg.com/)
  - Used to compress images.
- [Convertio](https://convertio.co/)
  - To convert images to a webp format(better performance)
- [Heroku](https://www.heroku.com/)
  - To deploy the project.
- [ChatGPT](https://chatgpt.com/)
  - Used for general queries and quick help.
- [Claude3.5](https://claude.ai/)
  - For insightful explanations of topic. 
- [ YouTube](https://www.youtube.com/) 
  - For tutorials and other learnigs.



## Validators

- HTML
    - Results of HTML official[W3C validator] (https://validator.w3.org/).

    <hr>

| File         | Preview |
|-------------|---------|
| `base.html`  | ![base.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599020/base.html_wug6vn.png) |
| `about.html`   | ![about.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599016/about.html_jpz6b9.png) |
| `post confirm delete.html`   | ![post_confirm_delete.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599034/p_c_delete.html_rfk5mt.png) |
| `post detail.html`  | ![post_detail.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599039/post_dital.html_ibqpmy.png) |
| `post form.html` | ![post_form.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599044/post_form.html_fcg0th.png) |
| `password_reset_complete.html`  | ![password_reset_complete.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599044/post_form.html_fcg0th.png) |


##  HTML Validation

All HTML files were tested using the [W3C Markup Validation Service](https://validator.w3.org/). The results are as follows:

| Page                   | Valid | Errors | Warnings |
|------------------------|:-----:|:------:|:--------:|
| Home                   |    |   0    |    0     |
| About                  |    |   0    |    0     |
| Profile                |    |   0    |    0     |
| Register               |    |   0    |    0     |
| Admin                  |    |   0    |    0     |
| Password Reset         |    |   0    |    0     |
| Login                  |    |   0    |    0     |
| Logout                 |    |   0    |    0     |


  <hr> 

  ##  Custom Error Pages

The Mollavie project includes fully custom-designed error pages to ensure a smooth and branded user experience, even during failures.

### Implemented Errors:

| Code | Description            |
|------|------------------------|
| 403  | Forbidden              |
| 404  | Page Not Found         |
| 500  | Internal Server Error  |

Each template extends the base layout, uses consistent colors and styling, and includes helpful messages and navigation.

---

###  Examples

#### 404 – Page Not Found  
When a user accesses a missing page:

![404 Error Page]()

#### 403 – Forbidden  
When permission is denied (e.g., accessing someone else's post):

![403 Error Page]()

#### 500 – Server Error  
When something unexpected crashes:

![500 Error Page]()

---



#  Testing

##  Table of Contents
- [Device Testing](#device-testing)
- [Browser Compatibility](#browser-compatibility)
- [Manual Testing of User Stories](#manual-testing-of-user-stories)
- [Automated Testing](#automated-testing)

---

##  Device Testing

Tested Mollavie on the following real devices:

| Device | Result | Screenshot |
|--------|--------|------------|
| Samsung Galaxy A52 |  Works as expected | ![Samsung A52]() |
| iPhone 13 Mini     |  WAS                | ![iPhone 13]()    |
| iPad (3rd Gen)     |  WAS                | ![iPad]()              |

---

##  Browser Compatibility

| Browser        | Result | Screenshot |
|----------------|--------|------------|
| Google Chrome  |  WAS | ![Chrome]() |
| Mozilla Firefox|  WAS | ![Firefox]() |
| Microsoft Edge |  WAS | ![Edge]()     |

---

##  Manual Testing of User Stories

### 🔍 As a user, I want to browse and view product details

| Step | Expected Result | Actual Result |
|------|------------------|---------------|
| Navigate to home page | Homepage loads |  WAS |
| Click on “Gallery” | Artwork list appears |  WAS |
| Click on an artwork | Product detail page with image and Buy Now button |  WAS |

---

###  As a user, I want to use the shopping cart

| Step | Expected Result | Actual Result |
|------|------------------|---------------|
| Add artwork to cart | Item added with message |  WAS |
| View cart | All items listed |  WAS |
| Remove item | Item removed with confirmation |  WAS |

---

###  As an authenticated user, I want to buy artwork via Stripe

| Step | Expected Result | Actual Result |
|------|------------------|---------------|
| Click Buy Now | Redirects to Stripe |  WAS |
| Complete payment | Redirects to success page |  WAS |
| Visit /my-orders | Order listed with details |  WAS |

---

###  As a site owner, I want unauthenticated users restricted

| Step | Expected Result | Actual Result |
|------|------------------|---------------|
| Visit /my-orders logged out | Redirect to login |  WAS |

---

###  Form Validation and Flash Messages

| Action | Feedback |
|--------|---------|
| Empty form submission |  Error displayed |
| Valid submission |  Success message shown |

---

##  Automated Testing

- `python manage.py test` run with basic model and view checks
- Stripe tested with test cards like `4242 4242 4242 4242`
- Admin site verified: `/admin` is accessible by superuser

---

## Deployment
This project utilizes [Heroku](http://heroku.com) , for deployment, allowing developers to build, run, and manage applications in the cloud.
Follow these steps to deploy the ArtBlog on Heroku:

1. Create a New Heroku App
- Log in to Heroku or sign up for a new account.
- Navigate to your Heroku dashboard and click on the "New" button.
- Select "Create new app" from the dropdown menu.
- Choose a unique name for your app, select a region (EU or USA), and click "Create app".
2. Configure Environment Variables
- In your app's settings, navigate to the "Config Vars" section.
- Click on "Reveal Config Vars" and add the following variables:
  - PORT: Set the value to 8000.
  - Any other confidential credentials or configuration settings required by the blog.
3. Add Buildpacks
- In the "Buildpacks" section, add the following buildpacks in the specified order:
  - Python
  - Node.js
4. Prepare Required Files
- Ensure your project includes the following files:
  - requirements.txt: Contains the project's Python dependencies.
  - Procfile: Specifies the commands to run the app.
5. Connect GitHub Repository

- Under the "Deploy" tab, select "GitHub" as the deployment method.
- Connect your GitHub repository to the Heroku app.
- Enable automatic deploys for continuous deployment.
6. Deploy Your App
- Trigger a manual deployment by clicking "Deploy Branch" or wait for automatic deployments to occur.
- Once deployed successfully, your blog will be accessible via the provided Heroku URL.




## Deployment

The site was deployed to GitHub Pages. The steps to deploy are as follows:

- In the [GitHub repository](https://github.com/mirjanacale/BlockArt), navigate to the Settings tab
- From the source section drop-down menu, select the **Main** Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found [here](https://mirjanablog-09220d34d6de.herokuapp.com/)

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/mirjanacale/BlockArt)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/mirjanacale/.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/mirjanacale//)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://mirjanacale.github.io//)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no major differences between the local (Gitpod) version and the deployed (GitHub Pages) version that I'm aware of.

## Contributing
Contributions are welcome! If you have suggestions for new questions or improvements to the game, please feel free to open an issue .

 
