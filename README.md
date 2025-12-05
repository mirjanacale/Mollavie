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

Mollavie is an independent e-commerce platform specialising in the sale of original artwork created by the artist Mirjana. The primary goal of the platform is to give customers direct access to unique paintings without any intermediary or commission-based marketplace. The business model focuses on presenting artwork in a modern, trustworthy, and visually rich environment that supports discovery, browsing, and seamless purchasing.

## Value Proposition

Mollavie offers authentic, hand-painted artworks that cannot be found in mass-production marketplaces. Each painting is presented with detailed information, clear imagery, and a simple purchase experience. Customers buying from Mollavie receive one-of-a-kind art directly from the artist, eliminating platform fees, agency commissions, or unknown production sources.

## Customer Segments

The platform is designed for customers who value original hand-crafted artwork. These include individual art collectors, homeowners seeking unique decoration, interior designers sourcing bespoke pieces, and general online art buyers who want to support independent artists.

## Product Strategy

Mollavie sells only original paintings created by Mirjana. This creates a high-trust environment where customers know exactly who created the artwork, how it was made, and that every piece is unique. There are no digital prints, dropshipping items, or mass-manufactured goods. This positions the platform in a niche market of authentic, single-edition art products.

## Pricing Strategy

Each painting is priced according to size, materials used, complexity of the artwork, and the time required for production. Pricing is transparent, with no additional platform fees. Stripe handles secure payments, providing customers with a reliable and recognised checkout flow. The business avoids discount models or constant promotions to preserve the artistic and collectible value of the pieces.

## Revenue Model

Revenue is generated exclusively from direct sales of original paintings. No commissions, subscription fees, or marketplace charges apply. Because the platform operates independently, the full sale price goes to the artist, making the revenue model straightforward and sustainable.

## Marketing and Audience Reach

Mollavie uses a combination of organic marketing channels to reach potential customers. These include a dedicated Facebook business page, newsletter updates, and future potential channels such as Instagram, Pinterest, and an artist blog. Search Engine Optimisation is integrated into the site through descriptive meta tags, a structured sitemap, and a valid robots.txt file to improve discoverability.

## Operations and Order Handling

When a customer places an order, Stripe processes the payment and the order is saved into the database. The artist then prepares the painting for packaging and delivery. Orders are manually fulfilled to ensure quality control and safe handling of the artwork. As the business grows, shipping integrations or courier tracking may be added.

## Competitive Positioning

Mollavie differs from large marketplaces because it is fully artist-owned and does not include mass-produced prints or generic artwork. Customers who prefer boutique, authentic, and personal art-buying experiences can expect a higher level of trust and originality compared to general marketplaces.

## Future Expansion

The business model has room for expansion in several areas. These include custom commission requests from customers, seasonal art collections, limited-edition series, instructional blog content, and potential collaborations with interior designers. Expansion will remain aligned with the platform’s core principle: original art created directly by the artist.

## Risk Considerations

The main risks include low traffic during early stages and limited inventory because the artwork is hand-made. Marketing consistency and social media presence reduce this risk. Future additions such as customer reviews or artist storytelling may also improve customer confidence and increase conversions.

## Summary

Mollavie follows a direct-to-consumer business model built around authenticity and originality. It provides customers with a transparent and personal art-buying experience, supported by secure payment processing and independent control over product presentation and pricing.


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





   











   
#  Resubmission Updates for Assessment Feedback 07 december 2025

## Sitemap & Robots.txt Fix

Users encountered a `500 Internal Server Error` when visiting `/sitemap.xml` during assessment.

### Root Cause
The sitemap referenced undefined URL names:

```
return ['home', 'gallery']
```

but the actual URLs were namespaced:

```
return ['shop:home', 'shop:gallery']
```

The product sitemap also used an incorrect field (`is_active` instead of `is_available`).  
`robots.txt` pointed to a non-working sitemap, which caused SEO issues.



### Fix Implemented

1. **Corrected sitemap URL names**  
   Updated the sitemap to use namespaced routes.

   **Before**
   ```
   return ['home', 'gallery']
   ```

   **After**
   ```
   return ['shop:home', 'shop:gallery']
   ```

2. **Updated product filtering**  
   Replaced the non-existent `is_active` field with the correct `is_available` field.

   **Before**
   ```
   Product.objects.filter(is_active=True)
   ```

   **After**
   ```
   Product.objects.filter(is_available=True)
   ```

