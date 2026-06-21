IPL Winning Team Prediction

This project predicts the winning team of an IPL match using historical IPL datasets and machine learning techniques. The model is trained on past match records and provides predictions through an interactive Streamlit web application.

Features

- Predicts the winning probability of IPL teams.
- Uses historical IPL match and ball-by-ball datasets.
- Machine learning model built with Scikit-Learn.
- Interactive web interface using Streamlit.
- Encoders and trained model stored for reuse.

Project Structure

├── app.py
├── train_model.py
├── model.pkl
├── encoders.pkl
├── data/
│   ├── matches.csv
│   ├── deliveries.csv
│   ├── teams.csv
│   ├── players.xlsx
│   ├── teamwise_home_and_away.csv
│   └── most_runs_average_strikerate.csv
├── requirements.txt
└── README.md

Dataset

The project uses IPL historical datasets including:

- Match information ("matches.csv")
- Ball-by-ball data ("deliveries.csv")
- Team information ("teams.csv")
- Player information ("players.xlsx")
- Team home and away records
- Batting statistics

Installation

Clone the repository:

git clone https://github.com/yourusername/ipl-winning-team-prediction.git
cd ipl-winning-team-prediction

Create a virtual environment:

python -m venv venv

Activate the environment:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Train the Model

python train_model.py

This generates:

- "model.pkl"
- "encoders.pkl"

Run the Application

streamlit run app.py

Open the browser and navigate to:

http://localhost:8501

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Pickle

Future Improvements

- Add player performance metrics.
- Improve model accuracy with advanced algorithms.
- Deploy the application on Streamlit Cloud or Heroku.

Author

Krish Parate