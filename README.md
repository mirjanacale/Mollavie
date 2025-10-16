# Mollavie


<div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748204215/firstimg_kugk4c.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748204215/firstimg_kugk4c.png" alt="base.html validation screenshot" width="800" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>


A modern, accessible Django-based art shop for unique artworks.
Mollavie is a Django-based e-commerce platform designed to showcase and sell original artworks and prints. The site features a user-friendly interface, responsive design, and robust functionality for both customers and administrators. Mollavie supports user registration, product browsing, shopping cart management, and secure checkout with Stripe integration.

---

## Business Model

Mollavie is a business-to-consumer  e-commerce platform that sells original artwork directly to customers. The business model is built around providing a curated experience for art collectors and design-focused buyers.

### Revenue Stream
- Direct sale of original art pieces through Stripe payment integration.
- No commission or marketplace model — Mollavie sells only Mirjana’s artwork.

### Target Audience
- Art collectors
- Home and office decorators
- Online art enthusiasts
- Interior designers looking for bespoke pieces

### Unique Selling Points (USP)
- Hand-crafted, original artwork
- Direct connection with the artist (no middleman)
- High-quality visual previews of paintings
- Simple checkout and delivery system

### Future Expansion (optional ideas)
- Commission-based custom orders
- User reviews and artwork ratings
- Artist spotlight section or blog

## Role-Based Authorization

- Only superusers (admin) can access the Django admin interface to manage products, orders, and users.
- Regular users are restricted from accessing admin-only features or pages.
- Direct URL access to restricted views (e.g., /admin/) redirects unauthorized user

## Features

- Browse original art and prints with responsive design.
- User registration, login and profile management.
- Shopping cart and checkout with Stripe integration.
- Orders created **only after successful payment**; cancelled payments automatically return stock and discard unpaid orders.
- Staff‑only dashboard for adding, editing and deleting products and categories.
- Category filter buttons on the Gallery page.
- Custom 400/403/404/500 error pages.
- Admin panel (superuser) for managing all models.
- Newsletter signup form in the footer (stores unique emails).

- **Category filtering** – the gallery page now shows filter buttons for each category (e.g., *Abstract*, *Landscape*, *Portrait*).  Users can click a category to see only the artworks in that category.
- **Staff admin dashboard** – added a secure `/admin-dashboard/` page.  Staff users (`is_staff=True`) can view, add, edit, and delete products and categories in a friendly interface.  Non‑staff users receive a 403 Forbidden response.
- **Improved payment flow** – orders are now created **only after** Stripe confirms payment.  Cancelling or abandoning the payment on Stripe automatically returns the product to stock and deletes any unpaid order.



