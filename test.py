import pandas as pd
from langchain_google_genai import GoogleGenerativeAI
from plotly import express as px
from plotly import graph_objects as go
from plotly.graph_objects import Figure
from langchain_core.prompts import PromptTemplate
import os
import mysql.connector
from dotenv import load_dotenv
from plotly.subplots import make_subplots

load_dotenv()

api_key = os.getenv("API_KEY")
sqllm = GoogleGenerativeAI(
    model="models/gemini-pro", google_api_key=api_key, temperature=0.1
)


def get_chart(query, data, llm):
    # data = prep_data(data)
    # # print(data)
    # index = [i for i in range(0, len(data[0]))]
    # df = pd.DataFrame(data=data[0], columns=data[1], index=index)
    # environment: dict = {"pd": pd, "go": go, "px": px, "df": df, "fig": None}
    # # print(df)

    directory = 'temp'
    if not os.path.exists(directory):
        os.mkdir(directory)
    # chart_path = f'{directory}/chart.html'
    # f = open(chart_path, "w")

    df = pd.DataFrame({
        'productName': ['Product QDOMO', 'Product VJXYN', 'Product AOZBW', 'Product QHFFP', 'Product CKEDC',
                        'Product UKXRI', 'Product APITJ', 'Product WUXYK', 'Product ZZZHR', 'Product OFBNT'],
        'unitPrice': [263.50, 123.79, 97.00, 81.00, 62.50, 55.00, 53.00, 49.30, 46.00, 45.60]
    })

    query = 'Give me all the products with unit price more than 30.'
    environment: dict = {"pd": pd, "go": go, "px": px, "df": df, "fig": None, "make_subplots": make_subplots}

    prompt_template = PromptTemplate.from_template("""You are a proficient Python developer with expertise in the 
    Plotly library. Your objective is to generate Python code to create a BEAUTIFUL chart based on the query using the 
    provided Pandas dataframe. You can create any chart you want.

    ### QUERY: 
    {query}

    ### DATAFRAME:
    {df}

    ### INSTRUCTIONS: 1. Create a function called 'get_chart'. 2. Begin by importing the necessary libraries (Pandas, 
    Plotly, and Decimal if needed). 3. Utilize the 'plotly.graph_objects' library if the provided dataframe has more 
    than 2 columns to showcase multi bar plots. Otherwise, utilize the 'plotly.express' library.  4. Generate a chart 
    using the provided dataframe and the Plotly library. 5. Accurately interpret the x-axis title, y-axis title, 
    and chart title as per the user's query and the dataframe. 6. Utilize the 'update_layout' method to include the 
    x-axis title, y-axis title, chart title, plot background color, and paper background color, setting both of them 
    to blue (HEX code: #0e243b). 7. Set the font color to white (HEX code: #f7f9fa) using the 'update_layout' method. 
    8. Execute the created function with the argument as the provided dataframe, at the outer indent at the end and 
    store the result in a variable called 'chart'. 9. Ensure that only the above mentioned libraries and methods are 
    utilized.

    ### CODE CRITERIA
    - Optimize the code for efficiency and clarity.
    - Avoid using incorrect syntax.
    - Ensure that the code is well-commented for readability and syntactically correct.
    """)

    prompt = prompt_template.format(query=query, df=df)
    result = llm.invoke(prompt).replace("```", "").replace("python", "")

    print(result)
    exec(result, globals(), environment)
    fig = environment.get("fig", None)
    chart = environment.get("chart", None)
    return chart


df = pd.DataFrame({
    'productName': ['Product QDOMO', 'Product VJXYN', 'Product AOZBW', 'Product QHFFP', 'Product CKEDC',
                    'Product UKXRI', 'Product APITJ', 'Product WUXYK', 'Product ZZZHR', 'Product OFBNT'],
    'unitPrice': [263.50, 123.79, 97.00, 81.00, 62.50, 55.00, 53.00, 49.30, 46.00, 45.60]
})

q = 'Give me all the products with unit price more than 30.'
figure = get_chart(q, df, sqllm)
print(figure)