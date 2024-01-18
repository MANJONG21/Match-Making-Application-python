#Login.py

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from Mainpage import MainScreen
import sqlite3



class LoginScreen(QMainWindow):
    def __init__(self, widget):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.widget = widget

        ### HIDING THE PASSWORD FIELD ###
        self.Password_LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        ###### LOGIN BUTTON TRIGGER THAT LEADS TO MAINPAGE ####
        self.login_pushButton.clicked.connect(self.Login)
        

    ####################################################################################
    ##          FUNCTION THAT CHECKS IF THE USER INFO IS FOUND IN THE DATABASE        ##
    ####################################################################################

    #17 Function that checks if the user info is found in the database
def checkInfoinDatabase(self, username, password):
try:
# Step 1: Connect to the usersInfo database
self.conn = sqlite3.connect(&quot;usersInfo.db&quot;)
self.cursor = self.conn.cursor()

# Step 2: Execute a SQL query to select user information based on the provided username and
password
self.cursor.execute(&#39;&#39;&#39;
SELECT Username, Email, Password, PhoneNumber, Age, Location, Gender FROM Users
WHERE Username = ? AND Password = ?
&#39;&#39;&#39;, (username, password))

# Step 3: Fetch the result of the query
result = self.cursor.fetchone()

# Step 4: Close the database connection
self.conn.close()

# Step 5: Return the result (user information)
return result

except Exception as e:
# Step 6: Handle any exceptions that might occur during the process
print(f&quot;Error in checkInfoinDatabase method: {str(e)}&quot;)
return None # Return None in case of an error
    

    #####################################################################################
    ##             FUNCTION CHECKS IF THE INPUT FIELD HAVE BEEN ENTERED ALL            ##
    #####################################################################################

    def checkInputFields(self, username, password):
       try:
        # Step 1: Check if either the username or password is missing
        if not username or not password:
            # Step 2: Check which field is missing and update the login_error_label accordingly
            if not username:
                self.login_error_label.setText("Username is required!")
            elif not password:
                self.login_error_label.setText("Password is required!")

            # Step 3: Return False indicating that the input fields are not complete
            return False

        # Step 4: If both username and password are present, return True indicating that the input fields are complete
        return True

    except Exception as e:
        # Step 5: Handle any exceptions that might occur during the process
        print(f"Error in checkInputFields method: {str(e)}")
        return False  # Return False in case of an error

    #####################################################################################
    ##                  LOGIN FUNCTION THAT LEADS TO THE MAINPAGE                      ##
    #####################################################################################

    def Login(self):
        pass



