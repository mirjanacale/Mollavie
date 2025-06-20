# Mollavie


<div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <a href="https://res.cloudinary.com/dyemjyefz/image/upload/v1748204215/firstimg_kugk4c.png" target="_blank">
    <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1748204215/firstimg_kugk4c.png" alt="base.html validation screenshot" width="800" style="border-radius: 8px; box-shadow: 0 2px 8px #ccc; margin-bottom: 8px;" />
  </a>
  </div>


A modern, accessible Django-based art shop for unique artworks.
Mollavie is a Django-based e-commerce platform designed to showcase and sell original artworks and prints. The site features a user-friendly interface, responsive design, and robust functionality for both customers and administrators. Mollavie supports user registration, product browsing, shopping cart management, and secure checkout with Stripe integration.

---

## Features

- Browse original art and prints
- User registration and profile management
- Shopping cart and checkout with Stripe integration
- Order history and profile management for users
- Custom error pages (400, 403, 404, 500)
- Responsive design for all devices
- Admin panel for product and order management



## Table of Contents

- [Database Planning](#database-planning)
- [Design](#design)
- [Wireframes](#wireframes)
- [Agile Development Process](#agile-development-process)
- [Technologies Used](#technologies-used)
- [Lighthouse Scores](#lighthouse-scores)
- [HTML Validation Results](#html-validation-results)
- [Testing](#testing)
- [Error Handling](#error-handling)
- [Deployment](#deployment)
- [Future Features](#future-features)
- [References](#references)
- [Contributing](#contributing)


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

---

 A full list of issues and progress can be viewed on the [GitHub Project Board](https://github.com/users/mirjanacale/projects/11).


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


### Bug Fixes

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

- In the [GitHub repository](https://github.com/mirjanacale/Mollavie.git), navigate to the Settings tab
- From the source section drop-down menu, select the **Main** Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

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

## Acknowledgements

- Inspired by artists everywhere, especially my daughter for original artworks.
- Special thanks to Code Institute mentors and the Stack Overflow community.


## Contributing

If you have suggestions for new features or improvements to the site, please feel free to open an issue.
If you would like to contribute code, please fork the repository and create a pull request.


