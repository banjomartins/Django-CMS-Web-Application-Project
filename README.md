# Django CMS Web Application

A Django-based web application with a built-in Content Management System (CMS) managed through the Django Admin interface. This project demonstrates how to build a full-stack application with authentication, CRUD operations, and admin-controlled content management.

## 🚀 Features

### Public Pages
- **Home Page** – Landing page with general information about the site
- **Contact Page** – A static page with contact details

### User Management (Frontend)
- **Registration & Login** – Users must sign up and log in to access protected pages
- **User Information Form** – A page where logged-in users can submit their details:
  - Name (from Django User model)
  - Age
  - City
  - Hobby
  - Favorite Food
- **User List Page** – Displays a list of all submitted users with the following options:
  - **Update** – Opens a pre-filled form where the user can update details. On submit, the user is redirected back to the list page
  - **Delete** – Deletes the selected user and redirects back to the list page (admin only)

### Product Management (Frontend & Admin)
- **Product List Page** – Logged-in users can view all available products
- **Admin Control** – From the Django Admin panel:
  - Add/Edit/Delete Users
  - Add/Edit/Delete Products with the following fields:
    - Product Name
    - Price
    - Description
    - Photo
    - Availability (is_available: Yes/No)

### Authentication & Permissions
- Only authenticated users can access:
  - User form page
  - User list page
  - Product list page
- Public pages (Home and Contact) are open for everyone
- Users can only update their own information (unless they're superusers)
- Only superusers can delete user information

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation / Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd BabloDjango/finalproject
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 💻 Usage / Examples

### For Regular Users

1. **Sign Up**: Visit `/signup/` to create a new account
2. **Log In**: Use your credentials to access protected pages
3. **Submit Information**: Go to `/user-form/` to fill out your profile details
4. **View Users**: Visit `/users/` to see all registered users
5. **View Products**: Go to `/products/` to browse available products
6. **Update Profile**: Click "Update" next to your name in the user list

### For Administrators

1. **Access Admin Panel**: Go to `/admin/` and log in with superuser credentials
2. **Manage Users**: Add, edit, or delete user accounts
3. **Manage Products**: Add products with photos, set prices, and manage availability
4. **Delete User Information**: Remove user profiles from the system

### Example Workflow

```bash
# 1. Start the server
python manage.py runserver

# 2. Visit the home page
# http://127.0.0.1:8000/

# 3. Sign up for a new account
# http://127.0.0.1:8000/signup/

# 4. Fill out your profile
# http://127.0.0.1:8000/user-form/

# 5. View all users
# http://127.0.0.1:8000/users/

# 6. Browse products
# http://127.0.0.1:8000/products/
```

## 🏗️ Project Structure

```
finalproject/
├── finalproject/           # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py           # Main URL routing
│   └── ...
├── main_app/             # Main application
│   ├── models.py         # Database models (UserInfo, Product)
│   ├── views.py          # View functions
│   ├── forms.py          # Django forms
│   ├── urls.py           # App URL routing
│   ├── admin.py          # Admin configuration
│   └── templates/        # HTML templates
├── media/                # User uploaded files
│   └── product_photos/   # Product images
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## 🎯 Learning Outcomes

By completing this project, students will learn how to:

- Build Django models, views, templates, and forms
- Implement CRUD functionality (Create, Read, Update, Delete)
- Use Django Admin for CMS features
- Handle user authentication and session management
- Restrict access to certain views with login requirements
- Manage media uploads (product photos)
- Implement proper permission systems
- Work with Django's built-in User model
- Handle form validation and error messages

## 🔧 Technical Details

### Models
- **UserInfo**: Extended user profile with age, city, hobby, and favorite food
- **Product**: Product catalog with name, price, description, photo, and availability

### Key Features
- **Authentication**: Built-in Django user authentication
- **Media Handling**: Image uploads for product photos
- **Permission System**: Role-based access control
- **Form Validation**: Client and server-side validation
- **Responsive Design**: Mobile-friendly templates

### Dependencies
- Django 5.2.6
- Pillow 11.3.0 (for image handling)
- asgiref 3.9.1
- sqlparse 0.5.3
- tzdata 2025.2

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions, please:
1. Check the Django documentation
2. Review the code comments
3. Create an issue in the repository
4. Contact the development team

---

**Happy Coding! 🎉**
