
from playwright.sync_api import Page, expect


def test_calculate_button(page: Page):
    page.goto("http://127.0.0.1:5000/")

    page.locator("#weight").fill("225")
    page.locator("#reps").fill("5")

    page.locator("#calculate-btn").click()

    expect(page.locator("#result")).to_have_text(
        "Estimated 1RM: 262.5 lbs"
    )
