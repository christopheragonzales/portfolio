# Domains of AI
---
## Table of Contents
- [Natural Language Processing, Speech, and Computer Vision](#natural-language-processing-speech-and-computer-vision)
- [What is Natural Language Processing (NLP)](#what-is-natural-language-processing-nlp)
- [Self-Driving Cars](#self-driving-cars)
- [AI and Cloud Computing, Edge Computing, and IoT](#ai-and-cloud-computing-edge-computing-and-iot)
---
## Natural Language Processing, Speech, and Computer Vision
### **Natural Langauge Processing**
- **Definition**: A subset of AI enables mahcines to understand, interpret, and generate human language
- **Key Functions**
    - Analyzing semantic meaning by deconstructing sentences grammatically, relationally, and structurally
    - Understanding context, intent, and emotions (e.g., discerning "cloud" as computing vs. weather)
    - Drawing inferences using linguistic models and algorithms
- **Applications**
    - **Customer Support**: STT transcribes queries, NLP interprets them, and TTS delivers responses
    - **Accessibility**: STT transcribes speech, NLP processes it, and TSS converts it back to comprehensible speech
    - Translation services integrate STT and TTS for multilingual communication
### Speech Technology
- **Speech-to-Text (STT)**
    - Converts spoken words into written text using neural networks
    - **Applications**
        - Real-time transcription (e.g., YouTube closed captioning)
        - Virtual Assistants (e.g., Siri, Google Assistant)
        - Voice Search and dictation services
- **Text-to-Speech**
    - Converts written text into spoken words (speech synthesis)
    - **Process**:
        - One neural network learns the voice
        - Another network generates audio and iteratively improves until the generated voice sounds natural
    - **Applications**
        - Smart home devices: Understanding commands (STT) and providing feedback (TTS)
        - Translation services: Google Translate listens (STT) and speaks translations (TTS)
### Computer Vision
- **Definition**: A field of AI enabling machins to interpret and analze visual data like images and videos
- **Key Applications**
    - **Facial Recognition**
        - Unlocking phones by matching facial images
    - **Image Classification**
        - Categorizes images (e.g., medical image analysis, e-commerce product sorting)
    - **Object Detection**
        - Recognizes and locates objects in images
        - Example algorithms: YOLO, Faster R-CNN
        - Uses Cases: Surveillance, autonomous vehicles
    - **Image Segmentation**:
        - Divides images into segments and labels each pixel for detailed analysis
- **Industry Applications**
    - **Retail**: Inventory Management, personalized shopping (Amazon, Walmart, Alibaba)
    - **Manufacturing**: Quality control, automation (Toyota, Siemens, Bosch)
    - **Agriculture**: Precision farming, crop health monitoring (John Deere, Monsanto)
    - **Transportation**: Self-driving cars interpreting surroundings
### Takeaways
- **NLP** helps machines understand and produce human language, leveraging ML and DL to grasp semantic meaning and intent
- **Speech Technology** enables seamless human-machine communication
    - STT: Converts speech to text for transcription and command processing
    - TTS: Synthesizes natural-sounding speech from text
- **Computer Vision** bridges the digital and physical worlds by analyzing data, enabling tasks like object detection, image segmentation, and facial recognition across various industries
---
## What is Natural Language Processing (NLP)
### Definition
- **Natural Language Processing (NLP)**: A branch of AI that enables computers to understand, interpret, and process human language (spoken or written).
Key Concept
- NLP bridges the gap between unstructured text (human language) and structured data (computer-readable format).
### How NLP Works
- **Unstructured Text**
    - Example: "Add eggs and milk to my shopping list."
    - Humans understand the meaning easily, but to a computer, this text is unstructured.
- **Structured Representation**
    - NLP translates unstructured text into structured data.
    - Example: Representing "shopping list" as an object with items: eggs and milk.
- **Two Core Processes**
    - **Natural Language Understanding (NLU)**: Converts unstructured text into structured data.
    - **Natural Language Generation (NLG)**: Converts structured data back into natural language.
### Applications of NLP
- **Machine Translation**
    - Translating text while preserving context and meaning.
    - Example: Avoiding mistranslation, such as turning "the spirit is willing, but the flesh is weak" into "the vodka is good, but the meat is rotten."
-  **Virtual Assistants and Chatbots**
    - Processing spoken or written commands and taking actions.
    - Example: Siri, Alexa, and text-based chatbots.
- **Sentiment Analysis**
    - Analyzing text to determine emotions or sentiment (e.g., positive, negative, sarcastic).
    - Example: Product reviews, emails.
- **Spam Detection**
    - Identifying spam emails based on content features like grammar errors, urgency, and overused words.
### NLP Processing Stages
- **Input**: Spoken or written text (unstructured data).
- **Tokenization**
    - Breaking text into smaller chunks (tokens).
    - Example: "Add eggs and milk to my shopping list" → 8 tokens.
- **Stemming**
    - Reduces words to their root form by removing prefixes/suffixes.
    - Example: "running," "runs," and "ran" → "run."
    - Limitation: Doesn’t work well for irregular cases (e.g., "universal" and "university").
- **Lemmatization**
    - Uses dictionary definitions to find the root meaning of a word.
    - Example: "better" → "good" (root/lemm).
    - Contrast: The stem of "better" would be "bet," which is less meaningful.
- **Part-of-Speech (POS) Tagging**
    - Identifies the role of a token in a sentence.
    - Example: "make" as a verb ("make dinner") vs. a noun ("what make is your laptop").
- **Named Entity Recognition (NER)**
    - Identifies named entities associated with tokens.
    - Example: "Arizona" → US State; "Ralph" → Person’s name.
### NLP's Bag of Tools
- NLP is not a single algorithm but a collection of tools and techniques.
- These tools enable the transformation of unstructured data into structured formats, which are essential for AI applications.
### Takeaways
- NLP enables seamless translation between human language and structured data for AI applications.
- Key techniques include tokenization, stemming, lemmatization, POS tagging, and NER.
- Applications like machine translation, virtual assistants, sentiment analysis, and spam detection rely heavily on NLP.
---
## Self-Driving Cars
### Overview
- Self-driving cars are a rapidly growing domain, gaining interest since early competitions (e.g, 2005)
- Recent advancements include developing self-driving vehicles capable of operating on public roads (e.g., a vehicle in Waterloo in August)
### Key Challenges and Research Areas
1. **3D Object Detection**
    - Identifying every vehicle, pedestrian, and signs in the driving environment
    - Critical for ensuring accurate decision-making by the vehicle
2. **Sensor Fusion**
    - Combining data from **Laser Sensors (LiDAR), cameras, and RADAR** to create a comprehensive view of the world
    - Enhances the system's ability to understand and interact with its environment
### Role of Computer Vision in Self-Driving Cars
- **Attention**: Addresses the limitations of human vision (e.g., visual attention span)
    - Cameras and sensors provide **360&deg; awareness**, allowing the system to "see" and process multiple elements simultaneously
    - Example: Detecting a pedestrian on a skateboard or an unexpected vehicle
- **Predictive Capabilities**: Helps anticipate and prevent potential accidents
### Advantages of AI and Computer Vision in Transportation
- Enhances safety by reducing human error (e.g., distracted driving)
- Improves efficiency in navigating complex traffic scenarios
- Offers convenience (e.g., allowing passengers to read or take calls while commuting)
### Future of Self-Driving Cars
- Significant potential to transform societal operations and individual lifestyles
    - Example: Changing commuting habits and reducing traffic stress
- **Current Limitations**
    - Autonomous systems are not yet robust enough for 100% safe, fully automated operation
    - Ongoing research needed to address challenges in object detection, decision-making, and system reliability
### Takeaways
- Self-driving cars represent a transformative step forward in transportation, but require further advancements in AI and computer vision
- Key technologies, like sensor fusion and 3D object detection, are critical for creating reliable and safe autonomous vehicles
- The vision of self-driving cars promises safer roads, more efficient commutes, and a reimagined transportation landscape
---
## AI and Cloud Computing, Edge Computing, and IoT
### Internet of Things (IoT)
- **Definiton**: A network of physical devices connected to the internet that collect and share data for processing and analysis
- **Examples**
    - Fitness trackers and smartwatches: Monitor health and activity levels
    - Smart thermostats: Learn and adjust temperature preferences
    - Washing machines: Operated remotely via smartphone app
- **How It Works**
    - Devices collect data and sent it to the cloud for storage and analysis
### Cloud Computing
- **Definition**: The use of remote servers over the internet to store, process, and analyze data
- **Purpose**
    - Provides powerful computing resources from remote data centers
    - Eliminates the need for local storage or processing
- **Examples**
    - Gmail: Emails stored and accessible from the cloud
- **Role of AI in Cloud Computing**
    - Analyzes data, automates tasks, and makes decisions
    - Example: AI filters spam emails based on patterns and user behavior
### Edge Computing
- **Definition**: Process data closer to its source (the device) rather than relying on centralized data centers
- **Advantages**
    - Faster decision-making
    - Reduces latency by processing data locally
- **Examples**
    - Thermostats: Instantly sense temperature and adjust heating/cooling without cloud reliance
    - Edge AI: AI integrated into devices for local processing (e.g., security cameras with facial recognition)
### Integration of AI, IoT, Cloud Computing, and Edge Computing
- **Example: Fitness Tracker**
    1. **IoT**: collects data (heart rate, steps, activity level)
    2. **Edge Computing**
        - Processes data locally
        - Provides real-time feedback (e.g., alerts for high heart rate)
    3. **AI on the Edge**
        - Analyzes activity patterns (e.g., differentiates running from walking)
        - Offers instant coaching instructions
    4. **Cloud Computing**
        - Syncs data with a smart phone app via Bluetooth
        - Stores data for long-term analysis and viewing
    5. **Cloud-Based AI**
        - Offers advanced features (e.g., sleep analysis, personalized workout recommendations)
### Real-World Applications
- **AI-Powered Traffic Lights**: Optimize traffic flow in real-time
- **Smart Public Transportation**: Enhance route efficiency and scheduling
- **Smart Agriculture**: Monitor crop health and optimize resources
- **Smart Buildings**: Automate energy use, lighting, and climate control
### Takeaways
- **IoT** connects devices for data collection and sharing
- **Cloud Computing** provides scalable data storage and analysis over the internet
- **Edge Computing** enables faster, localized processing and decision-making
- The convergence of AI, IoT, cloud computing, and edge computing powers smart, real-time applications that improve efficiecny and quality of life
---