## Table of Contents
- [Business Model](#business-model)
- [Features](#features)
- [Database Planning](#database-planning)
- [Design](#design)
- [Wireframes](#wireframes)
- [Agile Development Process](#agile-development-process)
- [Technologies Used](#technologies-used)
- [Lighthouse Scores](#lighthouse-scores)
- [HTML Validation Results](#html-validation-results)
- [Testing](#testing)
- [Error Handling](#error-handling)
- [Future Features](#future-features)
- [References](#references)
- [Bug Fixes](#bug-fixes)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)


### Database Planning

The database is designed to support unique products, user profiles, orders, and testimonials. See the admin page for a visual overview:


<div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748197772/database_hux1p4.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748197772/database_hux1p4.png" alt="base.html validation screenshot" width="500" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>



### Design

#### Mollavie Color Scheme

| Element      | Color Code  | Description                                 |
|--------------|-------------|---------------------------------------------|
| **Primary**  | `#18a085`   | Teal Green (Navbar, Footer, Buttons)        |
| **Background** | `#fafafa`  | Light Gray (Main Content Area)              |
| **Accent**   | `#c0392b`   | Strong Red (Buttons, Highlights)            |
| **Text**     | `#895332f2` | Brownish (Body Text)                        |
| **Heading**  | `#222`      | Dark Gray (Headings)                        |
| **Link**     | `#0056b3`   | Blue (Links)                                |
| **Button Hover** | `#003f8a`| Dark Blue (Button Hover)                    |
| **Card Border** | `#ddd`    | Light Gray (Card/Image Borders)             |

This table reflects the actual colors used in the current CSS for Mollavie.

- All images used are original, from myself and my daughter.

#### Typography

The fonts used are [Open Sans](https://fonts.google.com/specimen/Open+Sans) and [Lato](https://fonts.google.com/specimen/Lato) for a clean, modern, and readable appearance.


##  Digital Marketing

To meet the digital marketing criteria, I’ve included realistic mockups of my online artist presence on both **Facebook** and **Instagram**, showcasing how I promote and brand my *Mollavie Art* business online.

###  Facebook Business Page (Mockups)

I created a **Facebook business page mockup** that displays my branding, including a professional profile picture, a cover photo featuring my artwork, and recent post previews of my original paintings.


 <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748443203/Screenshot_2025-05-28_153753_rnlvwt.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748443203/Screenshot_2025-05-28_153753_rnlvwt.png" alt="chart.html validation screenshot" width="300" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>

  
<div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748442920/mockuper_zkfnns.jpg" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748442920/mockuper_zkfnns.jpg" alt="Facebook page mockup screenshot" width="300" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>


These mockups simulate how I would use Facebook to:

- Reach a wider audience through posts, events, or ads  
- Cross-promote my Etsy and Instagram  
- Build credibility as a professional artist  

###  Instagram Business Account

Alongside the Facebook mockups, I also maintain a real **Instagram business account** where I actively share visual stories and promote my artwork:

- [Instagram: @moly.art083](https://www.instagram.com/moly.art083/)
- [Etsy Shop](https://mollavie.etsy.com)

My Instagram strategy focuses on:

- High-impact visuals of original paintings  
- Behind-the-scenes content and Reels  
- Direct connection with art lovers and potential buyers  

---

###  Summary

These platforms support the **brand presence and discoverability** of *Mollavie Art*, fulfilling the digital marketing objective of the Full-Stack Toolkit. They demonstrate both the potential and the practice of marketing artwork through modern platforms.


##  Newsletter Signup

To support user engagement and digital marketing goals, *Mollavie Art* includes a fully functional newsletter signup form.

###  Technical Overview

- **Location**: Available on every page in the footer (`base.html`)
- **Model**: `NewsletterSubscriber` model stores unique email addresses
- **Validation**: Prevents duplicate signups using Django's ORM
- **Feedback**: Users receive success or info messages using Django's `messages` framework

###  Why It Matters

This feature demonstrates the ability to:

- Collect user data for future email marketing
- Apply form handling and model logic securely
- Integrate consistent user experience elements (UX)

The setup is ready for integration with a tool like **Mailchimp** or **SendGrid** in the future.



  ## Wireframes

Below are wireframes for each major feature/page of Mollavie. These illustrate the layout and user flow, helping guide the design and development process. (Replace image links with your actual wireframes as needed.)

<details open>
<summary><strong>Homepage</strong></summary>

- **Purpose:** Welcomes users, highlights featured artworks, and provides navigation to other sections.
- ![Homepage Wireframe](https://res.cloudinary.com/dyemjyefz/image/upload/v1748284763/image_8_rviaeg.png)
</details>

<details>
<summary><strong>Gallery</strong></summary>

- **Purpose:** Displays all available artworks in a grid, each with image, name, and short description.
- ![Gallery Wireframe](https://res.cloudinary.com/dyemjyefz/image/upload/v1748284752/image_11_qq7ggt.png)
</details>

<details>
<summary><strong>Product Detail</strong></summary>

- **Purpose:** Shows detailed information about a selected artwork, including image, description, and purchase option.
- ![Product Detail Wireframe](https://res.cloudinary.com/dyemjyefz/image/upload/v1748284730/image_12_ycsfla.png)
</details>

<details>
<summary><strong>Cart</strong></summary>

- **Purpose:** Lists selected artworks for purchase, allows removal, and proceeds to checkout.
- ![Cart Wireframe](https://res.cloudinary.com/dyemjyefz/image/upload/v1748284748/image_10_c84y74.png)
</details>

<details>
<summary><strong>Checkout</strong></summary>

- **Purpose:** Collects user details and payment information to complete the purchase.
- ![Checkout Wireframe](https://res.cloudinary.com/dyemjyefz/image/upload/v1748284717/image_14_o51kwg.png)
</details>

<details>
<summary><strong>Profile</strong></summary>

- **Purpose:** Allows users to view and edit their personal information and see order history.
- ![Profile Wireframe](https://res.cloudinary.com/dyemjyefz/image/upload/v1748284705/image_15_pyazyi.png)
</details>

<details>
<summary><strong>Signup / Login</strong></summary>

- **Purpose:** Enables users to create an account or log in to access personalized features.
- ![Signup Wireframe](https://res.cloudinary.com/dyemjyefz/image/upload/v1748284705/image_15_pyazyi.png)
- ![Login Wireframe](https://res.cloudinary.com/dyemjyefz/image/upload/v1748284717/image_14_o51kwg.png)
</details>


---

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


 All user stories were manually tested and tracked via GitHub issues and commits.

###  Agile Features Summary

| Sprint | Key Features Delivered |
|--------|------------------------|
| 1      | Project setup, user authentication, base templates, custom error pages |
| 2      | Product and category models, admin interface, gallery and product detail views |
| 3      | Shopping cart, add-to-cart, remove-from-cart, and checkout functionality |
| 4      | Stripe payment integration, order saving, order history, and profile management |
| 5      | Testimonials, custom 404/403/500 pages, HTML/CSS validation, accessibility improvements |
| 6      | Responsive design, gallery image enhancements, validator documentation, deployment to Heroku |

Each sprint focused on delivering user value, iterating on feedback, and ensuring the site is robust, accessible, and visually appealing. Features were tracked and reviewed using GitHub Projects and Issues for transparency and continuous improvement.
  

###  Resubmission Updates

During the resubmission phase, two new user stories were added to address assessment feedback and improve the overall functionality and user experience of the site.

| Feature | Description | Sprint |
|----------|--------------|---------|
|  **Favorites System** | Logged-in users can now add or remove artworks from their personal favorites list. The button dynamically toggles between  and  depending on the favorite status. This feature enhances personalization and user engagement. | 7 |
|  **Category Filtering** | Artworks are now organized by category, allowing users to browse and explore pieces by artistic style or type. Categories are displayed on the artwork detail page and managed through the admin dashboard. | 8 |

Both features were implemented, tested, and tracked using the GitHub Project Board to demonstrate iterative Agile development and responsiveness to assessment feedback.
  
| **Admin Role Access** | Added `is_staff` restrictions to the admin dashboard and product/category management views. Only staff members can perform CRUD actions. | 9 |

---

 A full list of issues and progress can be viewed on the [GitHub Project Board](https://github.com/users/mirjanacale/projects/11).


## CRUD Functionality

- **Create**: Users can register and create an account.
- **Read**: Users can view products and their profile information.
- **Update**: Users can edit their profile and cart.
- **Delete**: Users can delete their account from the profile page via a “Delete My Account” button.



 ## Technologies Used

- **HTML5**
- **CSS3**
- **JavaScript**
- **Python**
- **Django**
- **Bootstrap**
- **Cloudinary**
- **Stripe**
- **Heroku**
- **Git & GitHub**
- **Balsamiq** 
- **Visual Studio Code**
- **PostgreSQL**
- **Django Debug Toolbar**
- **Django Allauth** 
- **Django Crispy Forms** 
- **Django Messages Framework** 
- **Django Stripe** 
- **WhyNoPadlock.com** 

Other tools: Google Fonts, Font Awesome, Lucidchart, W3C Validators, Pep8, JSHint, Tinyjpg, Convertio.

##
<hr>


## Lighthouse Scores

Lighthouse testing was carried out using the [Chrome DevTools](https://developers.google.com/web/tools/lighthouse/).


  <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748196665/preformace_lhc9ad.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748196665/preformace_lhc9ad.png" alt="chart.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>

   <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748196672/performance3_lcjmq3.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748196672/performance3_lcjmq3.png" alt="chart.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>
  
   <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748196655/asesebiliti4_gqj9mz.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748196655/asesebiliti4_gqj9mz.png" alt="chart.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>

##  HTML Validation Results

All HTML files were tested using the [W3C Markup Validation Service](https://validator.w3.org/). The results are as follows:

| Page            | Valid | Errors | Warnings |
|-----------------|:-----:|:------:|:--------:|
| Home            |  ✔️   |   0    |    0     |
| Gallery         |  ✔️   |   0    |    0     |
| Product Detail  |  ✔️   |   0    |    0     |
| Cart            |  ✔️   |   0    |    0     |
| Checkout        |  ✔️   |   0    |    0     |
| Profile         |  ✔️   |   0    |    0     |
| Register        |  ✔️   |   0    |    0     |
| Login           |  ✔️   |   0    |    0     |
| Testimonials    |  ✔️   |   0    |    0     |
| My Orders       |  ✔️   |   0    |    0     |
| Edit Profile    |  ✔️   |   0    |    0     |
| 404 Error       |  ✔️   |   0    |    0     |


## Validators

- **HTML**
    - All main templates (`base.html`, `index.html`, `gallery.html`, `artwork_detail.html`, `cart.html`, `checkout.html`, `profile.html`, `signup.html`, `login.html`, `testimonial.html`, `my_orders.html`, `edit_profile.html`, `404.html`) were tested using the [W3C Markup Validation Service](https://validator.w3.org/).
    - All templates pass with 0 errors and 0 warnings (Django template tags are ignored by the validator).
    - Screenshots of validation results are included below for each template.

<hr>

> All screenshots are displayed below in a container. Each image can optionally be wrapped in a link to the live Cloudinary validator result or a larger version. For example:



<div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1747858504/base.html_obtz9k.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1747858504/base.html_obtz9k.png" alt="base.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>

  <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1747858510/gallery.html_pzf60m.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1747858510/gallery.html_pzf60m.png" alt="gallery.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>

  <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1747858519/index.html_o3tic9.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1747858519/index.html_o3tic9.png" alt="index.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>

  <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1747863759/profileval_nkmymp.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1747863759/profileval_nkmymp.png" alt="profile.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>


  <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1747864414/profileval_pzsaju.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1747864414/profileval_pzsaju.png" alt="profile.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>

  <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1747864403/chartval_agiwe5.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1747864403/chartval_agiwe5.png" alt="chart.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>

<hr>

---
##  CSS Validation Results
All CSS files were tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The results are as follows:

 <div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748204304/w3ccss_xtcw3i.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748204304/w3ccss_xtcw3i.png" alt="profile.html validation screenshot" width="220" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>



#  Testing

##  Table of Contents
- [Device Testing](#device-testing)
- [Browser Compatibility](#browser-compatibility)
- [Manual Testing of User Stories](#manual-testing-of-user-stories)


---

##  Device Testing

Tested Mollavie on the following real devices:



| Device | Result | Screenshot |
|--------|--------|------------|
| Samsung Galaxy A52 |  ✔️ | ![Samsung A52](https://res.cloudinary.com/dyemjyefz/image/upload/v1748204251/samsunggalaxy_sm4omc.png) |
| iPhone 13 Mini     |  ✔️                | ![iPhone 13](https://res.cloudinary.com/dyemjyefz/image/upload/v1748204238/iphone13_nff9ct.png)    |
| iPad (3rd Gen)     |    ✔️                | ![iPad](https://res.cloudinary.com/dyemjyefz/image/upload/v1748204230/ipadpro_fxdlph.png)              |


---

##  Browser Compatibility

| Browser        | Result | Screenshot |
|----------------|--------|------------|
| Google Chrome  |  ✔️ | ![Chrome](https://res.cloudinary.com/dyemjyefz/image/upload/v1748204202/googlecrom_kxnjzj.png) |
| Mozilla Firefox|  ✔️ | ![Firefox](https://res.cloudinary.com/dyemjyefz/image/upload/v1748205103/firfox_h4vbpg.png) |
| Microsoft Edge |  ✔️ | ![Edge](https://res.cloudinary.com/dyemjyefz/image/upload/v1748205117/age_sa71ia.png)     |

---

##  Manual Testing of User Stories

Manual testing was performed for all major user stories to ensure the site works as intended for different user types. Each scenario was tested on both desktop and mobile devices, and the results are summarized below:

###  As a visitor, I want to browse and view product details
| Step                        | Expected Result                                 | Actual Result |
|-----------------------------|-------------------------------------------------|---------------|
| Navigate to home page       | Homepage loads with welcome and featured art    |  ✔️           |
| Click on “Gallery”          | Artwork list appears                            |  ✔️           |
| Click on an artwork         | Product detail page with image and Buy Now      |  ✔️           |

###  As a visitor, I want to use the shopping cart
| Step                | Expected Result                | Actual Result |
|---------------------|-------------------------------|---------------|
| Add artwork to cart | Item added with message       |  ✔️           |
| View cart           | All items listed              |  ✔️           |
| Remove item         | Item removed with confirmation|  ✔️           |

###  As an authenticated user, I want to buy artwork via Stripe
| Step                | Expected Result                | Actual Result |
|---------------------|-------------------------------|---------------|
| Click Buy Now       | Redirects to Stripe           |  ✔️           |
| Complete payment    | Redirects to success page     |  ✔️           |
| Visit /my-orders    | Order listed with details     |  ✔️           |

###  As a site owner, I want unauthenticated users restricted
| Step                        | Expected Result           | Actual Result |
|-----------------------------|---------------------------|---------------|
| Visit /my-orders logged out | Redirect to login         |  ✔️           |

###  Form Validation and Flash Messages
| Action                | Feedback                     |
|-----------------------|------------------------------|
| Empty form submission | Error displayed              |
| Valid submission      | Success message shown        |

All user stories were manually tested and passed as expected. Screenshots and further details are available in the Testing section above.

---

##   Testing

### Python (Django)
- All Django models and views are tested using the built-in test runner:
- Run with: `python manage.py test`
- Tests cover model validation, view responses, and form handling.
- Stripe payment integration is tested using Stripe's official test cards (e.g., `4242 4242 4242 4242`).
- The Django admin site is verified to be accessible and functional for superusers.
- Example test result screenshot:




<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033932/admin.py_verob5.png" alt="admin.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033936/apps.py_circjo.png" alt="apps.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033941/category.py_s4j26f.png" alt="category.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033948/customer.py_mbg10e.png" alt="customer.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033952/forms.py_xdlg2n.png" alt="forms.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033959/manage.py_jxaedo.png" alt="manage.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033967/order.py_fof3o9.png" alt="order.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033971/product.py_yep4nx.png" alt="product.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748033998/view.py_efgum4.png" alt="view.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748034004/sitemaps.py_h8mbfv.png" alt="sitemaps.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748034008/urla.pyshop_dqmceh.png" alt="urls.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748034008/urla.pyshop_dqmceh.png" alt="settings.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748034036/signals.py_bbrfcj.png" alt="signals.py" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748034041/urls.pymollavie_jg4jis.png" alt="urls.pymollavie" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748034045/urla.pyshop_ejw8uj.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

- (Optional) For larger projects, consider using [Jest](https://jestjs.io/) or [Mocha](https://mochajs.org/) for automated JS unit tests.

---

#### Error Handling

Custom error pages for 400, 403, 404, and 500 errors are implemented and tested.  
Users always see branded, helpful messages—never default Django error screens.



<details>
<summary><strong>403 Error Page</strong></summary>

- **Purpose:** Alerts users that they do not have permission to access a page or resource.
- ![403 Error Screenshot](https://res.cloudinary.com/dyemjyefz/image/upload/v1748204278/test403_f2mxoq.png)
</details>

<details>
<summary><strong>404 Error Page</strong></summary>

- **Purpose:** Informs users when a page is not found and provides navigation options.
- ![404 Error Screenshot](https://res.cloudinary.com/dyemjyefz/image/upload/v1748204284/test404_ahohfj.png)
</details>

<details>
<summary><strong>500 Error Page</strong></summary>

- **Purpose:** Shows when an internal server error occurs and reassures users that the issue is being addressed.
- ![500 Error Screenshot](https://res.cloudinary.com/dyemjyefz/image/upload/v1748204291/test500_qflesv.png)
</details>

### JavaScript Testing

The navbar behavior (auto-collapse on link click) was tested manually in:
- Desktop (Chrome, Firefox)
- Mobile emulator via Chrome DevTools
- Verified that nav collapses after clicking a link




##  Future Features

- **Wishlist / Favorites:**  
  Allow users to save artworks to a wishlist or mark items as favorites for future reference.

- **Product Reviews and Ratings:**  
  Enable customers to leave reviews and ratings on individual artworks to build trust and engagement.

- **Order Tracking:**  
  Provide real-time order status updates and tracking for customers after purchase.

- **Live Chat Support:**  
  Integrate a live chat feature to assist visitors and answer questions instantly.

- **Newsletter Subscription:**  
  Let users subscribe to a newsletter for updates on new artwork, exhibitions, or promotions.

- **Admin Dashboard Enhancements:**  
  Add advanced analytics and sales reporting tools for administrators.

- **Gift Cards and Coupons:**  
  Allow customers to purchase and redeem gift cards or apply discount coupons at checkout.

- **Multi-language Support:**  
  Offer site translations for a wider, international audience.

- **Blog Section:**  
  Share news, artist insights, and painting process stories to engage the community.

- **Social Media Integration:**  
  Display a live Instagram feed or enable sharing artworks directly to social platforms.

- **Favorite Button Improvement**

Currently, users can still mark sold artworks as favorites. This design choice allows visitors to save their favorite pieces for inspiration and maintain engagement even after a painting has been sold.  

In a future update, the system could disable the **“Add to Favorites”** button for sold artworks or replace it with a label such as **“Saved for Inspiration”**. This enhancement would improve realism while still preserving the emotional connection users have with unavailable pieces.

##  References

- **Django Documentation (v3):**  
  [https://docs.djangoproject.com/en/3.0/](https://docs.djangoproject.com/en/3.0/)

- **Bootstrap 5 Documentation:**  
  [https://getbootstrap.com/docs/5.3/getting-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

- **YouTube Tutorials:**  
  - *How to Build an E-commerce Site with Django*  
    [https://www.youtube.com/watch?v=YOUR_VIDEO_1](https://www.youtube.com/watch?v=eZlosaH3fvE&list=PL2aJidc6QnyOe-fp1m4yKHjcInCRTF53N&ab_channel=ARKPROCODER)
  - *Django Custom Error Pages*  
    [https://www.youtube.com/watch?v=YOUR_VIDEO_2](https://www.youtube.com/watch?v=o0XbHvKxw7Y&ab_channel=freeCodeCamp.org)

- **Cloudinary for Django:**  
  [https://cloudinary.com/documentation/django_integration](https://cloudinary.com/documentation/django_integration)

  
- **Stack Overflow:**  
  [https://stackoverflow.com/](https://stackoverflow.com/)  
  (Community answers and code snippets used for troubleshooting and problem-solving.)

- **Perplexity AI:**  
  [https://www.perplexity.ai/](https://www.perplexity.ai/)  
  (Utilized for quick AI-powered research, explanations, and coding solutions.)

- **Other Helpful Resources:**  
  - [dbdiagram.io – Database Diagram Tool](https://dbdiagram.io/)
  - [Heroku – Django Deployment Guide](https://devcenter.heroku.com/categories/django-support)
  - [codeinstitute.net](https://codeinstitute.net/)


# Bug Fixes


##  Registration Bug Fix and Testing

###  Bug Fixed:
The original issue prevented users from registering due to missing success messages and validation feedback. This has been fixed by:
- Updating the `signup_view` to handle form errors
- Adding Django's `messages` framework for user feedback
- Including visible success/error messages on the frontend

###  Manual Testing Scenarios:

| Test Description                      | Input                                   | Expected Outcome                                               | Status |
|--------------------------------------|-----------------------------------------|----------------------------------------------------------------|--------|
| Valid registration                   | Unique username, email, matching strong passwords | User created and redirected to homepage, success message shown | yes     |
| Duplicate username/email             | Existing username or email              | Error message: "User already exists"                           | yes     |
| Weak/mismatched passwords            | `12345` and `password2` mismatch        | Errors about password strength or mismatch                    | yes     |
| Empty form submission                | No input                                | Validation errors shown under each field                       | yes     |
| Success message visibility (UX)      | Valid registration                      | Bootstrap alert shows: "Account created successfully"          | yes     |

All registration scenarios have now been addressed and confirmed to work as expected.

## Registration Bug Fix Screenshots

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752864078/Screenshot_2025-07-18_190246_p0jmf8.png" alt="Registration Success" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752864072/Screenshot_2025-07-18_190421_w5owdt.png" alt="Registration " width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752864098/Screenshot_2025-07-18_174305_xauqhh.png" alt="registration" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752864090/Screenshot_2025-07-18_190011_bdmh02.png" alt="registration" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752864129/Screenshot_2025-07-18_172628_e9tf6t.png" alt="registration" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />





## No order recorded in session — order not saved after Stripe payment

- "No order recorded in session — order not saved" after Stripe payment"

**Issue:**
After a successful Stripe payment, the payment success page sometimes displayed the message:
> No order recorded in session — order not saved. If you were charged, please contact support.

**Diagnosis:**
This error occurred because the session variable `order_id` was not always available on the payment success page after returning from Stripe. This happened if the session was lost or not set correctly before redirecting to Stripe Checkout.

**Steps Taken to Fix:**
- Double-checked that `order_id` is saved to `request.session` immediately after the order is created and before redirecting to payment.
- Made sure the redirect to Stripe is only triggered after `order_id` is saved.
- Tested the entire flow (cart → checkout → payment → success) in a single browser window to ensure session data persists through Stripe’s redirect.

**Result:**
The payment flow now consistently creates, saves, and confirms orders after successful payment, and the user sees their correct order confirmation message. Edge cases (like session loss or page refresh) now show an appropriate warning.

**Note:**  
If  experience this issue while testing, always complete the payment process in one browser tab without reloading the server between steps.

## Screenshots for No order recorded in session  

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752794041/Screenshot_2025-05-19_141832_o5375n.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


### Order creation & payment flow fix

- **Issue:** In the original submission, an order record was created as soon as the user initiated checkout.  If the user cancelled on the Stripe payment page, an unpaid order remained in the database and the product stayed reserved.
- **Fix:** Refactored the checkout workflow so that orders and order items are created only after Stripe confirms payment.  If the Stripe session is cancelled, any reserved product is restored to stock and the order record is deleted.
- **Test:** Attempt to cancel a Stripe payment; verify the product is still available and no unpaid order appears.  Complete a payment; verify the order appears with status “Paid” and the product is marked as sold.


#### Staff admin dashboard

| Step | Expected Result |
|-----|-----------------|
| Create or designate a user with `is_staff=True` (non‑superuser) in the Django admin | A staff user exists |
| Log in as the staff user and navigate to `/admin-dashboard/` | You see a dashboard displaying products and categories with forms to add new items |
| Use the “Add product” form to create a new product | The product appears in the list with a success message |
| Use the “Add category” form to create a new category | The category appears in the list with a success message |
| Edit an existing product or category via the dashboard and save | Changes are reflected immediately |
| Delete a product or category via the dashboard | The item is removed and a confirmation message appears |
| Log out and then log in as a regular user; visit `/admin-dashboard/` | You receive a 403 Forbidden response or are redirected (non‑staff users cannot access the dashboard) |

#### Category filtering

| Step | Expected Result |
|-----|-----------------|
| Ensure products are assigned to categories via Django admin or the staff dashboard | Products have categories |
| Visit the gallery page | Category buttons appear (e.g., *Abstract*, *Landscape*, *Portrait*) |
| Click a category button | Only artworks belonging to that category are displayed |
| Click another category button | The list updates to show artworks from the newly selected category |
| Clear the filter (by removing the `?category=` parameter) | All available artworks are displayed again |

#### Improved payment flow

| Step | Expected Result |
|-----|-----------------|
| Add an artwork to the cart and proceed to payment | The product becomes temporarily unavailable; a Stripe checkout session is created |
| On the Stripe page, cancel or close the payment session | The product returns to “available” status; no new unpaid order appears in “My Orders” |
| Add an artwork to the cart again and complete the payment using a Stripe test card | You are redirected to the success page; the order is listed in “My Orders” with status **Paid**; the product shows as sold/out of stock |


## **Shopping Cart and Stripe Payment Flow**

**Test Case 1: Add to Cart**
-  Added single and multiple products to the cart.
-  Verified that quantities update correctly.
-  Removed items and confirmed cart updates dynamically.

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752770579/Screenshot_2025-05-19_133627_ujzbai.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752770568/Screenshot_2025-05-18_001257_koq8eo.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752771552/Screenshot_2025-07-16_202337_prlotc.png" alt=" test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" /> 

**Test Case 2: Checkout**
-  Proceeded to checkout with valid user.
-  Filled in shipping address and phone number fields.
-  Verified form validation for required fields.


<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752771499/Screenshot_2025-07-15_164346_lnfczj.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752791333/Screenshot_2025-07-17_232326_tab8ef.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752864129/Screenshot_2025-07-18_172628_e9tf6t.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


**Test Case 3: Stripe Payment**
-  Confirmed Stripe test mode is active.
-  Used valid test card numbers (e.g., `4242 4242 4242 4242`) to simulate payment.
-  Confirmed redirection to Stripe Checkout page.
-  Completed payment successfully.
-  Verified that the order status updates to “Paid.”
-  Verified that the `stripe_session_id` is stored for payment tracking.

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752771455/Screenshot_2025-07-13_144412_unn3me.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752771454/Screenshot_2025-07-13_144238_zzpmyu.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752771461/Screenshot_2025-07-13_151021_u6sw5f.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

**Test Case 4: Payment Failure**
-  Tested an invalid card number to confirm payment fails gracefully.
-  Verified that a clear error message is shown to the user.
-  Confirmed no order is marked as paid if payment fails.


<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752794041/Screenshot_2025-05-19_141832_o5375n.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752770568/Screenshot_2025-05-18_001257_koq8eo.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

## Features / Payment Flow

Orders are now created **only after a successful payment** is confirmed by Stripe.  
When a user cancels or abandons the payment process, the unpaid order is **automatically removed**, and the product is **returned to stock**.

## Testing

1. **Add a product to your cart** and proceed to payment.  
2. **Cancel or close** the Stripe payment page before completing the transaction.  
3. Confirm that the product is **available again** and **no new order** appears in “My Orders.”  
4. Complete a payment successfully and verify that the order appears with the status **“Paid.”**

###  Stripe Payment Flow Test

**Test Objective:**  
Verify that successful payments trigger order creation and confirmation in the database.

**Test Steps:**
1. Added a product ("Rosalina") to cart and completed Stripe test checkout.
2. After payment, the app redirected to the success page showing:  
   *“Thank you! Your order has been placed.”*  
   with Order ID `#78`.
3. Verified in Django shell that the order was saved:

   ```python
   python manage.py shell
   >>> from orders.models import Order
   >>> Order.objects.latest('created_at')
   <Order: Order #78 by Mirjana1>

## Payment Flow Testing

1. **Add a product to your cart** and proceed to payment.
2. **Cancel or close** the Stripe payment page. You should see:
   - No new order in “My Orders”.
   - The product is again marked as available in the gallery.
3. **Complete a payment** with a Stripe test card (e.g., `4242 4242 4242 4242`). Upon return:
   - A success message and order summary appear.
   - The order status is “Paid” in the database.
4. **Abandon the session** and refresh the page. You should not see leftover unpaid orders.

## Account Deletion Testing

1. Log in as a user and go to **Profile → Delete My Account**.
2. Confirm deletion. The user account, associated `CustomerProfile`, and any orders linked to the user are removed.
3. Verify that you can now delete the same user from the Django admin without foreign‑key errors.


## New Features Added in Resubmission

- **Staff admin dashboard** – implemented a role‑based front‑end dashboard (`/admin-dashboard/`) for staff members.  The dashboard lists all products and categories in tables and includes forms to create new items.  Staff can edit and delete existing entries.  Access is controlled via a `@user_passes_test(lambda u: u.is_staff)` decorator.
- **Category filter** – added a `Category` model and filter buttons on the gallery page.  Users can click a category to limit artworks to that category.  Categories can be created and assigned to products in Django admin or via the staff dashboard.
- **Enhanced payment flow** – refined the checkout process so that orders and order items are saved only after the customer completes payment.  If a payment session is cancelled, the reserved product is restored to its available state and no unpaid order remains.


 ## Category Filter

Users can browse artworks by category. Each artwork can be assigned to a category (e.g., Abstract, Landscape) via the admin panel.

#### Testing
1. Add categories in the admin panel.
2. Assign artworks to categories.
3. Visit `/gallery/` and use the buttons to filter by category.
4. Confirm that only artworks from the selected category are displayed.

  <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1759956199/category_ldhqdm.png" alt="category" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

##  Known Bug: Old Project Users in Admin

In my **Mollavie** project, the Django admin dashboard shows some user accounts that do not belong to this project.  
These users were created for my **previous project**, which uses the **same database**.

They still appear because Django’s `auth_user` table is shared when you reuse the same database.  
I did **not** delete these old users because my previous project is still **submitted for assessment** and must stay complete for grading.  
Deleting them could break the integrity of the old project’s data.

---

###  Solution

- I fixed my `Order.customer_id` field to be **nullable**, so any **new Mollavie users** can be deleted properly from the admin site.
- I verified that orders do not block user deletion.
- This ensures Mollavie’s user management works correctly and safely.

---

## Future Improvement

In the future, I will use **separate databases** for each Django project to keep data isolated and avoid this overlap.

---

** Note for assessors:**  
This issue does **not affect** the core functionality of Mollavie’s authentication or order system.

##  Bug: Cannot Delete Users with Related Profiles


### Problem
While testing the Django admin panel, attempting to delete a user triggered a 500 `IntegrityError`. The error indicated that the user could not be deleted due to a foreign key constraint from the `CustomerProfile` (or `UserProfile`) model.

### Root Cause
The `CustomerProfile` model had a foreign key to Django’s built-in `User` model with `on_delete=models.CASCADE`. This configuration prevents a user from being deleted if a profile still references them, unless the profile is deleted first.

### Fix
The `user` field in the profile model was updated to:
```python
user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)


```
##  CRUD Functionality Fix (Create, Read, Update, Delete)

###  Original Issue
The assessor noted that CRUD (especially Delete) functionality was missing or incomplete in the user interface. Users were not able to delete their own accounts or related data from the frontend, and there was no evidence of role-based deletion in the app.

###  Fix Implemented

#### Delete (User Account)
- A **"Delete My Account"** button was added to the user **Profile page** (`profile.html`).
- This links to a secure view (`delete_profile`) which allows logged-in users to permanently delete their own accounts after confirmation.
- When a user is deleted:
  - Their associated `CustomerProfile` and `Order` records are also deleted thanks to Django's `on_delete=models.CASCADE`.

#### Delete (Admin Panel)
- Admins can delete users and products through the Django admin interface (`/admin/`).
- Orders associated with deleted users are removed automatically.

#### Read & Update
- **Read**: Users can view their account info, orders, and artwork details from their profile and gallery.
- **Update**: Users can update their profile information (name, email, address) via a form on the **Edit Profile** page.

###  Testing Performed

| Operation | Description                                 | Access Role        | Status |
|-----------|---------------------------------------------|--------------------|--------|
| Create    | Register user, place order                  | User               | yes    |
| Read      | View profile, order history, product details| User, Admin        | yes     |
| Update    | Edit profile info                           | User               | yes     |
| Delete    | Delete own account                          | User               | yes     |
| Delete    | Remove users/products via admin             | Admin              | yes     |

All CRUD operations are now functional from both the user interface and the admin backend.





<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752771545/Screenshot_2025-07-16_202020_gz5g3p.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752771492/Screenshot_2025-07-15_164115_ehuoyj.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1752791772/Screenshot_2025-07-16_193811_jblyip.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


##  Security Testing: Mixed Content Validation

To ensure Mollavie was fully secure and compliant with modern browser standards, I tested the live deployed site using [WhyNoPadlock.com](https://www.whynopadlock.com) – a third-party SSL and content security validator.

###  Why I Used WhyNoPadlock.com

Although my Heroku deployment included HTTPS by default, browsers may still show security warnings if any **resources (images, stylesheets, scripts)** are loaded using `http://` instead of `https://`. This is known as **mixed content**, and can:
 Decrease user trust.

### screenshots of WhyNoPadlock.com results:

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1753469442/Screenshot_2025-07-25_193731_l6iint.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1753469449/Screenshot_2025-07-25_193455_bljgef.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />
   


### Fixed: CustomerProfile admin 500 error

- **Issue:** Attempting to access `CustomerProfile` in Django admin caused a 500 server error if a profile had no linked user.  
- **Cause:** The admin list tried to display `user` directly, which was `NULL` for some profiles.  
- **Fix:** Replaced `user` in `list_display` with a custom `get_username` method that safely handles null values.  
- **Test:** Verified in Django admin that Customer Profiles now display correctly, even if no user is linked.
 
### Deployment Fixes on Heroku

During deployment to Heroku, I encountered two major issues:

1. **`django-extensions` not found**  
   - **Cause:** `django-extensions` was installed locally but not included in `requirements.txt`.  
   - **Fix:** Added `django-extensions==4.1` to `requirements.txt` and ensured it was only used in development (`DEBUG=True`).

2. **PostgreSQL adapter error (`psycopg2`)**  
   - **Cause:** Heroku was building with Python 3.13, and `psycopg2` is not fully compatible with this version. This caused the build to fail with `_PyInterpreterState_Get` errors.  
   - **Fix:**  
     - Removed `psycopg2` from `requirements.txt` and replaced it with `psycopg2-binary==2.9.10`.  
     - Added a `runtime.txt` file to pin the Python version to `python-3.12.7`, which is stable for Django apps on Heroku.  

3. **Result:**  
   - The app now builds and deploys successfully on Heroku.  
   - Verified that static files are collected, the admin panel is functional, and the `CustomerProfile` section no longer throws a 500 error.  


### Admin Dashboard (Staff Only)

A `/admin-dashboard/` route allows staff users to manage products and categories from a front-end interface.  
Only users with `is_staff=True` can access this dashboard.  
Features include:

- Viewing all products and categories in tables
- Adding new products and categories via forms
- Editing existing products and categories
- Deleting products and categories

This feature demonstrates custom CRUD functionality beyond the course walkthrough projects and meets the role‑based authorization requirements.

#### Staff-Only Dashboard Testing

1. Log in as a staff user (either by running `python manage.py createsuperuser` or by marking an existing user as staff via the Django admin).
2. Navigate to `/admin-dashboard/`.  
3. Confirm that:
   - Products and categories are listed correctly.
   - You can add a new product or category via the forms.
   - The edit and delete buttons work (items update or are removed).
4. Log in as a regular user and attempt to access `/admin-dashboard/` — you should receive a “Forbidden” or redirect response.

A superuser (`is_superuser=True`) has full control of the site, including all models via Django admin.  
A staff user (`is_staff=True` but `is_superuser=False`) can access the custom `/admin-dashboard/` interface but does not have unrestricted access to every model.  
The dashboard ensures only authorized staff can perform CRUD on products and categories.


###  Favorite Artwork Feature

Registered users can now mark artworks as **favorites** directly from the Artwork Detail page.  
A toggle button allows users to add or remove any artwork from their personal favorites list.

- The button text and icon dynamically change based on favorite status:
  -  *Add to Favorites* (if not yet added)
  -  *Remove from Favorites* (if already added)
- Favorites are linked to the logged-in user profile.
- This feature introduces more personalization and engagement for returning users.

#### Favorite Artwork Testing

| Test Action | Expected Result | Pass |
|--------------|----------------|------|
| Logged-in user clicks "Add to Favorites" | Artwork added to user's favorites | yes |
| User clicks again "Remove from Favorites" | Artwork removed from favorites | yes |
| Button text changes correctly | Reflects current favorite state | yes |
| Non-logged-in user | Button not shown | yes |

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1760620213/Screenshot_2025-10-16_140406_ccqzlw.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- In the [GitHub repository](https://github.com/mirjanacale/Mollavie.git), navigate to the Settings tab.
- From the source section drop-down menu in Heroku, connect to your GitHub repository and select the **main** branch.
- Enable automatic deploys or click "Deploy Branch" to trigger a manual deployment.
- Ensure your project contains a `Procfile`, `requirements.txt`, and all necessary environment variables in the Heroku dashboard (under Settings > Config Vars).
- Add the Heroku Postgres add-on from the Resources tab.

The live link can be found [here](https://mollaviart-f52cde6730c6.herokuapp.com/)

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/mirjanacale/Mollavie.git)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/mirjanacale/Mollavie.git`
7. Press Enter to create your local clone.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/mirjanacale/Mollavie.git)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!



### Local VS Deployment

There are no major differences between the local   version and the deployed (Heroku) version that I'm aware of.

## Acknowledgements

- Inspired by artists everywhere, especially my daughter for original artworks.
- Special thanks to Code Institute mentors and the Stack Overflow community.


## Contributing

If you have suggestions for new features or improvements to the site, please feel free to open an issue.
If you would like to contribute code, please fork the repository and create a pull request.


