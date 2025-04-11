from cinemagoerng import web

def print_advisory(advisory, name):
    print(f"\n{name}:")
    print("Status:", advisory.status)
    print("Details:")
    for detail in advisory.details:
        spoiler = "[SPOILER]" if detail.is_spoiler else ""
        print(f"- {detail.text} {spoiler}")

# Get movie with parental guide information
movie = web.get_title("tt0114709", page="parental_guide")  # Toy Story

# Print certification information
print("MPAA Rating:", movie.certification.mpa_rating)
print("Rating Reason:", movie.certification.mpa_rating_reason)

# Print advisory information
print_advisory(movie.advisories.nudity, "Nudity")
print_advisory(movie.advisories.violence, "Violence")
print_advisory(movie.advisories.profanity, "Profanity")
print_advisory(movie.advisories.alcohol, "Alcohol")
print_advisory(movie.advisories.frightening, "Frightening") 