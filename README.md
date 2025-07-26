# 🌱 IndiGro: Predict. Prevent. Prosper.

**AI-Powered Plant Disease Detection System**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-orange.svg)](https://tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [API Integration](#api-integration)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

IndiGro is an innovative AI-powered web application designed to revolutionize crop protection by providing instant plant disease detection. Our mission is to empower farmers with cutting-edge technology that enables swift, accurate, and cost-effective disease diagnosis, ultimately contributing to food security and sustainable farming practices.

### 🎯 Mission
To revolutionize crop protection by empowering farmers with cutting-edge AI-powered disease diagnosis, enabling them to take timely action to minimize crop losses and maximize yields.

## ✨ Features

### 🔍 **Disease Recognition**
- **Instant Detection**: Upload plant images and get immediate disease diagnosis
- **High Accuracy**: Trained on 35,406+ images across 38 disease categories
- **Multiple Crops**: Supports Apple, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, and Tomato
- **User-Friendly**: Simple drag-and-drop interface for image upload

### 💬 **AI Chat Assistant**
- **Smart Conversations**: Powered by Google Gemini 1.5 Flash
- **Agricultural Advice**: Get instant answers about plant care and disease prevention
- **Chat History**: Maintain conversation history for reference
- **Real-time Responses**: Quick and accurate agricultural guidance

### 🎨 **Modern User Interface**
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Beautiful UI**: Modern gradient backgrounds and enhanced styling
- **Intuitive Navigation**: Easy-to-use sidebar navigation
- **Professional Look**: Clean, professional appearance with green theme

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **AI/ML**: TensorFlow 2.13+, Keras
- **Image Processing**: OpenCV, PIL
- **AI Chat**: Google Generative AI (Gemini)
- **Data Processing**: NumPy, Pandas
- **Environment**: Python-dotenv

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/IndiGro-Predict-Prevent-Prosper.git
cd IndiGro-Predict-Prevent-Prosper
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

**To get your Google API key:**
1. Visit [Google MakerSuite](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy and paste it in the `.env` file

### Step 4: Run the Application
```bash
streamlit run main.py
```

The application will open at `http://localhost:8501`

## 🚀 Usage

### 1. **Home Page**
- Overview of the project and mission
- Information about how the system works
- Key benefits and features

### 2. **Disease Recognition**
1. Navigate to "Disease Recognition" from the sidebar
2. Click "Choose a plant image" to upload your image
3. Supported formats: JPG, JPEG, PNG
4. View the preview of your uploaded image
5. Click "Predict Disease" to get instant results
6. Review the prediction with confidence score

### 3. **Chat Assistant**
1. Navigate to "Chat With Us!" from the sidebar
2. Enter your question about plant care or diseases
3. Click "Send Message" to get AI-powered advice
4. View chat history for previous conversations
5. Use "Clear Chat History" to start fresh

### 4. **About Us**
- Learn about the team behind IndiGro
- Project statistics and achievements
- Technical details and dataset information

## 📊 Dataset

Our model is trained on a comprehensive dataset:

- **Training Images**: 35,406 images
- **Validation Images**: 17,572 images
- **Test Images**: 33 images
- **Total Classes**: 38 disease categories
- **Image Size**: 128x128 RGB
- **Crops Covered**: 12 different plant types

### Supported Crops and Diseases:
- **Apple**: Apple scab, Black rot, Cedar apple rust, Healthy
- **Corn**: Cercospora leaf spot, Common rust, Northern Leaf Blight, Healthy
- **Grape**: Black rot, Esca, Leaf blight, Healthy
- **Tomato**: Bacterial spot, Early blight, Late blight, Leaf Mold, Septoria leaf spot, Spider mites, Target Spot, Yellow Leaf Curl Virus, Mosaic virus, Healthy
- **And many more...**

## 🧠 Model Architecture

### CNN Architecture
```python
# Convolutional Neural Network Structure
- Input Layer: 128x128x3 RGB images
- Conv2D Layers: 5 blocks (32→64→128→256→512 filters)
- MaxPooling: Dimension reduction after each conv block
- Dropout: 0.25 and 0.4 for regularization
- Dense Layers: 1500 neurons with ReLU activation
- Output Layer: 38 classes with Softmax activation
```

### Training Details
- **Optimizer**: Adam (learning rate: 0.0001)
- **Loss Function**: Categorical Crossentropy
- **Epochs**: 5
- **Batch Size**: 32
- **Model Size**: ~90MB

## 🔌 API Integration

### Google Gemini Integration
The chat feature uses Google's Gemini 1.5 Flash model for intelligent agricultural advice:

```python
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(question)
    return response.text
```

## 📸 Screenshots

*[Add screenshots of your application here]*

## 🤝 Contributing

We welcome contributions to improve IndiGro! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Contribution:
- Model improvement and optimization
- Additional crop and disease support
- UI/UX enhancements
- Documentation improvements
- Bug fixes and performance optimization

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: PlantVillage dataset for training images
- **Google**: Gemini API for intelligent chat assistance
- **Streamlit**: For the beautiful web interface
- **TensorFlow**: For the powerful deep learning framework
- **Open Source Community**: For various libraries and tools


**🌱 Together, let's revolutionize crop protection and shape the future of farming!**

*Made with ❤️ for sustainable agriculture*