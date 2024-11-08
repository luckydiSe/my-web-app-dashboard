# my-web-app-dashboard

## Project Description
This project is a web application built with Streamlit that analyzes car advertisement data to provide insights on car prices, listing duration, and other attributes. It allows users to interact with the data through adjustable visualizations and explore relationships between various car attributes.

## Key Features
- Displays a histogram of car prices.
- Shows a scatter plot for car price vs. days listed with an adjustable price range.
- Includes a checkbox to toggle between a limited and full price range for the scatter plot.

## Libraries and Methods Used
- **Streamlit**: Used to create the web application dashboard and interactive components.
- **Pandas**: Utilized for data manipulation and loading the dataset.
- **Plotly Express**: Employed to create interactive visualizations (histogram and scatter plot).

## Instructions to Run Locally
To run this project on your local machine, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
    ```bash
    git clone https://github.com/your-username/my-web-app-dashboard.git
    ```

2. **Navigate to the Project Directory**: Move into the project folder.
    ```bash
    cd my-web-app-dashboard
    ```

3. **Install Dependencies**: Make sure you have Python installed, then install the required packages. You can create a virtual environment (recommended) and install dependencies using:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

4. **Run the Application**: Start the Streamlit application using the command:
    ```bash
    streamlit run app.py
    ```

5. **View the Application**: After running the command above, a URL will appear in the terminal. Open it in your browser to view and interact with the dashboard.

## Dependencies
Make sure to install dependencies by running:
```bash
pip install -r requirements.txt

## Deployment Note

This app is deployed on Render. To ensure compatibility with Render's environment, the Start Command was modified to:

```bash
streamlit run app.py --server.port $PORT
