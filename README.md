# Vision Assistant

A comprehensive computer vision assistant project that leverages Google's PaliGemma model for advanced image understanding and analysis. This application combines OCR (Optical Character Recognition), image captioning, visual question answering, and text-to-speech capabilities in an easy-to-use GUI interface.

## 🌟 Features

- **Image Analysis**: Generate detailed captions for any image
- **Optical Character Recognition (OCR)**: Extract text from images
- **Visual Question Answering**: Ask questions about image content
- **Text-to-Speech**: Listen to the assistant's responses
- **Speech Recognition**: Ask questions using your voice
- **Translation Support**: Translate captions to Hindi
- **User-friendly GUI**: Simple interface for all functionalities

## 🖼️ Demo

![Vision Assistant Demo](test.jpg)

*Example image used for demonstration*

## 🚀 Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Tesseract OCR installed on your system (for text extraction)
  - [Download Tesseract OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
  - [Download Tesseract OCR for macOS](https://tesseract-ocr.github.io/tessdoc/Installation.html)
  - For Linux: `sudo apt install tesseract-ocr`
  - Ensure Tesseract is added to your system PATH
- Microphone (for speech recognition features)
- Speakers (for text-to-speech output)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pavankalyan32/vision-assistant.git
   cd vision-assistant
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv vision-env
   # On Windows
   vision-env\Scripts\activate
   # On macOS/Linux
   source vision-env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the PaliGemma model**
   ```bash
   python download_model.py
   ```
   *Note: This will download approximately 3GB of model files to a local directory. The download may take some time depending on your internet connection.*

   **System Requirements for Model:**
   - At least 8GB RAM (16GB recommended)
   - At least 5GB free disk space
   - GPU acceleration is optional but recommended for faster processing

5. **Run the application**
   ```bash
   python vision_assistant_gui.py
   ```

## 💻 Usage

1. **Upload an Image**: Click the "Upload Image" button to select an image from your computer
2. **Describe Image**: Generate a detailed caption for the uploaded image
3. **Extract Text**: Use OCR to extract any text visible in the image
4. **Ask a Question**: Type or speak a question about the image content
5. **Translate**: Translate the generated caption to Hindi

### Testing with Sample Images

The repository includes a sample image (`test.jpg`) that you can use to test the application's functionality. To test with this image:

1. Run the application: `python vision_assistant_gui.py`
2. Click "Upload Image" and navigate to the `test.jpg` file in the project directory
3. Try each of the features (Describe, OCR, Ask Question) with this image

You can also test with your own images by uploading them through the GUI.

## 🔧 Project Structure

- **`vision_assistant_gui.py`**: Main GUI application built with Tkinter
- **`gemma_vision_assistant.py`**: Core functionality for image processing and analysis
- **`gemma_test.py`**: Testing script for the PaliGemma model implementation
- **`download_model.py`**: Script to download and save the PaliGemma model locally
- **`requirements.txt`**: List of Python dependencies
- **`test.jpg`**: Sample image for testing

## 🧠 How It Works

1. **Image Processing**: The application loads and processes images using OpenCV and PIL
2. **Text Extraction**: Tesseract OCR extracts any text present in the image
3. **Image Understanding**: The PaliGemma model generates detailed captions
4. **Question Answering**: Combines extracted text and captions to answer questions
5. **Speech Synthesis**: Converts text responses to speech using pyttsx3

## 🛠️ Technologies Used

- **PaliGemma**: Google's multimodal model for image understanding
- **Transformers**: Hugging Face library for accessing and using AI models
- **PyTesseract**: OCR engine for text extraction
- **OpenCV & PIL**: Image processing libraries
- **pyttsx3**: Text-to-speech conversion
- **SpeechRecognition**: Voice input processing
- **Tkinter**: GUI framework
- **Googletrans**: Translation capabilities

## ⚠️ Limitations

- The model requires significant memory (at least 8GB RAM recommended)
- Processing large or complex images may take time
- OCR accuracy depends on image quality and text clarity
- Internet connection required for speech recognition and translation

## 🔍 Troubleshooting

### Common Issues

1. **Tesseract OCR Not Found**
   - Ensure Tesseract is installed and added to your system PATH
   - You can specify the Tesseract path directly in the code by uncommenting and modifying this line in `gemma_vision_assistant.py`:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```

2. **Out of Memory Errors**
   - Close other memory-intensive applications
   - Try using a smaller image
   - If available, enable swap space or virtual memory

3. **Speech Recognition Not Working**
   - Check that your microphone is properly connected and has necessary permissions
   - Ensure you have an active internet connection (required for Google's speech recognition)
   - Try speaking clearly and in a quiet environment

4. **Model Download Failures**
   - Check your internet connection
   - Try running the download script again
   - If persistent, download the model files manually from Hugging Face and place them in the `paligemma-3b-mix-224` directory

## 🚀 Future Enhancements

- Support for video analysis and understanding
- Integration with more languages for translation
- Improved OCR accuracy for complex documents
- Support for batch processing multiple images
- Enhanced UI with dark mode and customization options
- Mobile application version

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

To contribute to this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgements

- Google for the PaliGemma model
- Hugging Face for the Transformers library
- The open-source community for various libraries used in this project
  
