from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import tensorflow as tf
import numpy as np
import os
import google.generativeai as genai
import base64
import time

# Path to your local image
image_path = "./web_app_imgs/background.jpg"

# Encode the image to base64
with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Create the CSS with enhanced styling for better readability and appearance
page_element = f"""
<style>
[data-testid="stAppViewContainer"]{{
  background-image: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)), url("data:image/jpeg;base64,{encoded_string}");
  background-size: cover;
  background-attachment: fixed;
}}

/* Enhanced text styling for better readability */
.main .block-container {{
  background-color: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  padding: 2rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  margin: 1rem;
}}

/* Header styling */
h1, h2, h3 {{
  color: #2E7D32 !important;
  font-weight: 700 !important;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
  margin-bottom: 1rem !important;
}}

/* Paragraph and text styling */
p, div {{
  color: #1B5E20 !important;
  font-weight: 500 !important;
  line-height: 1.6 !important;
  font-size: 1.1rem !important;
}}

/* Sidebar styling */
.sidebar .sidebar-content {{
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  color: white;
  padding: 1rem;
}}

/* Sidebar selectbox styling */
.sidebar .stSelectbox > div > div {{
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
  border: 3px solid #4CAF50 !important;
  border-radius: 15px !important;
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.25) !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
  padding: 1rem 1.25rem !important;
  min-height: 60px !important;
  height: auto !important;
  position: relative !important;
  overflow: visible !important;
  display: flex !important;
  align-items: center !important;
}}

.sidebar .stSelectbox > div > div::before {{
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: -100% !important;
  width: 100% !important;
  height: 100% !important;
  background: linear-gradient(90deg, transparent, rgba(76, 175, 80, 0.1), transparent) !important;
  transition: left 0.5s ease !important;
}}

.sidebar .stSelectbox > div > div:hover::before {{
  left: 100% !important;
}}

.sidebar .stSelectbox > div > div:hover {{
  border-color: #66BB6A !important;
  box-shadow: 0 8px 25px rgba(76, 175, 80, 0.4) !important;
  transform: translateY(-3px) scale(1.02) !important;
  background: linear-gradient(135deg, #ffffff 0%, #e8f5e8 100%) !important;
}}

.sidebar .stSelectbox > div > div:focus-within {{
  border-color: #2E7D32 !important;
  box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.2) !important;
  transform: translateY(-1px) !important;
}}

/* Selectbox text styling */
.sidebar .stSelectbox > div > div > div {{
  color: #1B5E20 !important;
  font-weight: 700 !important;
  font-size: 1rem !important;
  padding: 0.75rem 0 !important;
  line-height: 1.4 !important;
  letter-spacing: 0.3px !important;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1) !important;
  overflow: visible !important;
  text-overflow: unset !important;
  white-space: normal !important;
  word-wrap: break-word !important;
  max-height: none !important;
  height: auto !important;
}}

/* Selectbox dropdown styling */
.sidebar .stSelectbox > div > div > div[data-baseweb="select"] {{
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
  border-radius: 12px !important;
  padding: 0.75rem !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
  overflow: visible !important;
  height: auto !important;
  min-height: auto !important;
}}

/* Additional text container fixes */
.sidebar .stSelectbox > div > div > div > div:first-child {{
  overflow: visible !important;
  text-overflow: unset !important;
  white-space: normal !important;
  height: auto !important;
  min-height: auto !important;
  max-height: none !important;
  line-height: 1.4 !important;
  padding: 0.25rem 0 !important;
}}

/* Dropdown arrow styling */
.sidebar .stSelectbox > div > div > div > div:last-child {{
  background: linear-gradient(45deg, #4CAF50, #66BB6A) !important;
  border-radius: 8px !important;
  padding: 0.25rem !important;
  margin-left: 0.5rem !important;
  box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3) !important;
  transition: all 0.3s ease !important;
}}

.sidebar .stSelectbox > div > div:hover > div > div:last-child {{
  background: linear-gradient(45deg, #66BB6A, #81C784) !important;
  transform: scale(1.1) !important;
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4) !important;
}}

/* Sidebar text styling */
.sidebar p, .sidebar h1, .sidebar h2, .sidebar h3 {{
  color: white !important;
}}

/* Button styling */
.stButton > button {{
  background: linear-gradient(45deg, #4CAF50, #2E7D32) !important;
  color: white !important;
  border: none !important;
  border-radius: 25px !important;
  padding: 0.75rem 2rem !important;
  font-weight: 600 !important;
  font-size: 1rem !important;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3) !important;
  transition: all 0.3s ease !important;
}}

.stButton > button:hover {{
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4) !important;
  background: linear-gradient(45deg, #66BB6A, #4CAF50) !important;
}}

/* File uploader styling */
.stFileUploader {{
  background: rgba(255, 255, 255, 0.9) !important;
  border-radius: 15px !important;
  padding: 1.5rem !important;
  border: 2px dashed #4CAF50 !important;
}}

/* Success message styling */
.stSuccess {{
  background: linear-gradient(45deg, #4CAF50, #66BB6A) !important;
  color: white !important;
  border-radius: 15px !important;
  padding: 1rem !important;
  font-weight: 600 !important;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3) !important;
}}

/* Text input styling */
.stTextInput > div > div > input {{
  border-radius: 10px !important;
  border: 2px solid #4CAF50 !important;
  padding: 0.75rem !important;
  font-size: 1rem !important;
}}

/* Selectbox styling */
.stSelectbox > div > div > div {{
  border-radius: 12px !important;
  border: 2px solid #4CAF50 !important;
  padding: 0.75rem 1rem !important;
  min-height: 50px !important;
  display: flex !important;
  align-items: center !important;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2) !important;
  transition: all 0.3s ease !important;
}}

.stSelectbox > div > div > div:hover {{
  border-color: #66BB6A !important;
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3) !important;
  transform: translateY(-2px) !important;
}}

.stSelectbox > div > div > div > div {{
  color: #1B5E20 !important;
  font-weight: 600 !important;
  font-size: 1rem !important;
  line-height: 1.3 !important;
  overflow: visible !important;
  text-overflow: unset !important;
  white-space: normal !important;
  letter-spacing: 0.3px !important;
}}

/* Image styling */
img {{
  border-radius: 15px !important;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15) !important;
}}

/* Spinner styling */
.stSpinner > div {{
  border-color: #4CAF50 !important;
}}

/* Chat history styling */
.chat-message {{
  background: rgba(76, 175, 80, 0.1) !important;
  border-radius: 10px !important;
  padding: 1rem !important;
  margin: 0.5rem 0 !important;
  border-left: 4px solid #4CAF50 !important;
}}

/* Custom scrollbar */
::-webkit-scrollbar {{
  width: 8px;
}}

::-webkit-scrollbar-track {{
  background: #f1f1f1;
  border-radius: 10px;
}}

::-webkit-scrollbar-thumb {{
  background: #4CAF50;
  border-radius: 10px;
}}

::-webkit-scrollbar-thumb:hover {{
  background: #2E7D32;
}}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(page_element, unsafe_allow_html=True)


# tensorflow model prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model('./trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) # to convert single image to a batch
    prediction = model.predict([input_arr])
    result_index = np.argmax(prediction)
    return result_index

# Sidebar with clean design - only selection box
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem 0;">
    <h2 style="color: #4CAF50; margin-bottom: 0.5rem; font-size: 1.5rem;">🌱 IndiGro</h2>
    <p style="color: #81C784; font-size: 0.8rem; margin: 0;">AI-Powered Plant Disease Detection</p>
</div>
""", unsafe_allow_html=True)

