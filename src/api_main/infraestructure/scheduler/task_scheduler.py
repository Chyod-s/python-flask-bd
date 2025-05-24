from apscheduler.schedulers.background import BackgroundScheduler
from src.api_main.infraestructure.database.engine import get_db

def job_wrapper():
    db = next(get_db())
    print("Running scheduled job...")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_wrapper, 'cron', hour=8, minute=30)
    scheduler.start()
    return scheduler

