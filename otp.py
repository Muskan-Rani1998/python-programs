import random

class OTP:
    def __init__(self):
        self.otp = None
    
    def generate_otp(self):
        """Generate a six-digit OTP."""
        self.otp = random.randint(100000, 999999)
        return self.otp
    
    def validate_otp(self, user_otp):
        """Validate the provided OTP against the generated OTP."""
        if self.otp is None:
            return False, "No OTP generated."
        return self.otp == user_otp, "OTP is valid." if self.otp == user_otp else "OTP is invalid."
    
    def display_otp(self):
        """Display the generated OTP."""
        if self.otp is not None:
            return f"Your OTP is: {self.otp}"
        else:
            return "No OTP has been generated."

# Example usage
if __name__ == "__main__":
    otp_system = OTP()
    
    # Generate and display OTP
    generated_otp = otp_system.generate_otp()
    print(otp_system.display_otp())
    
    # Simulate user input
    user_input = int(input("Enter the OTP you received: "))
    
    # Validate OTP
    is_valid, message = otp_system.validate_otp(user_input)
    print(message)
