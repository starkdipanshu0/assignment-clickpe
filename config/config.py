import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL') or f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    #SQLALCHEMY_DATABASE_URI ="postgresql://neondb_owner:npg_0UopZGhaj1NH@ep-misty-shape-a434l5f4-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
   