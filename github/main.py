from selenium import webdriver
from selenium.webdriver.common.by import By

repositories = []

count = int(input("How many repositories do you want to analyze? "))

for i in range(count):
    url = input(f"Enter repository URL {i + 1}: ")
    repositories.append(url)

driver = webdriver.Chrome()

with open("github_report.txt", "w", encoding="utf-8") as file:

    file.write("GITHUB REPOSITORY REPORT\n")
    file.write("========================\n\n")

    for url in repositories:

        driver.get(url)

        parts = url.rstrip("/").split("/")

        owner = parts[-2]
        repository = parts[-1]

        description = driver.find_element(
            By.CSS_SELECTOR,
            'meta[name="description"]'
        ).get_attribute("content")

        stars = driver.find_element(
            By.ID,
            "repo-stars-counter-star"
        ).text

        forks = driver.find_element(
            By.ID,
            "repo-network-counter"
        ).text

        print()
        print("Repository:", repository)
        print("Owner:", owner)
        print("Description:", description)
        print("Stars:", stars)
        print("Forks:", forks)

        file.write(f"Repository: {repository}\n")
        file.write(f"Owner: {owner}\n")
        file.write(f"Description: {description}\n")
        file.write(f"Stars: {stars}\n")
        file.write(f"Forks: {forks}\n")
        file.write("------------------------\n\n")


print("Report saved to github_report.txt")

    