from webbrowser import get
from core.factory import create_app
from modules.scraper import get_all_items
from core import celery_ext
app = create_app(celery=celery_ext)

if __name__ == "__main__":
    app.run()
    # get_all_items(url="https://sport.detik.com/indeks")