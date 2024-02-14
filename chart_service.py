from langchain_core.prompts import PromptTemplate
import os

list_of_charts = ['Line Chart', 'Bar Chart', 'Histogram', 'Scatter Plot', 'Bubble Plot', 'Pie Chart']


def get_chart(list_of_charts, query, data, llm):
    directory = 'temp'
    if not os.path.exists(directory):
        os.mkdir(directory)

    prompt_template = PromptTemplate.from_template("""
    You are a proficient Python developer with expertise in the Plotly library. Your objective is to generate Python code to create a chart from the {list_of_charts} which best represents the data based on the query using the provided data. 

    ### QUERY: 
    {query}

    ### DATA:
    {data}

    ### INSTRUCTIONS:
    1. Create a function called 'get_chart'.
    2. Begin by importing the necessary libraries (Pandas, Plotly, and Decimal if needed).
    3. Create a Pandas dataframe, ensuring it includes ONLY the relevant columns needed for the specified chart. Assign the values according to the data, ensuring that the dataframe is structured to facilitate easy visualization and that all relevant data is represented.
    4. Create three variables 'x_column', 'y_column' and 'color_column' to store the value of 'x', 'y' and 'color' parameter respectively. Ensure that the values of 'y_column' are numeric, such as counts.
    5. Call the chart type method call inside a conditional logic which is used to determine whether to use the 'color_continuous_scale' parameter if the values of the 'color_column' are numeric, or the 'color_discrete_sequence' parameter if the values of the 'color_column' are not numeric. Specify the color of the plot as different gradients of red using ONLY the 'px.colors.sequential.Reds' colour scheme in the entire conditional logic. 
    6. Accurately interpret the x-axis title, y-axis title, and chart title as per the user's query and the dataset.
    7. Utilize the 'update_layout' method to include the x-axis title, y-axis title, chart title, plot background color, and paper background color, setting them to blue (HEX code: #0e243b).
    8. Ensure the font color is set to white (HEX code: #f7f9fa) using the 'update_layout' method.
    9. Save the plot as 'chart.html' in 'temp' folder in html format. Also, execute the function at the main indent at the end.
    10. Consider adding comments to the code for improved clarity and maintainability.
    11. Ensure that the code is syntactically correct.

    ### CODE CRITERIA
    - Optimize the code for efficiency and clarity.
    - Avoid using incorrect syntax.
    - Ensure that the code is well-commented for readability and syntactically correct.
    """)

    prompt = prompt_template.format(query=query, data=data, list_of_charts=list_of_charts)
    result = llm.invoke(prompt).replace("```", "").replace("python", "")

    exec(result)