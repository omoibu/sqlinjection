**NOTE:** manage.py is always in the root directory with requirements.py and use ctrl/cmd+shift+v to view the markdown

Here's your content formatted properly in markdown:

---

### Environment Setup

1. **Install Python**
   - Download the Python installer from [Python 3.12.8](https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe).
   - During installation:
     - Click **"Run as Administrator"** to ensure necessary privileges.
     - Check the option to **"Add Python to PATH"**.
     - Choose **"Customize installation"** for advanced options and proceed.

---

### Project Setup

1. **Verify `manage.py` in Your Current Directory**
   - Run the following command to check if `manage.py` is in your directory:
     - **Linux/macOS**: `ls`
     - **Windows**: `dir`

2. **Navigate to the Correct Directory (if necessary)**
   - If `manage.py` is not in your current folder, use the following commands to navigate:
     - **Move forward**: `cd <directory_name>`
     - **Move backward**: `cd ..`

3. **Install Project Dependencies**
   - Run the following command to install all dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Database Configuration**
   - Open `settings.py` and configure the database settings as needed.
   - For a list of supported databases, refer to the [Django database documentation](https://docs.djangoproject.com/en/stable/ref/databases/).

5. **Create Migrations**
   - Run the following command to generate a snapshot of the models:
     ```bash
     python manage.py makemigrations
     ```

6. **Apply Migrations**
   - Run the following command to apply the migrations and update the database:
     ```bash
     python manage.py migrate
     ```

7. **Start the Development Server**
   - To run the server, use the following command:
     ```bash
     python manage.py runserver
     ```

---

**Note:** Ensure that you are in the root directory (where `manage.py` is located) to run the server and make migrations.
