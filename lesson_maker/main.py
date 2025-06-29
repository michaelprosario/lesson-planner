import google.generativeai as genai
import os
from typing import List, Dict, Union, Literal
from dotenv import load_dotenv

load_dotenv()

# --- 1. Define your JSON Schema using Python typing ---

class Lesson:
    name: str
    description: str
    topics: List[str]

    def __init__(self, name: str, description: str, topics: List[str]):
        self.name = name
        self.description = description
        self.topics = topics

class CoursePlan:
    title: str
    target_audience: str
    overall_goal: str
    lessons: List[Lesson]

    @classmethod
    def from_json(cls, json_data: Dict) -> 'CoursePlan':
        """
        Create a CoursePlan instance from a JSON dictionary.
        """
        instance = cls()
        instance.title = json_data.get("title", "")
        instance.target_audience = json_data.get("target_audience", "")
        instance.overall_goal = json_data.get("overall_goal", "")
        instance.lessons = [
            Lesson(name=lesson["name"], description=lesson["description"], topics=lesson["topics"])
            for lesson in json_data.get("lessons", [])
        ]
        return instance

# --- 2. Configure the Gemini API ---
# Replace 'YOUR_API_KEY' with your actual Gemini API key,
# or set it as an environment variable (recommended)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose a suitable Gemini model. Gemini 1.5 Pro and Flash are excellent for structured output.
# 'gemini-1.5-pro-latest' or 'gemini-1.5-flash-latest'
MODEL_NAME = "gemini-1.5-pro-latest" # Or 'gemini-1.5-flash-latest' for lower latency

def make_lesson_content(lessonSpec: str) -> str:
    """
    Generates content for a lesson based on the provided lesson specification.
    """
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config={
            "temperature": 0.1,  # Low temperature for more deterministic output
            "response_mime_type": "text/plain"
        }
    )

    prompt = "Write a lesson. Define critical concepts. Provide samples of concepts. Draft exercises that explore the concepts. Return content as markdown. Write lesson about this topic: "
    response = model.generate_content(f'{prompt} {lessonSpec}')

    if response.text:
        #print("Received content from Gemini.")
        return response.text.strip()
    else:
        print("No content received from Gemini.")
        return ""

def get_lessons_plan_json(user_prompt: str) -> Dict:
    """
    Generates a Python learning plan in a consistent JSON format using Gemini.
    """
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config={
            "temperature": 0.1,  # Low temperature for more deterministic output
            "response_mime_type": "application/json",
            "response_schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Overall title of the learning plan."},
                    "target_audience": {"type": "string", "description": "The intended audience for this plan."},
                    "overall_goal": {"type": "string", "description": "The main objective of the learning plan."},
                    "lessons": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string", "description": "Name of the lesson."},
                                "description": {"type": "string", "description": "Brief description of the lesson content."},
                                "topics": {
                                    "type": "array",
                                    "items": {"type": "string", "description": "Key topics covered in the lesson."}
                                }
                            },
                            "required": ["name", "description", "topics"]
                        }
                    }
                },
                "required": ["title", "target_audience", "overall_goal", "lessons"]
            }
        }
    )

    # Your original prompt
    full_prompt = (
        user_prompt + " "
        "The plan should span multiple lessons, guiding them from basic concepts to more advanced topics. "
        "Each lesson should have a name, description, and a list of specific topics covered. "
        "Ensure the output is a JSON object strictly following the provided schema."
    )

    # print("Sending prompt to Gemini...")
    response = model.generate_content(full_prompt)

    try:
        # Gemini automatically parses the JSON when response_mime_type is set
        # and the output is valid JSON. The result.text will be the JSON string.
        import json
        json_output = json.loads(response.text)
        # print("Received valid JSON output.")
        return json_output
    except json.JSONDecodeError:
        # print("Error: Gemini did not return valid JSON. Raw response:")
        print(response.text)
        return {"error": "Invalid JSON from model", "raw_response": response.text}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": str(e), "raw_response": response.text}

# --- Execute the prompt ---
if __name__ == "__main__":
    plan = get_lessons_plan_json(
        "as an instructional designer, draft a plan for teaching a novice about cell biology. The plan should span multiple lessons."
    )

    if "error" not in plan:

        coursePlan = CoursePlan.from_json(plan)

        lessons = coursePlan.lessons
        for lesson in lessons:
            lesson.name = lesson.name.strip()
            lesson.description = lesson.description.strip()
            lesson.topics = [topic.strip() for topic in lesson.topics]

            # create on string with all the data about lesson
            lessonString = f"{lesson.name} - {lesson.description} - Topics: {', '.join(lesson.topics)}"

            lessonMarkdown = make_lesson_content(lessonString)
            print(lessonMarkdown)

    else:
        print(plan)
