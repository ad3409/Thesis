Prerequisites
Ensure that you have the following installed on your system:
• Python (version 3.x or above)
• Node.js (version 14.x or above)
If these are not installed, please download and install them from the official
websites:
• Python Download
• Node.js Download
Frontend Setup
1. Navigate to the Frontend Directory: Open a terminal and change your work-
ing directory to the frontend folder of the project:
cd path/to/frontend
2. Install Dependencies: Run the following command to install the necessary
packages using npm (Node Package Manager):
npm install
3. Start the Development Server: Once the dependencies are installed, start the
frontend development server:
npm run dev
4. Access the Application: After running the server, open a browser and visit
the local URL:
http://localhost:5303
5. Modify URL to Access AIChat API: Change the URL to access the AIChat
API endpoint:
http://localhost:5303/AIChat
This will bring you to the AIChat UI, where you can interact with the chatbot.

Backend Setup
1. Navigate to the Backend Directory: Open a new terminal window and change
your working directory to the backend folder:
cd path/to/backend
2. Install Python Dependencies: Install the necessary Python packages as speci-
fied in the requirements.txt file:
pip install -r requirements.txt
3. Database Migrations: Run the following commands to apply database migra-
tions:
python manage.py makemigrations
python manage.py migrate
4. Start the Backend Server: Run the server to start the backend:
python manage.py runserver
Using the Chatbot UI
1. Open the Chatbot UI: Once both the frontend and backend servers are run-
ning, you can interact with the AIChat API through the UI hosted at:
http://localhost:5303/AIChat
2. Start the Conversation: Begin interacting with the chatbot UI by typing your
queries or commands.
