# Movie Guide Examples
#
# This script contains examples of movie guides for different genres and age groups.

from cinemagoerng.web import get_title

def print_movie_guide(movie_id):
    title = get_title(movie_id, page="parental_guide")
    if title is None:
        print(f"Movie not found: {movie_id}")
        return
        
    print(f"Movie: {title.title} ({movie_id})")
    if title.certification:
        print(f"Rating: {title.certification.mpa_rating}")
    if title.advisories:
        print("Advisory:")
        for category, advisory in title.advisories.__dict__.items():
            if advisory.details:
                print(f"- {category}:")
                for detail in advisory.details:
                    print(f"  - {detail.text}")
    print("---")

# Example movies
movie_ids = [
    "tt0114709",  # Toy Story
    "tt0133093",  # The Matrix
    "tt0070047",  # The Exorcist
    "tt0111161",  # The Shawshank Redemption
    "tt1375666"   # Inception
]

for movie_id in movie_ids:
    print_movie_guide(movie_id) 