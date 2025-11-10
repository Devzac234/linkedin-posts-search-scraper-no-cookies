thonimport os
import sys
import json
from extractors.linkedin_parser import LinkedInParser
from outputs.exporters import Exporter
from config.settings import SETTINGS

def run_scraper():
    query = sys.argv[1] if len(sys.argv) > 1 else None
    if not query:
        print("Please provide a search keyword or phrase.")
        sys.exit(1)

    parser = LinkedInParser(query)
    posts = parser.scrape_posts()

    if posts:
        exporter = Exporter()
        exporter.export_to_json(posts)
        print(f"Successfully scraped {len(posts)} posts.")
    else:
        print("No posts found.")
        
if __name__ == "__main__":
    run_scraper()