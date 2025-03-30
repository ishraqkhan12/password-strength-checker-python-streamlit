import streamlit as st
import re 


def check_password_strength(password):
    if len(password)<8 :
      return "❌weak: Password must be at least 8 charcters long "
    
    if not any(char.isdigit() for char in password):
       return "❌weak: Password must include at least one digit"
    
    if not any(char.islower() for char in password):
       return "❌weak: Password must include at least one lowercase letter"
    
    if not any(char.isupper() for char in password):
       return "❌weak: Password must include at least one uppercase letter"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|_-<>]', password):
        return "⚠️ Medium: Add special characters to make your password stronger."
    
    else:
       return " ✔ Strong: Your password is secure"
    
def password_checker():
   
   st.title("🔐Password Strength Checker")
   
  
   password = st.text_input("Enter your password", type="password")

      
     
   if password:
    result = check_password_strength(password)
    st.write(result)

   else:
      st.write("❗Please enter your password")

if __name__ == "__main__":
 password_checker()
