from openai import OpenAI
import json

client = OpenAI()


def analyze_resume(resume_text, user_goal):

    prompt = f"""
Analyze the following resume according to the user's career goal.

USER GOAL:
{user_goal}

RESUME:
{resume_text}

STRICT RULES:
- Identify only highly relevant skills for the user's goal.
- Remove irrelevant information.
- Identify the most important skills and experiences that align with the user's goal.
- Identify important skills that are missing for the user's goal.
- Create a practical learning roadmap.
- Generate relevant interview questions based on the resume and target role.
- Keep the response concise and easy to read.
- Return ONLY valid JSON.
- Do not add markdown or explanations outside JSON.

Return JSON in exactly this format:

{{
    "skills": [],
    "missing_skills": [],
    "roadmap": [],
    "interview_questions": []
}}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.7,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI career assistant specialized in resume analysis and interview preparation."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000
        )

        result = response.choices[0].message.content.strip()

        # Remove markdown code fences if returned by the model
        if result.startswith("```"):
            result = result.replace("```json", "").replace("```", "").strip()

        return json.loads(result)

    except json.JSONDecodeError:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": "AI returned an invalid JSON response."
        }

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }