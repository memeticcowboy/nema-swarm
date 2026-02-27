import random
import datetime

archetypes = [
    ("Urban Planner", "city infrastructure", "sustainable development", "traffic congestion"),
    ("Marine Biologist", "ocean ecosystems", "coral restoration", "plastic pollution"),
    ("Game Developer", "procedural generation", "AI NPCs", "player retention"),
    ("Rural Doctor", "telemedicine", "vaccine distribution", "chronic disease"),
    ("Climate Scientist", "carbon capture", "renewable energy", "extreme weather"),
    ("Journalist", "investigative reporting", "misinformation", "press freedom"),
    ("Teacher", "remote learning", "student engagement", "curriculum design"),
    ("Chef", "farm-to-table", "food waste", "flavor chemistry"),
    ("Architect", "biophilic design", "affordable housing", "adaptive reuse"),
    ("Ethical Hacker", "penetration testing", "zero-day exploits", "social engineering"),
    ("Social Worker", "community outreach", "mental health crisis", "resource allocation"),
    ("Astronomer", "exoplanet discovery", "dark matter", "telescope arrays"),
    ("Librarian", "digital archives", "information literacy", "community spaces"),
    ("Wildlife Photographer", "conservation", "animal behavior", "habitat loss"),
    ("Folklorist", "oral traditions", "cultural preservation", "myth interpretation")
]

daemons = ["arboriel", "ferrosid", "jvalion", "humavita", "aerunik", "sentaria", "nema"]
themes = ["growth", "structure", "chaos", "community", "wisdom", "conflict", "harmony", "entropy", "resilience", "transformation"]

archetype, expertise, interest, challenge = random.choice(archetypes)
daemon = random.choice(daemons)
theme = random.choice(themes)

# Generate topic based on archetype expertise
if "Urban Planner" in archetype:
    topic = random.choice(["vertical farming", "15-minute cities", "green corridors"])
elif "Marine Biologist" in archetype:
    topic = random.choice(["kelp forests", "deep sea mining", "marine protected areas"])
elif "Game Developer" in archetype:
    topic = random.choice(["emergent narratives", "accessibility design", "cloud gaming"])
elif "Rural Doctor" in archetype:
    topic = random.choice(["community health workers", "mobile clinics", "preventive care"])
elif "Climate Scientist" in archetype:
    topic = random.choice(["permafrost thaw", "ocean acidification", "climate migration"])
elif "Journalist" in archetype:
    topic = random.choice(["data journalism", "underground reporting", "AI-generated news"])
elif "Teacher" in archetype:
    topic = random.choice(["gamified learning", "multilingual education", "trauma-informed teaching"])
elif "Chef" in archetype:
    topic = random.choice(["fermentation", "insect protein", "indigenous ingredients"])
elif "Architect" in archetype:
    topic = random.choice(["passive house design", "modular construction", "urban heat islands"])
elif "Ethical Hacker" in archetype:
    topic = random.choice(["IoT security", "supply chain attacks", "cryptographic protocols"])
elif "Social Worker" in archetype:
    topic = random.choice(["housing first", "restorative justice", "peer support networks"])
elif "Astronomer" in archetype:
    topic = random.choice(["gravitational waves", "space debris", "SETI protocols"])
elif "Librarian" in archetype:
    topic = random.choice(["open access", "community archives", "algorithmic bias"])
elif "Wildlife Photographer" in archetype:
    topic = random.choice(["camera traps", "ethical wildlife tourism", "visual storytelling"])
else:  # Folklorist
    topic = random.choice(["digital folklore", "urban legends", "intangible heritage"])

print(f"ARCHETYPE: {archetype}")
print(f"EXPERTISE: {expertise}")
print(f"INTEREST: {interest}")
print(f"CHALLENGE: {challenge}")
print(f"DAEMON: {daemon}")
print(f"THEME: {theme}")
print(f"TOPIC: {topic}")
