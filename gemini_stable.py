from google import genai
from google.genai import types
import PIL.Image
import time
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def gemini(image_path):

    prompt ="Extract the complete water meter reading from the given image. The reading is displayed inside a rectangular box  and consists of a sequence of digits."
    system_instructions = "Return only the digits as a continuous string, ignoring any spaces, decimal points, or other symbols. Do not include any additional text from the image."
    model_name = "gemini-2.0-flash"

    image = PIL.Image.open(image_path)
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=[prompt, image],
            config = types.GenerateContentConfig(
                system_instruction=system_instructions,
                temperature=0.1,
            )
        )
        return response.text
    except Exception as e:
        return e
    

# system_instructions = """
#     Return the specific digits on the counter as a continuous string, ignoring any spaces, decimal points, or other symbols.  
#     Exclude the last digit from the extracted reading.Do not include any additional text from the image.  
#     """

# prompt = """
# Extract the complete water meter reading from the given image, excluding the last digit.  
# The reading is displayed inside a rectangular box consisting of a sequence of digits.
# """


# system_instructions = """
#     Return the specific digits on the counter as continious string , ignoring any spaces, decimal points, or other symbols. 
#     Do not include any additional text from the image.
#     """

# prompt = """
# Extract the complete water meter reading from the given image. 
# The reading is displayed inside a rectangular box consists of a sequence of digits.
# """


# image = PIL.Image.open('images/water04.jpeg')
# response_list = []
# # for i in range(100):
# response = client.models.generate_content(
#     model=model_name,
#     contents=[prompt, image],
#     config = types.GenerateContentConfig(
#         system_instruction=system_instructions,
#         temperature=0.1,
#     )
# )

# print(response.text)

# for i in range(100):
#     print(gemini("/home/skywalker/#/project03/images/water01.jpeg"))
#     print(gemini("/home/skywalker/#/project03/images/water02.jpeg"))
#     print(gemini("/home/skywalker/#/project03/images/water03.jpeg"))
#     print(gemini("/home/skywalker/#/project03/images/water04.jpeg"))
#     print(gemini("/home/skywalker/#/project03/images/water05.jpeg"))
#     print(i)

    
