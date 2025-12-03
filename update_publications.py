"""
Script to fetch publications from Google Scholar and generate JSON data.
Usage: python update_publications.py
"""

import json
import os
from datetime import datetime
from scholarly import scholarly

# Configuration
SCHOLAR_ID = "7tsIRXYAAAAJ"
OUTPUT_DIR = "files"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "publications.json")

def get_category(venue):
    """Determine publication category based on venue."""
    venue_lower = venue.lower() if venue else ""

    if any(word in venue_lower for word in ['conference', 'proceedings', 'symposium', 'workshop']):
        return 'Conference'
    elif any(word in venue_lower for word in ['journal', 'transactions', 'letters']):
        return 'Journal'
    elif any(word in venue_lower for word in ['book', 'chapter']):
        return 'Book'
    elif any(word in venue_lower for word in ['arxiv', 'preprint']):
        return 'Preprint'
    else:
        return 'Other'

def format_authors(authors):
    """Format author list."""
    if not authors:
        return ""
    # If authors is a string, return it directly
    if isinstance(authors, str):
        return authors
    # If it's a list
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    else:
        return f"{', '.join(authors[:-1])}, and {authors[-1]}"

def main():
    """Main function to fetch and process publications."""
    print(f"Fetching publications for Google Scholar ID: {SCHOLAR_ID}")
    print("This may take a few minutes...\n")

    try:
        # Create output directory if it doesn't exist
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Fetch author profile
        search_query = scholarly.search_author_id(SCHOLAR_ID)
        author = scholarly.fill(search_query)

        print(f"Found author: {author.get('name', 'Unknown')}")
        print(f"Total publications: {len(author.get('publications', []))}\n")

        # Process each publication
        publications_data = []
        publications = author.get('publications', [])

        for i, pub in enumerate(publications, 1):
            print(f"Processing {i}/{len(publications)}: ", end='')

            try:
                # Fill in complete publication details
                filled_pub = scholarly.fill(pub)
                bib = filled_pub.get('bib', {})

                title = bib.get('title', f'Publication {i}')
                print(title[:50] if len(title) <= 50 else title[:50] + '...')

                # Extract publication details
                pub_data = {
                    'title': title,
                    'authors': format_authors(bib.get('author', [])),
                    'year': str(bib.get('pub_year', datetime.now().year)),
                    'venue': bib.get('venue', 'Unknown Venue'),
                    'abstract': bib.get('abstract', ''),
                    'citations': filled_pub.get('num_citations', 0),
                    'url': filled_pub.get('pub_url') or filled_pub.get('eprint_url') or '',
                    'category': get_category(bib.get('venue', ''))
                }

                publications_data.append(pub_data)

            except Exception as e:
                print(f"Error: {str(e)}")
                continue

        # Sort by year (descending)
        publications_data.sort(key=lambda x: x['year'], reverse=True)

        # Save to JSON
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(publications_data, f, indent=2, ensure_ascii=False)

        print(f"\n{'='*50}")
        print(f"Successfully saved {len(publications_data)} publications to {OUTPUT_FILE}")
        print(f"{'='*50}")

    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nMake sure you have installed the required package:")
        print("  pip install scholarly")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
