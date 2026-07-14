# Smart News Notifier Bot for Bale Messenger

An intelligent Python application that monitors RSS feeds from news websites and filters articles based on specific keywords. The bot ensures that only relevant and new content is delivered to the user via the Bale Messenger API.

## Key Features
- **Automated News Monitoring:** Continuously tracks RSS feeds (e.g., Zoomit, Varzesh3) for the latest updates.
- **Keyword-Based Filtering:** Only notifies the user if the news title contains predefined keywords (e.g., "AI", "Python", "Unity").
- **Deduplication System:** Implements a history-tracking mechanism using a local text file (`news_history.txt`) to prevent sending the same news multiple times.
- **Bale API Integration:** Sends formatted alerts with titles and links directly to the user's chat.

## Tech Stack
- **Language:** Python 3.x
- **Libraries:** 
  - `feedparser` (for parsing RSS feeds)
  - `requests` (for API communication)
  - `os` (for file system management)
- **Platform:** Bale Messenger API

## Logic Workflow
1. **Fetch:** The bot parses the RSS feed of the target news site.
2. **Filter:** It checks if any of the target keywords exist in the news title.
3. **Verify:** It compares the article link against a local database (text file) to ensure it hasn't been sent before.
4. **Notify:** If the news is both relevant and new, it triggers a notification via the Bale Bot API.
5. **Save:** The link is added to the history file to avoid future duplication.

## How to Run
1. Clone this repository.
2. Update `TOKEN` and `CHAT_ID` in the code.
3. Run the script:
