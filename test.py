import google.generativeai as genai

# Configure the API key for Gemini
genai.configure(api_key="")  # API key removed

try:
    # Initialize the Gemini model
    model = genai.GenerativeModel('gemini-pro')
    
    # Generate content using Gemini
    response = model.generate_content("Say hello")
    
    print("✅ API key is working!")
    print("Response:", response.text)

except Exception as e:
    if "API_KEY_INVALID" in str(e) or "invalid API key" in str(e).lower():
        print("❌ Invalid API key.")
    else:
        print("⚠️ Something went wrong:", str(e))