app_mode = st.sidebar.selectbox("Select Page", ["Home", "About Us", "Disease Recognition", "Chat With Us!"])

# Home Page
if (app_mode=="Home"):
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #2E7D32; font-size: 3rem; margin-bottom: 1rem;">🌱 IndiGro</h1>
        <h2 style="color: #1B5E20; font-size: 1.5rem; margin-bottom: 2rem;">Predict. Prevent. Prosper.</h2>
        <p style="color: #1B5E20; font-size: 1.2rem; margin-bottom: 2rem;">Revolutionizing crop protection with AI-powered disease detection</p>
    </div>
    """, unsafe_allow_html=True)
    
    image_path = "./web_app_imgs/home1.jpg"
    st.image(image_path, use_container_width=True)
    st.markdown("""
    
    ### 🪴Our Mission
    At IndiGro, our mission is to revolutionize crop protection by empowering farmers with cutting-edge AI-powered disease diagnosis. We aim to provide farmers with a fast, reliable, and cost-effective solution for identifying plant diseases in their fields, enabling them to take timely action to minimize crop losses and maximize yields. By harnessing the power of technology, we strive to contribute to food security, sustainable farming practices, and the overall profitability of agricultural operations.
    
    ### 🏹How It Works?
    1. **Upload Images:** Simply upload the images to our platform.
    2. **AI Analysis:** Our AI model, trained on extensive data, analyzes the images to identify the presence of diseases in crops.
    3. **Rapid Diagnosis:** Our AI-powered system provides instant disease diagnosis, allowing you to act swiftly to protect your crops.
    4. **Take Action:** Armed with this information, farmers can take swift and targeted action to control the spread of disease and optimize their harvest.
    
    ### ✨Why Choose Us?
    1. **Swift Diagnosis:** Our AI-powered system swiftly identifies diseases, enabling prompt action to safeguard your crops.
    2. **Unrivaled Accuracy:** Backed by extensive datasets, our model ensures precise detection of plant diseases.
    3. **Cost-effective Solution:** Save valuable time and resources with our efficient approach compared to traditional lab testing.
    4. **Empowering Farmers:** We equip farmers with advanced technology, empowering them to make informed decisions and enhance their farm management practices.
    
    ### 🪴Get Started 
    At IndiGro, we are a team of passionate students dedicated to applying the latest advancements in AI and machine learning to tackle critical issues in agriculture. With a blend of expertise in AI, agriculture, and data science, we are committed to crafting innovative solutions to empower farmers and bolster food security globally. Our relentless pursuit of excellence motivates us to refine and enhance our platform continually, ensuring that farmers have the necessary tools and resources to thrive in today's dynamic agricultural environment. Join us on our journey to revolutionize crop protection and shape the future of farming.
    
    """)
    
# About Page
elif (app_mode=="About Us"):
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; margin-bottom: 1rem;">👥 About Us</h1>
        <p style="color: #1B5E20; font-size: 1.2rem;">Meet the team behind IndiGro</p>
    </div>
    """, unsafe_allow_html=True)
    
    image_path = "./web_app_imgs/about.jpg"
    st.image(image_path, use_container_width=True)
    
    st.markdown("""
    
    At IndiGro, our team is comprised of driven and passionate students who are united by a common goal: harnessing the latest advancements in artificial intelligence (AI) and machine learning to tackle the critical issues facing agriculture today. 🌱 With a unique blend of expertise spanning AI, agriculture, and data science, we are deeply committed to developing innovative solutions that not only empower farmers but also contribute to the global efforts aimed at enhancing food security. 🌍

    Our relentless pursuit of excellence serves as the driving force behind our work. We are dedicated to continually refining and enhancing our platform, ensuring that it remains at the forefront of agricultural technology. By providing farmers with access to cutting-edge tools and resources, we aim to equip them with the necessary means to thrive in today's rapidly evolving agricultural landscape. 🚜

    In our pursuit of excellence, we have trained our AI model on an extensive dataset consisting of 35,406 training images, meticulously curated to ensure optimal performance. Additionally, we have rigorously validated our model using 17,572 validation images, further enhancing its accuracy and reliability. With a thorough testing phase that includes 33 images, we are confident in the effectiveness of our solution and its potential to revolutionize crop protection practices worldwide. 📊 Join us as we embark on this transformative journey to revolutionize crop protection and pave the way for a more sustainable and prosperous future in farming. 🌟
    
    """)
    
