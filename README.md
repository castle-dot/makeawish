# Make-A-Wish App ✨

A fun Django web application where users can share their dreams and hopes with the community.

## ✨ Features
- User authentication (register/login)
- Create, view, and browse wishes
- Clean and responsive UI
- Admin panel for management

## 🛠 Tech Stack
- Python + Django
- SQLite / PostgreSQL
- HTML, CSS, Bootstrap
- Django templates

## 🚀 Live Demo
*(Previously deployed on Render — redeploying soon)*  
<img width="1920" height="987" alt="Screenshot (169)" src="https://github.com/user-attachments/assets/807e9d7d-7f28-41f1-bb00-058cdd2c4b14" />
<img width="1920" height="984" alt="Screenshot (170)" src="https://github.com/user-attachments/assets/d31cda29-4bc9-4791-8dbf-e9a9022c0613" />
<img width="1920" height="989" alt="Screenshot (171)" src="https://github.com/user-attachments/assets/c5a19913-c959-4392-951f-9dd3b0c6380f" />
<img width="1920" height="939" alt="Screenshot (172)" src="https://github.com/user-attachments/assets/0642f2aa-c90e-4924-a3f3-a3c7043a15fe" />
<img width="1920" height="983" alt="Screenshot (168)" src="https://github.com/user-attachments/assets/71350dc6-71b3-4075-8bfb-1fbeafc6eeea" />


## 🏃‍♂️ How to Run Locally
```bash
git clone https://github.com/castle-dot/makeawish.git
cd makeawish
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
