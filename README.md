# BackendFAQProject
# 📌 FAQ Management System  

A **Django-based FAQ Management System** that supports **multilingual FAQs** with a **WYSIWYG editor**, **REST API**, and **caching** using Redis.  

---

## 🚀 Features  

✅ Store FAQs with **question and answer fields**  
✅ Supports **multiple languages** (automatic translation)  
✅ **WYSIWYG Editor** for rich text answers  
✅ REST API for CRUD operations  
✅ **Language selection** via `?lang=` query parameter  
✅ **Caching** for optimized performance (Redis)  
✅ **Admin panel** for FAQ management  
✅ **Docker support** for containerization  
✅ **Unit tests** for reliability  


## **Clone the Repository**  

git clone https://github.com/GayathriManchikanti/BackendFAQProject.git
cd FAQ_Project

## **Apply Migrations & Create Superuser**

python manage.py migrate
python manage.py createsuperuser

## **Run the server**

python manage.py runserver

## API Endpoints
### ** Get All FAQs (Default Language: English)**

GET /api/faqs/
### **Get FAQs in a Specific Language**

GET /api/faqs/?lang=hi
### **Create a New FAQ**

POST /api/faqs/

##Running Tests
pytest FAQ/tests/






