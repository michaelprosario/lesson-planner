# Lesson Planner

An AI-powered lesson planning tool that generates comprehensive educational content using Google's Gemini API. This tool creates structured course plans with detailed lessons, topics, and educational materials in markdown format.

## 🎯 Major Concepts

### 1. **AI-Driven Course Planning**
The system uses Google's Gemini API to generate structured learning plans based on user-defined topics. It creates a comprehensive course outline with multiple lessons, each containing specific learning objectives and topics.

### 2. **Structured Data Generation**
The application leverages Gemini's structured output capabilities to generate consistent JSON schemas that define:
- Course titles and target audiences
- Learning objectives and goals
- Individual lesson plans with topics
- Educational content in markdown format

### 3. **Two-Phase Content Creation**
1. **Planning Phase**: Generates a structured course outline with lesson specifications
2. **Content Phase**: Creates detailed educational content for each lesson including concepts, examples, and exercises

## 🏗️ How It Works

### Architecture Overview

The `main.py` file contains the core functionality organized into several key components:

#### 1. **Data Models**
```python
class Lesson:
    name: str
    description: str
    topics: List[str]

class CoursePlan:
    title: str
    target_audience: str
    overall_goal: str
    lessons: List[Lesson]
```

#### 2. **Course Plan Generation (`get_lessons_plan_json`)**
- Accepts a user prompt describing the desired course topic
- Uses Gemini's structured output with JSON schema validation
- Returns a complete course plan with multiple lessons
- Includes error handling for invalid JSON responses

#### 3. **Lesson Content Creation (`make_lesson_content`)**
- Takes individual lesson specifications
- Generates detailed educational content in markdown format
- Creates comprehensive lessons with:
  - Critical concept definitions
  - Practical examples
  - Interactive exercises

#### 4. **Execution Flow**
1. Define the key topic for course creation
2. Generate structured course plan using Gemini API
3. Extract individual lesson specifications
4. Create detailed content for each lesson
5. Output formatted markdown content

### Sample Workflow

```python
# 1. Define topic
keyTopic = "Encouraging usability by design"

# 2. Generate course plan
plan = get_lessons_plan_json(f"draft a plan for teaching {keyTopic}")

# 3. Create detailed lessons
coursePlan = CoursePlan.from_json(plan)
for lesson in coursePlan.lessons:
    lessonMarkdown = make_lesson_content(lesson_specifications)
    print(lessonMarkdown)
```

## 🚀 Setup and Configuration

### Prerequisites
- Python 3.7 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd lesson-planner
   ```

2. **Install dependencies**
   ```bash
   pip install -r lesson_maker/requirements.txt
   ```

3. **Configure API Key**
   
   **⚠️ IMPORTANT: You must configure your Gemini API key before running the application.**
   
   Create a `.env` file in the `lesson_maker/` directory:
   ```bash
   cd lesson_maker
   touch .env
   ```
   
   Add your Gemini API key to the `.env` file:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   
   **How to get a Gemini API key:**
   1. Go to [Google AI Studio](https://aistudio.google.com/)
   2. Sign in with your Google account
   3. Create a new API key
   4. Copy the API key to your `.env` file

### Running the Application

```bash
cd lesson_maker
python main.py
```

The application will:
1. Generate a course plan for the default topic
2. Create detailed lesson content
3. Output formatted markdown lessons to the console

### Customizing Topics

To create lessons for different topics, modify the `keyTopic` variable in `main.py`:

```python
keyTopic = "Your desired learning topic here"
```

## 📁 Project Structure

```
lesson-planner/
├── README.md                    # This file
├── LICENSE                      # Project license
├── lesson_maker/               # Main application directory
│   ├── main.py                 # Core lesson planning logic
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # API key configuration (create this)
│   └── *.md                    # Sample generated lessons
```

## 🔧 Configuration Options

### Model Selection
The application uses `gemini-1.5-pro-latest` by default. You can modify the model in `main.py`:

```python
MODEL_NAME = "gemini-1.5-flash-latest"  # For faster responses
```

### Generation Parameters
Adjust the generation settings for different output styles:

```python
generation_config={
    "temperature": 0.1,  # Lower = more consistent, Higher = more creative
    "response_mime_type": "application/json"  # or "text/plain"
}
```

## 📋 Output Format

The system generates:
- **Structured course plans** in JSON format
- **Detailed lesson content** in markdown format
- **Comprehensive educational materials** including concepts, examples, and exercises

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with your own API key
5. Submit a pull request

## 📄 License

See the LICENSE file for details.

---

**Note**: This tool requires a valid Google Gemini API key to function. Make sure to configure your `.env` file before running the application.