# Prediction Page
elif (app_mode=="Disease Recognition"):
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; margin-bottom: 0.5rem;">🔍 Disease Recognition</h1>
        <p style="color: #1B5E20; font-size: 1.2rem;">Upload a plant image to detect diseases using our AI model</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📸 Upload Image")
        test_image = st.file_uploader("Choose a plant image:", type=['jpg', 'jpeg', 'png'])
        
        if test_image:
            st.markdown("### 👀 Preview")
            st.image(test_image, use_container_width=True)
    
    with col2:
        st.markdown("### 🤖 AI Analysis")
        if test_image:
            if st.button("🔍 Analyze Disease", type="primary"):
                with st.spinner('🔄 Analyzing image with AI...'):
                    time.sleep(2)
                
                st.markdown("### 📊 Results")
                result_index = model_prediction(test_image)
                
                # Define Class
                class_name = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']
                
                # Enhanced result display
                disease_name = class_name[result_index]
                if "healthy" in disease_name.lower():
                    st.markdown(f"""
                    <div style="background: linear-gradient(45deg, #4CAF50, #66BB6A); color: white; padding: 1rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);">
                        <h3 style="color: white; margin-bottom: 0.5rem;">🌿 Healthy Plant Detected!</h3>
                        <p style="color: white; font-size: 1.1rem;">The plant appears to be in good health.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background: linear-gradient(45deg, #f44336, #e53935); color: white; padding: 1rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(244, 67, 54, 0.3);">
                        <h3 style="color: white; margin-bottom: 0.5rem;">⚠️ Disease Detected</h3>
                        <p style="color: white; font-size: 1.1rem;">The plant appears to have: <strong>{disease_name.replace('___', ' - ')}</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Add recommendations
                st.markdown("### 💡 Recommendations")
                if "healthy" in disease_name.lower():
                    st.info("✅ Continue with your current care routine. Regular monitoring is recommended.")
                else:
                    st.warning("🔧 Consider consulting with an agricultural expert for treatment options.")
        
# Chat With Us Page
elif (app_mode=="Chat With Us!"):
    
    # Check if API key is available
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key or api_key == "your_google_api_key_here":
        st.markdown("""
        <div style="background: linear-gradient(45deg, #ff9800, #f57c00); color: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(255, 152, 0, 0.3);">
            <h3 style="color: white; margin-bottom: 1rem;">🔑 API Key Required</h3>
            <p style="color: white; font-size: 1.1rem; margin-bottom: 1rem;">To use the chat feature, you need to set up a Google API key.</p>
            <div style="background: rgba(255, 255, 255, 0.1); padding: 1rem; border-radius: 10px; margin: 1rem 0;">
                <h4 style="color: white; margin-bottom: 0.5rem;">📋 Setup Instructions:</h4>
                <ol style="color: white; text-align: left; margin: 0; padding-left: 2rem;">
                    <li>Go to <a href="https://makersuite.google.com/app/apikey" target="_blank" style="color: #fff3e0; text-decoration: underline;">Google AI Studio</a></li>
                    <li>Sign in with your Google account</li>
                    <li>Click "Create API Key"</li>
                    <li>Copy the generated API key</li>
                    <li>Create a <code>.env</code> file in the project root</li>
                    <li>Add: <code>GOOGLE_API_KEY=your_actual_api_key_here</code></li>
                    <li>Restart the application</li>
                </ol>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Alternative: Manual API key input
        st.markdown("### 🔧 Quick Setup (Alternative)")
        manual_api_key = st.text_input("Enter your Google API Key:", type="password", help="Get your API key from https://makersuite.google.com/app/apikey")
        
        if manual_api_key:
            # Store in session state for this session
            st.session_state['manual_api_key'] = manual_api_key
            st.success("✅ API key set! You can now use the chat feature.")
            st.rerun()
            
    else:
        # API key is available, proceed with chat functionality
        try:
            # Use manual API key if available in session state
            if 'manual_api_key' in st.session_state:
                genai.configure(api_key=st.session_state['manual_api_key'])
            else:
                genai.configure(api_key=api_key)
            
            # function to load Gemini Pro model and get response
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            def get_gemini_response(question):
                try:
                    response = model.generate_content(question)
                    return response.text
                except Exception as e:
                    return f"Sorry, I encountered an error: {str(e)}"
            
            # initialize streamlit app
            st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h1 style="color: #2E7D32; font-size: 2.5rem; margin-bottom: 1rem;">💬 Chat With Us!</h1>
                <p style="color: #1B5E20; font-size: 1.2rem;">Get instant answers about plant care and disease prevention</p>
            </div>
            """, unsafe_allow_html=True)
            
            # initialize session state for chat history if it doesn't exist
            if 'chat_history' not in st.session_state:
               st.session_state['chat_history'] = []
               
            input = st.text_input("Ask me Something! ", key="input", placeholder="Ask about plant diseases, care tips, or agricultural advice...")
            submit = st.button("🚀 Send Message", type="primary")
            
            if submit and input:
                with st.spinner('🤖 Getting response from AI...'):
                    response = get_gemini_response(input)
                    
                # add user query and response to session chat history
                st.session_state['chat_history'].append(("You", input))
                
                st.markdown("### 💬 AI Response")
                if isinstance(response, str) and response.startswith("Sorry, I encountered an error"):
                    st.markdown(f"""
                    <div style="background: linear-gradient(45deg, #f44336, #e53935); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                        <p style="color: white; margin: 0;">{response}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.session_state['chat_history'].append(("Bot", response))
                else:
                    st.markdown(f"""
                    <div style="background: linear-gradient(45deg, #4CAF50, #66BB6A); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                        <p style="color: white; margin: 0;">{response}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.session_state['chat_history'].append(("Bot", response))
            
            # Display chat history
            if st.session_state['chat_history']:
                st.markdown("### 📚 Chat History")
                for role, text in st.session_state['chat_history']:
                    if role == "You":
                        st.markdown(f"""
                        <div style="background: rgba(76, 175, 80, 0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #4CAF50;">
                            <strong>👤 You:</strong> {text}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background: rgba(33, 150, 243, 0.1); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #2196F3;">
                            <strong>🤖 AI:</strong> {text}
                        </div>
                        """, unsafe_allow_html=True)
            
            # Clear chat button
            if st.button("🗑️ Clear Chat History"):
                st.session_state['chat_history'] = []
                st.rerun()
                
        except Exception as e:
            st.error(f"❌ Error initializing chat: {str(e)}")
            st.info("Please check your API key configuration.") 