from contacts_manager import validate_phone, validate_email

def run_tests():
    print("🧪 Running Validation Tests...")
    
    # Test Phone Validation
    assert validate_phone("1234567890")[0] == True
    assert validate_phone("123")[0] == False
    print("✅ Phone validation passed!")

    # Test Email Validation
    assert validate_email("test@example.com") == True
    assert validate_email("invalid-email") == False
    print("✅ Email validation passed!")

    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    run_tests()