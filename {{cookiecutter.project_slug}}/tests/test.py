import pytest
from django.test import TestCase
{% if cookiecutter.playwright == "true" %}
import os
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import sync_playwright, expect as sync_expect
from playwright.async_api import Page, expect


# ── Class-based UI tests (unittest-style, sync) ───────────────────────────────

# class UITests(StaticLiveServerTestCase):
#     """Example browser tests using the unittest class-based approach."""

#     pytestmark = pytest.mark.ui

#     @classmethod
#     def setUpClass(cls):
#         os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "1"
#         super().setUpClass()
#         cls.playwright = sync_playwright().start()
#         cls.browser = cls.playwright.chromium.launch(
#             headless=os.environ.get("HEADLESS", "true") == "true"
#         )
#         cls.page = cls.browser.new_page()

#     @classmethod
#     def tearDownClass(cls):
#         cls.page.close()
#         cls.browser.close()
#         cls.playwright.stop()
#         super().tearDownClass()
#         del os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"]

#     def setUp(self):
#         admin_username = "admin"
#         admin_password = "password"
#         get_user_model().objects.create_superuser(
#             username=admin_username,
#             password=admin_password,
#         )
#         self.page.goto(f"{self.live_server_url}/admin/login/")
#         self.page.fill("input[name='username']", admin_username)
#         self.page.fill("input[name='password']", admin_password)
#         self.page.click("input[type='submit']")
#         sync_expect(self.page).to_have_url(f"{self.live_server_url}/admin/")


# ── Pytest functional UI tests (async) ────────────────────────────────────────
#
# pytest-playwright provides async `page` / `browser` / `context` fixtures
# automatically when asyncio_mode = "auto" is set in pytest config.
# Django ORM calls are wrapped with sync_to_async so no event-loop conflicts
# occur — DJANGO_ALLOW_ASYNC_UNSAFE is not required.

# @pytest.fixture
# async def admin_user(db):
#     """Create and return a superuser for UI tests."""
#     return await sync_to_async(get_user_model().objects.create_superuser)(
#         username="admin",
#         password="password",
#     )


# @pytest.fixture
# async def logged_in_page(page: Page, live_server, admin_user):
#     """An async Playwright page already logged in to the Django admin."""
#     await page.goto(f"{live_server.url}/admin/login/")
#     await page.fill("input[name='username']", "admin")
#     await page.fill("input[name='password']", "password")
#     await page.click("input[type='submit']")
#     await expect(page).to_have_url(f"{live_server.url}/admin/")
#     return page


# @pytest.mark.ui
# @pytest.mark.django_db(transaction=True)
# async def test_admin_login(logged_in_page: Page, live_server):
#     """Verify an admin user can log in and reach the site administration page."""
#     await expect(logged_in_page).to_have_url(f"{live_server.url}/admin/")
#     await expect(logged_in_page.locator("h1")).to_contain_text("Site administration")

{% endif %}

# ── Non-browser unittest style tests ────────────────────────────────────────

# class ExampleTests(TestCase):
#     """Example Django unit tests."""

#     def test_placeholder(self):
#         """Replace with real tests."""
#         self.assertTrue(True)

# ── Non-browser pytest functional style tests ────────────────────────────────────────

# @pytest.mark.django_db
# def test_example():
#     """Example pytest functional test with database access."""
#     from django.contrib.auth import get_user_model
#     User = get_user_model()
#     user = User.objects.create_user(username="alice", password="secret")
#     assert User.objects.filter(username="alice").exists()
#     assert user.check_password("secret")
