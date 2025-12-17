# Contributing to MO.RPG Bot

Thanks for your interest in contributing!  
This project is community-driven, and all help is appreciated.

---

## How Contributions Work

- Only maintainers can push directly to `main`
- All contributions happen through **forks and pull requests**

### Steps:
1. Fork the repository
2. Create a new branch for your change
3. Make your changes
4. Open a pull request (PR) to `main`

Please keep PRs focused and related to a single change or feature.

---

## Development Setup

### Requirements
- Python 3.10+
- A Discord bot token

### Setup
1. Clone your fork
2. Install dependencies:
   pip install -r requirements.txt

3. Copy `.env.example` to `.env` and add your token:

   ```env
   DISCORD_TOKEN=your_token_here
   ```
4. Run the bot:

   ```bash
   python main.py
   ```

If everything is set up correctly, the bot should log in and respond to `!hello`.

---

## Pull Request Guidelines

When opening a PR:

* Explain **what** you changed and **why**
* Test your changes locally
* Keep PRs reasonably small
* Be responsive to review feedback

PRs may be requested to change or may be closed if they do not meet project standards.

---

## AI-Assisted Contributions

AI-assisted code (e.g., ChatGPT, Copilot) is allowed.

However:

* You must understand the code you submit
* You are responsible for maintaining it
* You must be able to explain changes during review

PRs that appear to be unreviewed AI output may be rejected.

---

## Security Guidelines

* **Never commit bot tokens or secrets**
* Use environment variables for all sensitive values
* Be cautious with permissions and command abuse
* Consider rate limits and potential exploits

Security issues should be reported privately to the maintainers if possible.

---

## Code of Conduct

Be respectful and constructive.

Harassment, discrimination, or hostile behavior will not be tolerated.