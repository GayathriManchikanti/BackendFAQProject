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


### **Clone the Repository**  
```bash
git clone https://github.com/GayathriManchikanti/BackendFAQProject.git
cd FAQ_Project

## **Apply Migrations & Create Superuser**
```bash
python manage.py migrate
python manage.py createsuperuser

## **Run the server**
```bash
python manage.py runserver

## API Endpoints
### ** Get All FAQs (Default Language: English)**
```bash
GET /api/faqs/
### **Get FAQs in a Specific Language**
```bash
GET /api/faqs/?lang=hi
### **Create a New FAQ**
```bash
POST /api/faqs/

##Running Tests
```bash
pytest FAQ/tests/