3. **Corrected robots.txt**  
   Updated the file to properly reference the live sitemap:

   ```
   User-agent: *
   Disallow: /admin/
   Allow: /

   Sitemap: https://mollaviart-f52cde6730c6.herokuapp.com/sitemap.xml
   ```

  
   <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764533407/Screenshot_2025-11-30_200036_a6kgoo.png" alt="sitemp" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


### Testing

- Opened the sitemap locally and on Heroku to confirm it loads successfully.
- Verified that:
  ```
  reverse('shop:home')
  reverse('shop:gallery')
  ```
  resolve correctly.
- Confirmed sitemap lists:
  - Home page
  - Gallery
  - Individual artworks with `<lastmod>`
- Verified no broken links and correct product filtering.
- Confirmed robots.txt formatting and SEO discoverability.

### Outcome

The `/sitemap.xml` error has been fully resolved.  
The sitemap is valid, loads correctly, and meets SEO requirements.  
`robots.txt` correctly references the sitemap, satisfying assessment criteria.


## Admin CRUD Fix (Resubmission Update)

- Users encountered broken CRUD actions in the custom admin dashboard during assessment.

### Root Cause
- Edit and delete actions returned `404` because the admin routes were incorrect or missing.

- There was no direct link to the custom admin dashboard in the navbar, and admin access was not restricted to staff. These issues affected **LO1.4**, **LO1.8**, **LO1.13**, and **LO1.15**.

### Fix Implemented

1. **Corrected admin URL patterns**  
   Updated `urls.py` to point to the correct edit/delete endpoints for products and categories:

   ```python
   path('admin-dashboard/product/<int:product_id>/edit/', views.admin_edit_product, name='admin_edit_product'),
   path('admin-dashboard/product/<int:product_id>/delete/', views.admin_delete_product, name='admin_delete_product'),

   path('admin-dashboard/category/<int:category_id>/edit/', views.admin_edit_category, name='admin_edit_category'),
   path('admin-dashboard/category/<int:category_id>/delete/', views.admin_delete_category, name='admin_delete_category'),

- Added staff-only admin link in the navbar
  The link is visible only for staff users:


  
   <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764533356/admin_dashboard_bzhhhs.png" alt="dashboard" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />



```
{% if user.is_staff %}
<a class="nav-link" href="{% url 'shop:admin_dashboard' %}">Admin Dashboard</a>
{% endif %}
```
Restricted admin views to staff
All custom admin views now require staff privileges to access.

### Testing
- Logged in as staff:

- Create, edit, and delete actions work without 404 errors.

- Forms load correctly and changes reflect instantly in the gallery.

- Logged in as non-staff:

- Cannot access the admin dashboard.

-  Navbar link is hidden.

Verified that navigation from the navbar reaches the admin dashboard and returns to catalog pages without broken links.


   <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764533417/TESTING_CRUD_igiddh.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


### Outcome

The admin CRUD system is now complete, functional, and secure. Routes resolve correctly, the dashboard is discoverable only to staff, and access is properly restricted. This satisfies the assessment criteria for CRUD and role-based access.

 
   <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764533363/admin_deleted_r8hkju.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

   
   <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764533373/admin_product_created_hhvdca.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


## Favorites System Testing

The Favorites feature allows logged-in users to toggle an artwork as a favorite.  
There is **no favorites page**; the system simply updates the database when the button is clicked.

### Test: Add Favorite
1. Log in and open artwork `/artwork/<id>/`.
2. Click the “Add to Favorites” button.
3. Result in terminal:
   - `POST /favorite/<id>/ 302`
4. Expected outcome:
   - Favorite entry is created in the database.
   - Button changes to “Remove from Favorites.”

### Test: Remove Favorite
1. With the same artwork already favorited, click the button again.
2. Result in terminal:
   - `POST /favorite/<id>/ 302`
3. Expected outcome:
   - Favorite entry is removed from the database.
   - Button changes back to “Add to Favorites.”

### Test: Page Reload
1. Refresh `/artwork/<id>/`.
2. Expected:
   - Button correctly shows the current state based on the database.
3. Result: ✔️

### Test: Non-Logged-In User
1. Log out and visit `/artwork/<id>/`.
2. Expected:
   - Favorite button is hidden, OR clicking redirects to login.
3. Result: ✔️

### Evidence From Server Logs
Example from testing:

 
   <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764950283/favorite_testing_egkqjl.png" alt="favorite" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />










## Cloudinary Image Upload Fix (Resubmission Update)

This update explains how product images stopped appearing in the application and why existing images disappeared after each deployment. All issues were caused by the project storing images locally instead of in Cloudinary.

### Root Cause

The Product model used a local ImageField:

```python
image = models.ImageField(upload_to="products/")
```

Heroku does not keep local media files. Every deployment removed everything stored in the `/media/products/` directory. Cloudinary was configured, but due to duplicated and incorrectly ordered environment loading, Django never activated the Cloudinary storage backend. This caused every new upload to be stored locally instead of in Cloudinary, leading to missing images, 404 errors, and disappearing content.

### Fix Implemented

The Product model was updated to use CloudinaryField instead of ImageField.

Before:
```python
image = models.ImageField(upload_to="products/")
```

After:
```python
from cloudinary.models import CloudinaryField
image = CloudinaryField("image")
```

The environment variable loading in `settings.py` was corrected so that `BASE_DIR` is defined before executing `env.py`.

Before:
```python
if os.path.exists("env.py"):
    exec(open("env.py").read())

