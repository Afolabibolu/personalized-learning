from pathlib import Path

ML_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = ML_DIR / "models"
RESULTS_DIR = ML_DIR / "results"

# The cold-start threshold (completed quizzes on a course before the models rank
# its topics) is one value in the database, app_settings.cold_start_threshold,
# shared with the web app and the SQL functions; /recommend reads it each run.

# Label rule: a topic "requires attention" when the next attempt scores below this.
ATTENTION_THRESHOLD = 50.0

MODEL_VERSION = "v1"
LR_MODEL_PATH = MODELS_DIR / f"lr_{MODEL_VERSION}.joblib"
RF_MODEL_PATH = MODELS_DIR / f"rf_{MODEL_VERSION}.joblib"

# At or above this averaged probability a topic shows as "Needs attention";
# below it, as "Keep it up".
ATTENTION_PROBABILITY = 0.5

# How many topics get ML recommendations, across all of a student's courses.
TOP_TOPICS = 3
