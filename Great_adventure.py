import random

def main():
    # Initialize themes
    themes = {
        "Adventure": {
            "Characters": ["A daring astronaut", "A fearless explorer", "A curious archaeologist"],
            "Settings": ["on a distant planet", "in a hidden jungle", "inside an ancient pyramid"],
            "Conflicts": ["encountered an alien civilization", "discovered a lost artifact", "faced a giant creature"],
            "Resolutions": ["became their ambassador", "uncovered the artifact's secrets", "defeated the creature"]
        },
        "Comedy": {
            "Characters": ["A clumsy detective", "A quirky magician", "A forgetful professor"],
            "Settings": ["at a fancy dinner party", "during a live TV show", "in a chaotic classroom"],
            "Conflicts": ["accidentally revealed the host's secret", "lost their magic wand", "tripped during a presentation"],
            "Resolutions": ["became the life of the party", "improvised with surprising success", "turned the mishap into a joke"]
        },
        "Mystery": {
            "Characters": ["A brilliant detective", "An amateur sleuth", "A reclusive writer"],
            "Settings": ["in a haunted mansion", "at a quiet seaside town", "during a high-profile gala"],
            "Conflicts": ["unraveled a series of strange clues", "encountered an unexpected suspect", "found themselves under suspicion"],
            "Resolutions": ["solved the case dramatically", "exposed the real culprit", "cleared their name"]
        }
    }

    print("Welcome to the Random Story Generator!")
    name = input("What is your name? ").strip()

    while True:
        # Ask user for their theme choice
        print("\nChoose a theme: Adventure, Comedy, Mystery, or Random")
        user_choice = input("Enter your choice: ").strip().capitalize()

        # Select theme
        if user_choice in themes:
            chosen_theme = themes[user_choice]
        elif user_choice == "Random":
            chosen_theme = random.choice(list(themes.values()))
        else:
            print("Invalid choice. Please choose Adventure, Comedy, Mystery, or Random.")
            continue

        # Generate random story elements
        character = random.choice(chosen_theme["Characters"])
        setting = random.choice(chosen_theme["Settings"])
        conflict = random.choice(chosen_theme["Conflicts"])
        resolution = random.choice(chosen_theme["Resolutions"])

        # Assemble and display the story
        story = (f"Once upon a time, {character} was {setting}. "
                 f"They {conflict}, and finally, {resolution}.")
        print(f"\nHere is your story, {name}:\n")
        print(story)

        # Ask for replay
        replay = input("\nWould you like to generate another story? (yes/no): ").strip().lower()
        if replay != "yes":
            print("\nThank you for using the Random Story Generator. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
    