env_path = os.path.join(BASE_DIR, "env.py")
if os.path.exists(env_path):
    exec(open(env_path).read())
```

After:
```python
BASE_DIR = Path(__file__).resolve().parent.parent

env_path = BASE_DIR / "env.py"
if env_path.exists():
    exec(open(env_path).read())
```

Cloudinary was then ensured as the active storage backend:

```python
CLOUDINARY_STORAGE = {
    "CLOUDINARY_URL": os.environ.get("CLOUDINARY_URL")
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
MEDIA_URL = "/media/"
```

A new migration was created and applied so that the updated field could take effect.

### Testing

New product images were uploaded through Django Admin and confirmed to appear in the Cloudinary Media Library. The Gallery and Product Detail pages were reloaded and displayed the images correctly. The application was redeployed to Heroku, and the images remained in place, confirming that they now persist across deployments. All previously missing and broken image URLs were resolved.

### Outcome

The project now stores all product images directly in Cloudinary, which provides permanent and stable media storage. Images no longer disappear after deployments, and new uploads display correctly across the application. This fully resolves the media persistence issue identified during assessment.

 <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764533351/admin_clodenery_edekz6.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


 
   <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764533389/image_ClodinaryField_rpvzmj.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


## Testimonial Model Addition (Resubmission Update)

This update documents the addition of a new Testimonial model, implemented to meet assessment requirements for demonstrating database design, model creation, and dynamic content handling within the application.

### Root Cause

The original project did not include a secondary model that supports user-generated or dynamically managed content. The assessment required at least one additional model with clear fields, database integration, and admin management. Without this model, the project did not fully meet the criteria for demonstrating relational data structures and CRUD support.

### Fix Implemented

A new Testimonial model was created with fields for the testimonial author, testimonial text. The model integrates with Django’s ORM and is fully managed through Django Admin.

Before:
(No testimonial model existed.)

After:
```python
class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
```

The model was registered in the Django Admin to allow staff users to create, view, edit, and delete testimonials.

```python
from django.contrib import admin
from .models import Testimonial

admin.site.register(Testimonial)
```

A new migration was made and applied to include the Testimonial model in the database.

### Testing

The Testimonial model was tested directly through Django Admin. New testimonials were added and confirmed to display correctly. Editing a testimonial updated the database as expected, and deletion removed it without errors. Model fields were validated to ensure input limits and formatting behaved correctly. The data appeared reliably within the admin dashboard.

### Outcome

The application now includes a fully functional Testimonial model that satisfies the assessment requirement for an additional dynamic database model. Testimonials can be created, displayed, and managed through Django Admin, improving both project completeness and data structure quality.


 <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764611010/costumers_think_daufkv.png" alt="statments" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

## Payment Flow Bug – Incorrect “Sold” Status


- When a user clicked Buy Now on the artwork detail page, the product was immediately marked as sold even if the Stripe payment was not completed. As a result, the detail page displayed the message:
```
This piece has been sold.
```  

- even though no successful transaction occurred.

### Root Cause

- Inside the create_checkout_session view, the product’s is_available field was set to False before the Stripe payment process began:

```
artwork.is_available = False
artwork.save()
```

- This caused the system to treat the item as sold as soon as the Buy button was pressed, regardless of whether the payment succeeded or was cancelled.

### Fix Implemented

- The early availability update was removed from create_checkout_session.
The product is now marked as sold only in payment_success, after Stripe confirms a successful payment.

### Before
```
artwork.is_available = False
artwork.save()
```

### After

 - Removed from create_checkout_session
 - Product availability now updates only after successful payment

### Testing

- Clicked Buy Now and closed the Stripe popup.
Result: The product remained available.

- Completed a Stripe test payment.
Result: The product changed to sold correctly.

- Cancelled a payment.
Result: The product remained available and no false “sold” message appeared.

### Outcome

- The payment flow now works correctly.
Products are only marked as sold after Stripe confirms a successful charge, preventing incorrect “sold” messages on the detail page.


 <img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764622297/payment_flow_oa8kvi.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />

 
## Sitemap Fix

- The sitemap previously caused a 500 Internal Server Error during assessment. Django attempted to load URL names that did not exist because the application used namespaced routes. The product sitemap also referenced the wrong field, causing filtering errors. After updating the sitemap classes, the XML renders correctly and the robots.txt file points to the valid sitemap URL.

### Root Cause

- Sitemap classes referenced wrong URL names (home, gallery) instead of namespaced names (shop:home, shop:gallery).
The product sitemap attempted to filter using the field is_active, which does not exist in the Product model.
This caused the sitemap generator to fail before rendering.

### Fix Implemented

- Updated static view sitemap to reference correct namespaced URL names.

- Updated product sitemap to filter using the correct field is_available.

- Verified sitemap loads without errors in both local and production environments.
Before
### sitemap

````
return ['home', 'gallery']
````

### product sitemap
```
Product.objects.filter(is_active=True)
```
After
### sitemap
```
return ['shop:home', 'shop:gallery']
```
### product sitemap
```
Product.objects.filter(is_available=True)
```
### Testing

Loaded /sitemap.xml locally and confirmed correct XML structure.
Verified all URLs in sitemap resolve successfully.
Checked Heroku production sitemap to ensure the generator works without server errors.

### Outcome

The sitemap now renders correctly and is compatible with search engine crawlers.
This resolves the 500 error reported in assessment.


<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764687096/robots_txt_her2v1.png" alt="sitemap" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />








## Cancel Order Feature (Resubmission Update)

- This feature was added to allow users to cancel an order that has not been paid. When an unpaid order is cancelled, the product automatically becomes available again in the store. This ensures correct business logic for single-quantity artwork sales.

### Root Cause

- Originally, the checkout flow marked items as unavailable when added to the cart, but there was no user-facing way to cancel an unpaid order. The only way to reverse the reserved item was through the Django admin panel. This prevented users from managing their own unpaid orders and caused products to remain marked as Sold Out until manually corrected.

## Fix Implemented

- Added a new view payment_cancel to restore product availability and delete the unpaid order.

Before

## No cancel view existed


After

```
def payment_cancel(request):
    order_id = request.session.get('order_id')

    if order_id:
        order = get_object_or_404(Order, id=order_id, paid=False)
        for item in order.items.all():
            item.product.is_available = True
            item.product.save()
        order.delete()
        del request.session['order_id']

    messages.info(request, "Payment was cancelled. The item is back in the store.")
    return redirect('shop:cancelled_page')
```

- Updated template logic to show a Cancel Order button only for unpaid orders.

Before

-  No cancellation option existed for users 


After
```
{% if not order.paid %}
    <span class="badge bg-warning text-dark mt-1">Unpaid</span>
    <form action="{% url 'shop:payment_cancel' %}" method="get" class="mt-2">
        <button class="btn btn-danger btn-sm">Cancel Order</button>
    </form>
{% endif %}
```

- Added the My Orders page to the navigation bar and ensured it appears only when a user is logged in.

- Connected the cancel button to the /cancel/ route and added a success message page to confirm cancellation.

## Testing

### Tests were performed manually:

- Created an unpaid order by entering checkout but not completing Stripe payment.

- Navigated to My Orders and verified the order appeared with the Unpaid status.

- Clicked Cancel Order.

- Verified redirect to the Payment Cancelled page with confirmation message.

- Verified the product was restored as available.

- Confirmed the order was removed from the user's My Orders page.

- Checked Django admin to ensure the order was deleted and the product status was correct.

### Outcome

- Users can now safely cancel unpaid orders. The system restores product availability automatically and removes abandoned orders from the database. This resolves the earlier issue where items became permanently Sold Out unless manually changed in the Django admin.




<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764698502/cansel_payments_hdb5dg.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />



<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1764698509/cansel_payment_xdkjp0.png" alt="stripe test" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />




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

## Authentication Testing

The authentication system was tested to ensure users can securely register, log in, log out, and only access pages appropriate for their role.

### Registration (Signup)
| Scenario | Expected Result | Actual Result |
|----------|----------------|----------------|
| Valid signup with unique email/username | Account created, redirected, success message displayed | ✔️ |
| Duplicate email or username | Error shown: “User already exists” | ✔️ |
| Weak or mismatched passwords | Validation errors displayed | ✔️ |
| Empty form submission | Required-field errors shown | ✔️ |

### Login
| Scenario | Expected Result | Actual Result |
|----------|----------------|----------------|
| Valid credentials | User logged in, redirected to homepage | ✔️ |
| Invalid password | Error message displayed | ✔️ |
| Non-existing user | Login refused | ✔️ |

### Logout
| Scenario | Expected Result | Actual Result |
|----------|----------------|----------------|
| User clicks “Logout” | Session cleared, logout message shown | ✔️ |

### Restricted Page Access
| Page | User Type | Expected | Actual |
|------|-----------|----------|--------|
| /profile/ | Not logged in | Redirect to login | ✔️ |
| /my-orders/ | Not logged in | Redirect to login | ✔️ |
| /admin-dashboard/ | Regular user | 403 Forbidden | ✔️ |
| /admin-dashboard/ | Staff user | Dashboard visible | ✔️ |


## Database Integrity Testing

Database relationships were tested to ensure safe deletion, consistent foreign-key behaviour, and accurate data storage.

### User & Profile Deletion
| Scenario | Expected Result | Actual |
|----------|----------------|--------|
| User deletes their own account | User, CustomerProfile, and related Orders removed | ✔️ |
| Admin deletes a user with orders | No IntegrityError; related data removed | ✔️ |
| Profile without linked user | CustomerProfile admin page loads safely | ✔️ |

### Order Integrity
| Scenario | Expected Result | Actual |
|----------|----------------|--------|
| Payment completed | Order created with status “Paid” | ✔️ |
| Payment cancelled | No order saved; product returned to stock | ✔️ |
| Session lost during checkout | No orphan orders created | ✔️ |

### Newsletter Integrity
| Scenario | Expected Result | Actual |
|----------|----------------|--------|
| Duplicate email submitted | Duplicate prevented by model constraint | ✔️ |
| New valid email | Added once to database | ✔️ |

### Category → Product Relationship
| Scenario | Expected Result | Actual |
|----------|----------------|--------|
| Delete a category | Products remain safe or reassigned | ✔️ |
| Product with category displays in gallery | Filter works correctly | ✔️ |

### Favorites System
| Scenario | Expected Result | Actual |
|----------|----------------|--------|
| Add/remove favorite | Entry created or deleted correctly | ✔️ |
| User deleted | All related favorites removed | ✔️ |






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

| Test Action | Expected Result | Pass |g
|--------------|----------------|------|
| Logged-in user clicks "Add to Favorites" | Artwork added to user's favorites | yes |
| User clicks again "Remove from Favorites" | Artwork removed from favorites | yes |
| Button text changes correctly | Reflects current favorite state | yes |
| Non-logged-in user | Button not shown | yes |

<img src="https://res.cloudinary.com/dyemjyefz/image/upload/v1760620213/Screenshot_2025-10-16_140406_ccqzlw.png" alt="urls.pyshop" width="350" style="border-radius:8px; box-shadow:0 2px 8px #ccc; margin-bottom:8px;" />


# Deployment

This project uses GitHub for version control and Heroku for hosting the live application. The following sections explain how to deploy the project to GitHub, how to deploy it to Heroku, and how to fork or clone the repository for your own use.

# Deploying to GitHub

The full project code is stored on GitHub. To deploy your version to GitHub:

1. Create a new GitHub repository:
   https://github.com/new

2. Open your project folder in a terminal and initialize Git:

```
git init
```

3. Add all project files:

```
git add .
git commit -m "Initial commit"
```

4. Connect to your GitHub repository:

```
git remote add origin https://github.com/https://github.com/mirjanacale/Mollavie.git/mi.git
```

5. Push the project:

```
git push -u origin main
```

The project is now deployed on GitHub.

# Deploying to Heroku

The live project is hosted here:

https://mollaviart-f52cde6730c6.herokuapp.com/

## Create the Heroku App

Log in:

```
heroku login
```

Create a new application here:

https://dashboard.heroku.com/apps

## Add Heroku Postgres

Open the Heroku Dashboard → Resources tab.  
Search for **Heroku Postgres** and add the free tier.

This automatically sets the `DATABASE_URL` environment variable.

## Configure Environment Variables

In the Heroku Dashboard, open:

Settings → Reveal Config Vars

Add the following:

```
SECRET_KEY=your_production_secret_key
DEBUG=False
ALLOWED_HOSTS=<your-heroku-app>.herokuapp.com,localhost,127.0.0.1
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
STRIPE_PUBLIC_KEY=pk_live_or_test_key
STRIPE_SECRET_KEY=sk_live_or_test_key
STRIPE_WH_SECRET=whsec_from_stripe
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASS=your_email_password
```

Create a Cloudinary account here:  
https://cloudinary.com/

Stripe API keys are obtained here:  
https://dashboard.stripe.com/apikeys

## Connect Heroku to GitHub

1. Open the **Deploy** tab in Heroku.
2. Choose **GitHub** as the deployment method.
3. Connect your repository.
4. Enable **Automatic Deploys** or deploy manually.

## Procfile

Ensure a `Procfile` exists in the project root:

```
web: gunicorn mollavie.wsgi:application
```

## Static and Media Files

Heroku automatically runs:

```
python manage.py collectstatic
```

Static files are handled by Django’s static storage.  
Media files are stored in Cloudinary and require the `CLOUDINARY_URL` variable.

## First Deploy

In the Deploy tab, select `main` and click **Deploy Branch**.  
When deployment completes, click **Open App**.

## Run Migrations and Create Superuser on Heroku

Open the Heroku console:

```
python manage.py migrate
python manage.py createsuperuser
```

The application is now live.

# Updating the Live Site

After making changes locally, push them to GitHub:

```
git add .
git commit -m "Update project"
git push origin main
```

If automatic deploys are enabled, Heroku redeploys immediately.  
If models changed, run migrations again in the Heroku console:

```
python manage.py migrate
```

# Troubleshooting Deployment

To check logs:

```
heroku logs --tail
```

Verify the following:

DEBUG is set to False  
ALLOWED_HOSTS includes the Heroku domain  
All required config vars are set  
Migrations applied successfully  
Static files collected successfully  
Cloudinary uploads working  

# Forking This Repository

Forking creates your own independent copy of the project.

1. Log into GitHub.
2. Open the repository:
  https://github.com/mirjanacale/Mollavie.git
3. Click **Fork** (top right).
4. GitHub creates a new copy under your account.

You can now modify or deploy your own version.

# Cloning This Repository

Cloning allows you to run a local copy of the project.

To clone:

```
git clone https://github.com/mirjanacale/Mollavie.git
```

Move into the project:

```
cd <your-repo-name>
```

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

For Windows:

```
venv\Scripts\activate
```

Install project dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WH_SECRET=whsec_...
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASS=your_email_password
```

Apply migrations:

```
python manage.py migrate
```

Run the local development server:

```
python manage.py runserver
```

Local site will run at:

http://127.0.0.1:8000/

# Deploying a Fork to Heroku

If you fork this project and want to deploy your version:

1. Create a new Heroku app  
   https://dashboard.heroku.com/apps

2. Add **Heroku Postgres**.

3. Open Settings → Reveal Config Vars and add:

```
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=<your-app>.herokuapp.com
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
STRIPE_PUBLIC_KEY=your_key
STRIPE_SECRET_KEY=your_key
STRIPE_WH_SECRET=your_key
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASS=your_password
```

4. Connect Heroku to your GitHub fork.
5. Ensure your fork contains a Procfile:

```
web: gunicorn mollavie.wsgi:application
```

6. Deploy the main branch.
7. Run migrations:

```
python manage.py migrate
python manage.py createsuperuser
```

Your fork is now live on Heroku.

## Contributing

If you have suggestions for new features or improvements to the site, please feel free to open an issue.
If you would like to contribute code, please fork the repository and create a pull request.

















































