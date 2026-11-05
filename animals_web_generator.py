import requests
import os


def load_animals(animal_name):
    """Load animal data from the API."""

    API_KEY = os.getenv("API_NINJAS_KEY")
    URL = "https://api.api-ninjas.com/v1/animals"

    if not API_KEY:
        raise RuntimeError("API key is missing.")

    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "name": animal_name
    }

    response = requests.get(
        URL,
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def load_template():
    """Load the HTML template."""
    with open("animals_template.html", "r", encoding="utf-8") as file:
        return file.read()


def serialize_animal(animal_obj):
    """Convert one animal into an HTML card."""
    output = ['<li class="cards__item">\n']

    if "name" in animal_obj:
        output.append(
            f'  <div class="card__title">{animal_obj["name"]}</div>\n'
        )

    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    output.append('  <div class="card__text">\n')
    output.append('    <ul class="animal__details">\n')

    if "diet" in characteristics:
        output.append(
            f'      <li class="animal__detail"><strong>Diet:</strong> '
            f'{characteristics["diet"]}</li>\n'
        )

    if locations:
        output.append(
            f'      <li class="animal__detail"><strong>Location:</strong> '
            f'{locations[0]}</li>\n'
        )

    if "type" in characteristics:
        output.append(
            f'      <li class="animal__detail"><strong>Type:</strong> '
            f'{characteristics["type"]}</li>\n'
        )

    output.append('    </ul>\n')
    output.append('  </div>\n')
    output.append('</li>\n')

    return "".join(output)


def create_animals_info(data):
    """Create HTML cards for all animals."""
    return "".join(serialize_animal(animal) for animal in data)


def create_html(template, animals_info):
    """Insert animal information into the HTML template."""
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_info)


def save_html(html):
    """Save the generated HTML to a file."""
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html)


def main():
    try:
        animal_name = input("Enter a name of an animal: ")

        data = load_animals(animal_name)

        if not data:
            animals_info = f"<h2>The animal '{animal_name}' does not exist.</h2>"
        else:
            animals_info = create_animals_info(data)

        template = load_template()
        html = create_html(template, animals_info)

        save_html(html)

        print("The file animals.html was created successfully.")

    except FileNotFoundError as error:
        print(f"File not found: {error.filename}")

    except requests.exceptions.RequestException as error:
        print(
            "Sorry, we couldn't connect to the animal database. "
            "Please check your internet connection and try again."
        )

    except RuntimeError as error:
        print(error)

    except PermissionError:
        print("Error: Permission denied.")

    except IsADirectoryError:
        print(
            "Error: A directory was provided instead of a file. "
            "Please check the file path."
        )

    except OSError:
        print(
            "Error: A file operation failed. "
            "Please check the file path and access permissions."
        )


if __name__ == "__main__":
    main()
