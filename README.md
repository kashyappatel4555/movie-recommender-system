# 🎬 Movie Recommender System 🍿

- This project leverages movie metadata to recommend similar movies based on content and additional features like popularity and ratings. The application is built using Python and Streamlit, providing an interactive interface for users to get movie recommendations and view posters.

## ✨ Key Features

- **Content-Based Recommendations**: Recommends movies based on genres, keywords, cast, and crew.
- **Enhanced Similarity Scoring**: Incorporates textual similarity with popularity, vote count, and vote average.
- **Interactive UI**: Streamlit-based interface for selecting movies and viewing recommendations.
- **Movie Posters**: Displays posters fetched from The Movie Database (TMDb) API.

## 🌍 Deployed Application

- The app is live and can be accessed here: [Movie Recommender System](https://movie-recommender-system-45.streamlit.app/)

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- `pip` for installing Python packages

### ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kashyappatel4555/movie-recommender-system.git
   cd movie-recommender-system

2. **Install Required Packages:**

    Create a virtual environment and install dependencies using `requirements.txt`:
    ```bash
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt

### 🛠️ Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py

2. **Access the app:**
Open a web browser and navigate to [http://localhost:8501](http://localhost:8501) to interact with the movie recommender system.

### 💡 How It Works

1. **Data Processing**: Merges and cleans the TMDb 5000 dataset, extracting relevant features such as genres, keywords, cast, and crew.
   
2. **Feature Extraction**: Uses `TfidfVectorizer` for text-based features and normalizes numerical features.

3. **Similarity Calculation**: Combines textual similarity with popularity, vote count, and vote average to recommend similar movies.

4. **Poster Fetching**: Retrieves movie posters from the TMDb API.

### 🎬 Example Usage

1.  **Select a movie** from the dropdown menu.
    
2.  **Click "Recommend"** to see a list of recommended movies and their posters.

### 🤝 Contributing

- If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Make sure your code adheres to the project's coding standards and includes appropriate tests.
