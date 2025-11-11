import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from view.login_view import LoginApp



if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()


 